# -*- coding: utf-8 -*-
"""Test the TcEx Batch Module."""
import pytest


# pylint: disable=R0201,W0201
class TestEmbedded:
    """Test the TcEx Batch Module."""

    def stage_data(self, tcex):
        """Configure setup before all tests."""
        out_variables = []
        setattr(tcex.args, 'tc_playbook_out_variables', ','.join(out_variables))

        # add String inputs
        string_inputs = [
            {'variable': '#App:0001:string.1!String', 'data': 'DATA'},
            {'variable': '#App:0001:string.2!String', 'data': 'This is \"a string\"'},
            {'variable': '#App:0001:string.3!String', 'data': 'two'},
            {'variable': '#App:0001:string.4!String', 'data': 'one\ntwo\n'},
            {'variable': '#App:0001:string.5!String', 'data': r'\snow or later\s'},
            {'variable': '#App:0001:string.6!String', 'data': r'\snow is not \\snow.\s'},
            {'variable': '#App:0001:string.7!String', 'data': r'invalid json char " \\'},
            {
                'variable': '#App:0001:string.8!String',
                'data': r'Json Reserved Characters: \\\\" \n \r \f \b \t \\',
            },
        ]
        for i in string_inputs:
            tcex.playbook.create_string(i.get('variable'), i.get('data'))

        # add StringArray inputs
        string_array_inputs = [
            {
                'variable': '#App:0001:array.1!StringArray',
                'data': ['#App:0001:string.3!String', 'three'],
            },
            {
                'variable': '#App:0001:array.2!StringArray',
                'data': ['#App:0001:string.4!String', 'three\nfour\n'],
            },
        ]
        for i in string_array_inputs:
            tcex.playbook.create_string_array(i.get('variable'), i.get('data'))

        # add KeyValue inputs
        keyvalue_inputs = [
            {
                'variable': '#App:0001:keyvalue.1!KeyValue',
                'data': {'key': 'kv1', 'value': '#App:0001:string.3!String'},
            },
            {
                'variable': '#App:0001:keyvalue.2!KeyValue',
                'data': {'key': 'kv1', 'value': '#App:0001:array.1!StringArray'},
            },
            {
                'variable': '#App:0001:keyvalue.3!KeyValue',
                'data': {'key': 'kv1', 'value': '#App:0001:array.2!StringArray'},
            },
        ]
        for i in keyvalue_inputs:
            tcex.playbook.create_key_value(i.get('variable'), i.get('data'))

        # add KeyValueArray inputs
        keyvalue_array_inputs = [
            {
                'variable': '#App:0001:keyvalue.array.1!KeyValueArray',
                'data': [
                    {'key': 'kv.string', 'value': '#App:0001:string.3!String'},
                    {'key': 'kv.string.array', 'value': '#App:0001:array.1!StringArray'},
                ],
            }
        ]
        for i in keyvalue_array_inputs:
            tcex.playbook.create_key_value_array(i.get('variable'), i.get('data'))

    @pytest.mark.parametrize(
        'embedded_value,resolved_value',
        [
            (
                (
                    '{\n\"trackingID\": 12345,\n\"title\": \"#App:0001:string.7!String\",\n'
                    '\"comments\": \"#App:0001:string.8!String\",\n\"requestor\": '
                    '\"ThreatConnect Playbook\"}'
                ),
                (
                    '{\n\"trackingID\": 12345,\n\"title\": \"invalid json char \\" \\\\",\n'
                    '\"comments\": \"Json Reserved Characters: \\\\\\\\\\" \\n \\r \\f \\b \\t '
                    '\\\\",\n\"requestor\": \"ThreatConnect Playbook\"}'
                ),
            ),
            # test \s replacement
            (r'\stest', r' test'),
            (r'test\s', r'test '),
            (r'\stest\s', r' test '),
            (r'\\stest', r'\stest'),
            (r'test\\s', r'test\s'),
            (r'\\\somedir', r'\\somedir'),
            (r'\snow\sor\slater\s', ' now or later '),
            (
                '{"numbers": "#App:0001:string.4!String three\n\r"}',
                '{"numbers": "one\ntwo\n three\n\r"}',
            ),
            # String Test: new lines
            ('#App:0001:string.4!String', 'one\ntwo\n'),
            # String Test: escaped \n
            ('#App:0001:string.5!String', r'\snow or later\s'),
            # String Test: \s replacement
            ('#App:0001:string.6!String', r'\snow is not \\snow.\s'),
            # String Test: String in String
            ('This is #App:0001:string.1!String in a String.', 'This is DATA in a String.'),
            # String Test: StringArray in String
            (
                'This is #App:0001:array.1!StringArray in a String.',
                'This is ["two", "three"] in a String.',
            ),
            # String Test: KeyValue in String
            (
                'This is #App:0001:keyvalue.1!KeyValue in a String.',
                'This is {"value": "two", "key": "kv1"} in a String.',
            ),
            # String Test: KeyValueArray in String
            (
                'This is #App:0001:keyvalue.array.1!KeyValueArray in a String.',
                'This is [{"value": "two", "key": "kv.string"}, {"value": ["two", "three"], '
                '"key": "kv.string.array"}] in a String.',
            ),
            # String Test: String and StringArray in String
            (
                'This is #App:0001:string.1!String and #App:0001:array.1!StringArray in '
                'a String.',
                'This is DATA and ["two", "three"] in a String.',
            ),
            # String Test: service now use case
            ('{"work_notes": "#App:0001:string.4!String"}', '{"work_notes": "one\ntwo\n"}'),
            # KeyValueArray Test: Nested KeyValue
            (
                '{"key": "one", "value": #App:0001:keyvalue.1!KeyValue}',
                '{"key": "one", "value": {"value": "two", "key": "kv1"}}',
            ),
            (
                (
                    '{'
                    '    "KeyValue": #App:0001:keyvalue.1!KeyValue,'
                    '    "KeyValueArray": #App:0001:keyvalue.array.1!KeyValueArray,'
                    '    "String": "#App:0001:string.1!String",'
                    '    "StringArray": #App:0001:array.1!StringArray'
                    '}'
                ),
                (
                    '{'
                    '    "KeyValue": {"value": "two", "key": "kv1"},'
                    '    "KeyValueArray": '
                    '[{"value": "two", "key": "kv.string"}, '
                    '{"value": ["two", "three"], "key": "kv.string.array"}],'
                    '    "String": "DATA",'
                    '    "StringArray": ["two", "three"]'
                    '}'
                ),
            ),
            # StringArray Test: String in StringArray
            ('#App:0001:array.1!StringArray', ['two', 'three']),
        ],
    )
    def test_embedded_read_string(self, tcex, embedded_value, resolved_value):
        """Test playbook embedded string in string"""
        print(('\nredis    : <{}>'.format(repr(tcex.playbook.read(embedded_value)))))
        print(('\nresolved : <{}>'.format(repr(resolved_value))))
        print(('redis (type)   : {}'.format(type(tcex.playbook.read(embedded_value)))))
        print(('resolved (type): {}'.format(type(resolved_value))))

        # import json

        # embedded = json.loads(tcex.playbook.read(embedded_value))
        # print(json.dumps(embedded, indent=2))

        self.stage_data(tcex)
        assert tcex.playbook.read(embedded_value) == resolved_value

    @pytest.mark.parametrize(
        'variable,embedded_value,resolved_value',
        [
            (
                '#App:0001:embedded.string.1!String',
                'Test of embedded #App:0001:string.1!String in String.',
                'Test of embedded DATA in String.',
            ),
            (
                '#App:0001:embedded.string.1!String',
                '#App:0001:string.2!String inside a string.',
                'This is "a string" inside a string.',
            ),
            (
                '#App:0001:embedded.string.1!String',
                '{"work_notes": "#App:0001:string.4!String"}',
                '{"work_notes": "one\ntwo\n"}',
            ),
        ],
    )
    def test_embedded_string_in_string(self, tcex, variable, embedded_value, resolved_value):
        """Test playbook embedded string in string"""
        self.stage_data(tcex)
        tcex.playbook.create_string(variable, embedded_value)
        assert tcex.playbook.read(variable) == resolved_value

        # print('\nredis    : {}'.format(tcex.playbook.read(variable)))
        # print('resolved : {}'.format(resolved_value))
        # print('redis (type)   : {}'.format(type(tcex.playbook.read(variable))))
        # print('resolved (type): {}'.format(type(resolved_value)))

        tcex.playbook.delete(variable)
        assert tcex.playbook.read(variable) is None

    @pytest.mark.parametrize(
        'variable,embedded_value,resolved_value',
        [
            (
                '#App:0001:embedded.string.1!String',
                'Test of embedded #App:0001:array.1!StringArray in String.',
                'Test of embedded ["two", "three"] in String.',
            )
        ],
    )
    def test_embedded_string_array_in_string(self, tcex, variable, embedded_value, resolved_value):
        """Test playbook embedded string array in string"""
        self.stage_data(tcex)
        tcex.playbook.create_string(variable, embedded_value)
        assert tcex.playbook.read(variable) == resolved_value

        # print('redis    : {}'.format(tcex.playbook.read(variable)))
        # print('resolved : {}'.format(resolved_value))
        # print('redis (type)   : {}'.format(type(tcex.playbook.read(variable))))
        # print('resolved (type): {}'.format(type(resolved_value)))

        tcex.playbook.delete(variable)
        assert tcex.playbook.read(variable) is None

    @pytest.mark.parametrize(
        'variable,embedded_value,resolved_value',
        [
            (
                '#App:0001:embedded.string_array.2!StringArray',
                ['one', '#App:0001:string.3!String', 'three'],
                ['one', 'two', 'three'],
            )
        ],
    )
    def test_embedded_string_in_string_array(self, tcex, variable, embedded_value, resolved_value):
        """Test playbook embedded string in string array"""
        self.stage_data(tcex)
        tcex.playbook.create_string_array(variable, embedded_value)
        assert tcex.playbook.read(variable) == resolved_value

        # print('redis    : {}'.format(tcex.playbook.read(variable)))
        # print('resolved : {}'.format(resolved_value))
        # print('redis (type)   : {}'.format(type(tcex.playbook.read(variable))))
        # print('resolved (type): {}'.format(type(resolved_value)))

        tcex.playbook.delete(variable)
        assert tcex.playbook.read(variable) is None

    @pytest.mark.parametrize(
        'variable,embedded_value,resolved_value',
        [
            (
                '#App:0001:embedded.keyvalue.1!KeyValue',
                {'key': 'one', 'value': '#App:0001:string.3!String'},
                {'key': 'one', 'value': 'two'},
            )
        ],
    )
    def test_embedded_string_in_keyvalue(self, tcex, variable, embedded_value, resolved_value):
        """Test playbook embedded string array in string array"""
        self.stage_data(tcex)
        tcex.playbook.create_key_value(variable, embedded_value)
        assert tcex.playbook.read(variable) == resolved_value

        # print('redis    : {}'.format(tcex.playbook.read(variable)))
        # print('resolved : {}'.format(resolved_value))
        # print('redis (type)   : {}'.format(type(tcex.playbook.read(variable))))
        # print('resolved (type): {}'.format(type(resolved_value)))

        tcex.playbook.delete(variable)
        assert tcex.playbook.read(variable) is None

    @pytest.mark.parametrize(
        'variable,embedded_value,resolved_value',
        [
            (
                '#App:0001:embedded.keyvalue.1!KeyValue',
                {'key': 'one', 'value': '#App:0001:array.1!StringArray'},
                {'key': 'one', 'value': ['two', 'three']},
            )
        ],
    )
    def test_embedded_string_array_in_keyvalue(
        self, tcex, variable, embedded_value, resolved_value
    ):
        """Test playbook embedded string array in string array"""
        self.stage_data(tcex)
        tcex.playbook.create_key_value(variable, embedded_value)
        assert tcex.playbook.read(variable) == resolved_value

        # print('redis    : {}'.format(tcex.playbook.read(variable)))
        # print('resolved : {}'.format(resolved_value))
        # print('redis (type)   : {}'.format(type(tcex.playbook.read(variable))))
        # print('resolved (type): {}'.format(type(resolved_value)))

        tcex.playbook.delete(variable)
        assert tcex.playbook.read(variable) is None

    @pytest.mark.parametrize(
        'variable,embedded_value,resolved_value',
        [
            (
                '#App:0001:embedded.keyvalue.1!KeyValue',
                {'key': 'one', 'value': '#App:0001:keyvalue.1!KeyValue'},
                {'key': 'one', 'value': {'value': 'two', 'key': 'kv1'}},
            )
        ],
    )
    def test_embedded_keyvalue_in_keyvalue(self, tcex, variable, embedded_value, resolved_value):
        """Test playbook embedded string array in string array"""
        self.stage_data(tcex)
        tcex.playbook.create_key_value(variable, embedded_value)
        assert tcex.playbook.read(variable) == resolved_value

        # print('redis    : {}'.format(tcex.playbook.read(variable)))
        # print('resolved : {}'.format(resolved_value))
        # print('redis (type)   : {}'.format(type(tcex.playbook.read(variable))))
        # print('resolved (type): {}'.format(type(resolved_value)))

        tcex.playbook.delete(variable)
        assert tcex.playbook.read(variable) is None
