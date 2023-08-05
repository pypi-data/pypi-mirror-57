#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""TcEx Framework Profile Generation Module."""
import json
import os
import sys
from uuid import uuid4
from collections import OrderedDict
from random import randint

import colorama as c

from .bin import Bin
from ..app_config_object import InstallJson


class Profile(Bin):
    """Create profiles for ThreatConnect Job or Playbook App.

    Args:
        _args (namespace): The argparser args Namespace.
    """

    def __init__(self, _args):
        """Initialize Class properties.

        Args:
            _args (namespace): The argparser args Namespace.
        """

        super(Profile, self).__init__(_args)

        # properties
        self.data_dir = os.path.join(self.args.outdir, 'data')
        self.profile_dir = os.path.join(self.args.outdir, 'profiles')
        self.profiles = {}

    @staticmethod
    def _create_tcex_dirs():
        """Create tcex.d directory and sub directories."""

        dirs = ['tcex.d', 'tcex.d/data', 'tcex.d/profiles']
        for d in dirs:
            if not os.path.isdir(d):
                os.makedirs(d)

    def load_profiles(self):
        """Return configuration data.

        Load on first access, otherwise return existing data.

        .. code-block:: python

            self.profiles = {
                <profile name>: {
                    'data': {},
                    'ij_filename': <filename>,
                    'fqfn': 'tcex.json'
                }
        """
        if not os.path.isfile('tcex.json'):
            msg = 'The tcex.json config file is required.'
            sys.exit(msg)

        # create default directories
        self._create_tcex_dirs()

        # open tcex.json configuration file
        with open('tcex.json', 'r+') as fh:
            data = json.load(fh)
            if data.get('profiles') is not None:
                # no longer supporting profiles in tcex.json
                print((
                    '{}{}Migrating profiles from tcex.json to individual files.'.format(
                        c.Style.BRIGHT, c.Fore.YELLOW
                    )
                ))

                for profile in data.get('profiles') or []:
                    outfile = '{}.json'.format(
                        profile.get('profile_name').replace(' ', '_').lower()
                    )
                    self.profile_write(profile, outfile)

                # remove legacy profile key
                del data['profiles']
                data.setdefault('profile_include_dirs', [])
                if self.profile_dir not in data.get('profile_include_dirs'):
                    data['profile_include_dirs'].append(self.profile_dir)
            fh.seek(0)
            fh.write(json.dumps(data, indent=2, sort_keys=True))
            fh.truncate()

        # load includes
        for directory in data.get('profile_include_dirs') or []:
            self.load_profile_include(directory)

    def load_profiles_from_file(self, fqfn):
        """Load profiles from file.

        Args:
            fqfn (str): Fully qualified file name.
        """
        if self.args.verbose:
            print(('Loading profiles from File: {}{}{}'.format(c.Style.BRIGHT, c.Fore.MAGENTA, fqfn)))
        with open(fqfn, 'r+') as fh:
            data = json.load(fh)
            for profile in data:
                # force update old profiles
                self.profile_update(profile)
                if self.args.action == 'validate':
                    self.validate(profile)
            fh.seek(0)
            fh.write(json.dumps(data, indent=2, sort_keys=True))
            fh.truncate()

        for d in data:
            if d.get('profile_name') in self.profiles:
                self.handle_error(
                    'Found a duplicate profile name ({}).'.format(d.get('profile_name'))
                )
            self.profiles.setdefault(
                d.get('profile_name'),
                {'data': d, 'ij_filename': d.get('install_json'), 'fqfn': fqfn},
            )

    def load_profile_include(self, include_directory):
        """Load included configuration files.

        Args:
            include_directory (str): The path of the profile include directory.
        """

        include_directory = os.path.join(self.app_path, include_directory)
        if not os.path.isdir(include_directory):
            msg = 'Provided include directory does not exist ({}).'.format(include_directory)
            sys.exit(msg)

        for filename in sorted(os.listdir(include_directory)):
            if filename.endswith('.json'):
                fqfn = os.path.join(include_directory, filename)
                self.load_profiles_from_file(fqfn)

    def profile_create(self):
        """Create a profile."""
        if self.args.profile_name in self.profiles:
            self.handle_error('Profile "{}" already exists.'.format(self.args.profile_name))

        # load the install.json file defined as a arg (default: install.json)
        ij = InstallJson(self.args.ij, self.app_path)

        print((
            'Building Profile: {}{}{}'.format(c.Style.BRIGHT, c.Fore.CYAN, self.args.profile_name)
        ))
        profile = OrderedDict()
        profile['args'] = {}
        profile['args']['app'] = {}
        profile['args']['app']['optional'] = self.profile_settings_args(ij, False)
        profile['args']['app']['required'] = self.profile_settings_args(ij, True)
        profile['args']['default'] = self.profile_setting_default_args(ij)
        profile['autoclear'] = True
        profile['clear'] = []
        profile['description'] = ''
        profile['data_files'] = []
        profile['exit_codes'] = [0]
        profile['groups'] = [os.environ.get('TCEX_GROUP', 'qa-build')]
        profile['install_json'] = self.args.ij
        profile['profile_name'] = self.args.profile_name
        profile['quiet'] = False

        if ij.runtime_level.lower() == 'playbook':
            validations = self.profile_settings_validations
            profile['validations'] = validations.get('rules')
            profile['args']['default']['tc_playbook_out_variables'] = '{}'.format(
                ','.join(validations.get('outputs'))
            )
        return profile

    def profile_delete(self):
        """Delete an existing profile."""
        self.validate_profile_exists()

        profile_data = self.profiles.get(self.args.profile_name)
        fqfn = profile_data.get('fqfn')
        with open(fqfn, 'r+') as fh:
            data = json.load(fh)
            for profile in data:
                if profile.get('profile_name') == self.args.profile_name:
                    data.remove(profile)
            fh.seek(0)
            fh.write(json.dumps(data, indent=2, sort_keys=True))
            fh.truncate()

        if not data:
            # remove empty file
            os.remove(fqfn)

    def profile_settings_args(self, ij, required):
        """Return args based on install.json or layout.json params.

        Args:
            ij (dict): The install.json contents.
            required (bool): If True only required args will be returned.

        Returns:
            dict: Dictionary of required or optional App args.
        """
        if self.args.permutation_id is not None:
            if 'sqlite3' not in sys.modules:
                print('The sqlite3 module needs to be build-in to Python for this feature.')
                sys.exit(1)
            profile_args = self.profile_settings_args_layout_json(required)
        else:
            profile_args = ij.params_to_args(required=required)
        return profile_args

    @staticmethod
    def profile_setting_default_args(ij):
        """Build the default args for this profile.

        Args:
            ij (dict): The install.json contents.

        Returns:
            dict: The default args for a Job or Playbook App.
        """

        # build default args
        profile_default_args = OrderedDict()
        profile_default_args['api_default_org'] = '$env.API_DEFAULT_ORG'
        profile_default_args['api_access_id'] = '$env.API_ACCESS_ID'
        profile_default_args['api_secret_key'] = '$envs.API_SECRET_KEY'
        profile_default_args['tc_api_path'] = '$env.TC_API_PATH'
        profile_default_args['tc_docker'] = False
        profile_default_args['tc_in_path'] = 'log'
        profile_default_args['tc_log_level'] = 'debug'
        profile_default_args['tc_log_path'] = 'log'
        profile_default_args['tc_log_to_api'] = False
        profile_default_args['tc_out_path'] = 'log'
        profile_default_args['tc_proxy_external'] = False
        profile_default_args['tc_proxy_host'] = '$env.TC_PROXY_HOST'
        profile_default_args['tc_proxy_port'] = '$env.TC_PROXY_PORT'
        profile_default_args['tc_proxy_password'] = '$envs.TC_PROXY_PASSWORD'
        profile_default_args['tc_proxy_tc'] = False
        profile_default_args['tc_proxy_username'] = '$env.TC_PROXY_USERNAME'
        profile_default_args['tc_temp_path'] = 'log'
        if ij.runtime_level.lower() == 'playbook':
            profile_default_args['tc_playbook_db_type'] = 'Redis'
            profile_default_args['tc_playbook_db_context'] = str(uuid4())
            profile_default_args['tc_playbook_db_path'] = '$env.DB_PATH'
            profile_default_args['tc_playbook_db_port'] = '$env.DB_PORT'
            profile_default_args['tc_playbook_out_variables'] = ''
        return profile_default_args

    @property
    def profile_settings_validations(self):
        """Create 2 default validations rules for each output variable.

        * One validation rule to check that the output variable is not null.
        * One validation rule to ensure the output value is of the correct type.
        """

        ij = InstallJson(self.args.ij, self.app_path)
        validations = {'rules': [], 'outputs': []}

        job_id = randint(1000, 9999)
        output_variables = ij.playbook.get('outputVariables') or []
        if self.args.permutation_id is not None:
            output_variables = self._output_permutations[self.args.permutation_id]
        for o in output_variables:
            variable = '#App:{}:{}!{}'.format(job_id, o.get('name'), o.get('type'))
            validations['outputs'].append(variable)

            # null check
            od = OrderedDict()
            if o.get('type').endswith('Array'):
                od['data'] = [None, []]
                od['data_type'] = 'redis'
                od['operator'] = 'ni'
            else:
                od['data'] = None
                od['data_type'] = 'redis'
                od['operator'] = 'ne'
            od['variable'] = variable
            validations['rules'].append(od)

            # type check
            od = OrderedDict()
            if o.get('type').endswith('Array'):
                od['data'] = 'array'
                od['data_type'] = 'redis'
                od['operator'] = 'it'
            elif o.get('type').endswith('Binary'):
                od['data'] = 'binary'
                od['data_type'] = 'redis'
                od['operator'] = 'it'
            elif o.get('type').endswith('Entity') or o.get('type') == 'KeyValue':
                od['data'] = 'entity'
                od['data_type'] = 'redis'
                od['operator'] = 'it'
            else:
                od['data'] = 'string'
                od['data_type'] = 'redis'
                od['operator'] = 'it'
            od['variable'] = variable
            validations['rules'].append(od)
        return validations

    def profile_update(self, profile):
        """Update an existing profile with new parameters or remove deprecated parameters.

        Args:
            profile (dict): The dictionary containting the profile settings.
        """
        # warn about missing install_json parameter
        if profile.get('install_json') is None:
            print((
                '{}{}Missing install_json parameter for profile {}.'.format(
                    c.Style.BRIGHT, c.Fore.YELLOW, profile.get('profile_name')
                )
            ))

        # update args section to v2 schema
        self.profile_update_args_v2(profile)

        # update args section to v3 schema
        self.profile_update_args_v3(profile)

        # remove legacy script field
        self.profile_update_schema(profile)

    def profile_update_args_v2(self, profile):
        """Update v1 profile args to v2 schema for args.

        .. code-block:: javascript

            "args": {
                "app": {
                    "input_strings": "capitalize",
                    "tc_action": "Capitalize"
                }
            },
            "default": {
                "api_access_id": "$env.API_ACCESS_ID",
                "api_default_org": "$env.API_DEFAULT_ORG",
            },

        Args:
            profile (dict): The dictionary containting the profile settings.
        """
        ij = InstallJson(profile.get('install_json', 'install.json'), self.app_path)

        if (
            profile.get('args', {}).get('app') is None
            and profile.get('args', {}).get('default') is None
        ):
            _args = profile.pop('args')
            profile['args'] = {}
            profile['args']['app'] = {}
            profile['args']['default'] = {}
            for arg in ij.params_to_args():
                try:
                    profile['args']['app'][arg] = _args.pop(arg)
                except KeyError:
                    # set the value to the default?
                    # profile['args']['app'][arg] = self.profile_settings_args.get(arg)
                    # TODO: prompt to add missing input?
                    if self.args.verbose:
                        print((
                            '{}{}Input "{}" not found in profile "{}".'.format(
                                c.Style.BRIGHT, c.Fore.YELLOW, arg, profile.get('profile_name')
                            )
                        ))
            profile['args']['default'] = _args
            print((
                '{}{}Updating args section to v2 schema for profile {}.'.format(
                    c.Style.BRIGHT, c.Fore.YELLOW, profile.get('profile_name')
                )
            ))

    def profile_update_args_v3(self, profile):
        """Update v1 profile args to v3 schema for args.

        .. code-block:: javascript

            "args": {
                "app": {
                    "required": {
                        "input_strings": "capitalize",
                        "tc_action": "Capitalize"
                    },
                    "optional": {
                        "fail_on_error": true
                    }
                }
            },
            "default": {
                "api_access_id": "$env.API_ACCESS_ID",
                "api_default_org": "$env.API_DEFAULT_ORG",
            },

        Args:
            profile (dict): The dictionary containting the profile settings.
        """
        ij = InstallJson(profile.get('install_json', 'install.json'))

        if (
            profile.get('args', {}).get('app', {}).get('optional') is None
            and profile.get('args', {}).get('app', {}).get('required') is None
        ):
            app_args = profile['args'].pop('app')
            profile['args']['app'] = {}
            profile['args']['app']['optional'] = {}
            profile['args']['app']['required'] = {}
            for arg in ij.params_to_args():
                required = ij.params_dict.get(arg).get('required', False)

                try:
                    if required:
                        profile['args']['app']['required'][arg] = app_args.pop(arg)
                    else:
                        profile['args']['app']['optional'][arg] = app_args.pop(arg)
                except KeyError:
                    if self.args.verbose:
                        print((
                            '{}{}Input "{}" not found in profile "{}".'.format(
                                c.Style.BRIGHT, c.Fore.YELLOW, arg, profile.get('profile_name')
                            )
                        ))
            print((
                '{}{}Updating args section to v3 schema for profile {}.'.format(
                    c.Style.BRIGHT, c.Fore.YELLOW, profile.get('profile_name')
                )
            ))

    @staticmethod
    def profile_update_schema(profile):
        """Update profile to latest schema.

        Args:
            profile (dict): The dictionary containting the profile settings.
        """

        # add new "autoclear" field
        if profile.get('autoclear') is None:
            print((
                '{}{}Profile Update: Adding new "autoclear" parameter.'.format(
                    c.Style.BRIGHT, c.Fore.YELLOW
                )
            ))
            profile['autoclear'] = True

        # add new "data_type" field
        for validation in profile.get('validations') or []:
            if validation.get('data_type') is None:
                print((
                    '{}{}Profile Update: Adding new "data_type" parameter.'.format(
                        c.Style.BRIGHT, c.Fore.YELLOW
                    )
                ))
                validation['data_type'] = 'redis'

        # remove "script" parameter from profile
        if profile.get('install_json') is not None and profile.get('script') is not None:
            print((
                '{}{}Removing deprecated "script" parameter.'.format(c.Style.BRIGHT, c.Fore.YELLOW)
            ))
            profile.pop('script')

    def profile_write(self, profile, outfile=None):
        """Write the profile to the output directory.

        Args:
            profile (dict): The dictionary containting the profile settings.
            outfile (str, optional): Defaults to None. The filename for the profile.
        """

        # fully qualified output file
        if outfile is None:
            outfile = '{}.json'.format(profile.get('profile_name').replace(' ', '_').lower())
        fqpn = os.path.join(self.profile_dir, outfile)

        if os.path.isfile(fqpn):
            # append
            print(('Append to File: {}{}{}'.format(c.Style.BRIGHT, c.Fore.CYAN, fqpn)))
            with open(fqpn, 'r+') as fh:
                try:
                    data = json.load(fh, object_pairs_hook=OrderedDict)
                except ValueError as e:
                    self.handle_error('Can not parse JSON data ({}).'.format(e))

                data.append(profile)
                fh.seek(0)
                fh.write(json.dumps(data, indent=2, sort_keys=True))
                fh.truncate()
        else:
            print(('Create File: {}{}{}'.format(c.Style.BRIGHT, c.Fore.CYAN, fqpn)))
            with open(fqpn, 'w') as fh:
                data = [profile]
                fh.write(json.dumps(data, indent=2, sort_keys=True))

    def replace_validation(self):
        """Replace the validation configuration in the selected profile.

        TODO: Update this method.

        """

        self.validate_profile_exists()
        profile_data = self.profiles.get(self.args.profile_name)

        # check redis
        # if redis is None:
        #     self.handle_error('Could not get connection to Redis')

        # load hash
        redis_hash = profile_data.get('data', {}).get('args', {}).get('tc_playbook_db_context')
        if redis_hash is None:
            self.handle_error('Could not find redis hash (db context).')

        # load data
        data = self.redis.hgetall(redis_hash)
        if data is None:
            self.handle_error('Could not load data for hash {}.'.format(redis_hash))
        validations = {'rules': [], 'outputs': []}
        for v, d in list(data.items()):
            variable = v.decode('utf-8')
            # data = d.decode('utf-8')
            data = json.loads(d.decode('utf-8'))
            # if data == 'null':
            if data is None:
                continue
            validations['outputs'].append(variable)

            # null check
            od = OrderedDict()
            od['data'] = data
            od['data_type'] = 'redis'
            od['operator'] = 'eq'
            od['variable'] = variable
            # if variable.endswith('Array'):
            #     od['data'] = json.loads(data)
            #     od['data_type'] = 'redis'
            #     od['operator'] = 'eq'
            #     od['variable'] = variable
            # elif variable.endswith('Binary'):
            #     od['data'] = json.loads(data)
            #     od['data_type'] = 'redis'
            #     od['operator'] = 'eq'
            #     od['variable'] = variable
            # elif variable.endswith('String'):
            #     od['data'] = json.loads(data)
            #     od['data_type'] = 'redis'
            #     od['operator'] = 'eq'
            #     od['variable'] = variable
            validations['rules'].append(od)

        fqfn = profile_data.get('fqfn')
        with open(fqfn, 'r+') as fh:
            data = json.load(fh)
            for profile in data:
                if profile.get('profile_name') == self.args.profile_name:
                    profile['validations'] = validations.get('rules')
                    profile['args']['default']['tc_playbook_out_variables'] = ','.join(
                        validations.get('outputs')
                    )
            fh.seek(0)
            fh.write(json.dumps(data, indent=2, sort_keys=True))
            fh.truncate()

    def validate(self, profile):
        """Check to see if any args are "missing" from profile.

        Validate all args from install.json are in the profile.  This can be helpful to validate
        that any new args added to App are included in the profiles.

        .. Note:: This method does not work with layout.json Apps.

        Args:
            profile (dict): The current profile to validate.
        """

        ij = InstallJson(profile.get('install_json'), self.app_path)
        print(('{}{}Profile: "{}".'.format(c.Style.BRIGHT, c.Fore.BLUE, profile.get('profile_name'))))
        for arg in ij.params_to_args():
            if profile.get('args', {}).get('app', {}).get(arg) is None:
                print(('{}{}Input "{}" not found.'.format(c.Style.BRIGHT, c.Fore.YELLOW, arg)))

    def validate_profile_exists(self):
        """Validate the provided profiles name exists."""

        if self.args.profile_name not in self.profiles:
            self.handle_error('Could not find profile "{}"'.format(self.args.profile_name))
