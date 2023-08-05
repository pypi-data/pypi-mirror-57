# -*- coding: utf-8 -*-
"""Test the TcEx Threat Intel Module."""

from ..tcex_init import tcex


# pylint: disable=W0201
class TestHostIndicators:
    """Test TcEx Host Indicators."""

    def setup_class(self):
        """Configure setup before all tests."""
        self.ti = tcex.ti

    @staticmethod
    def test_update_hostname(hostname='www.hostname-title-42353.com'):
        """Testing changing the hostname before sending save request to TC"""
        ti = tcex.ti.indicator(
            indicator_type='Host',
            owner=tcex.args.tc_owner,
            hostname=hostname,
            dns_active=True,
            whois_active=True,
        )
        hostname = 'www.hostname-title-42333.com'
        ti.set(hostname=hostname)
        r = ti.create()
        assert r.ok
        ti_data = r.json()
        assert ti_data.get('status') == 'Success'
        assert ti_data.get('data').get('host').get('hostName') == hostname
        ti.delete()

    @staticmethod
    def test_attributes(hostname='www.hostname-title-42353.com'):
        """Tests adding, fetching, updating, and deleting host attributes"""
        ti = tcex.ti.indicator(
            indicator_type='Host',
            owner=tcex.args.tc_owner,
            hostname=hostname,
            dns_active=True,
            whois_active=True,
        )
        ti.create()

        # assert that attribute is created.
        r = ti.add_attribute('description', 'description1')
        assert r.ok

        # assert that attribute data is correct
        json = r.json().get('data', {}).get('attribute', {})
        assert json.get('type').lower() == 'description'
        assert json.get('value').lower() == 'description1'
        for attribute in ti.attributes():
            assert attribute.get('value') == 'description1'

        # fetch the attribute id
        attribute_id = json.get('id')

        # assert that attribute is updated
        r = ti.update_attribute('description2', attribute_id)
        assert r.ok

        # assert that updated attribute data is correct
        for attribute in ti.attributes():
            assert attribute.get('value') == 'description2'

        # assert that attribute is deleted
        r = ti.delete_attribute(attribute_id)
        assert r.ok

        # assert that no attributes remain for this indicator/group/victim
        for attribute in ti.attributes():
            assert False

        # remove indicator/group/victim
        ti.delete()

    @staticmethod
    def test_host_attribute_create(hostname='www.hostname-title-42355.com'):
        """Tests that attributes can be appropriately added to hosts"""
        ti = tcex.ti.indicator(
            indicator_type='Host',
            owner=tcex.args.tc_owner,
            hostname=hostname,
            dns_active=True,
            whois_active=True,
        )
        ti.create()

        r = ti.add_attribute(
            attribute_type='External Date Created', attribute_value='2017-05-03T14:38:02Z'
        )
        assert r.ok

        attribute_data = r.json()
        attribute_id = attribute_data.get('data').get('attribute').get('id')
        r = ti.delete_attribute(attribute_id)
        assert r.ok

    def test_host_get(self, hostname='www.hostname-title-42353.com'):
        """Test host get."""
        # create
        self.host_create(hostname)

        # get
        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        r = ti.single()
        ti_data = r.json()
        assert r.status_code == 200
        assert ti_data.get('status') == 'Success'
        assert ti_data.get('data').get(ti.api_entity).get('hostName') == hostname

        # delete
        self.host_delete(hostname)

    def test_host_get_attributes(self, hostname='www.hostname-title-12453.com'):
        """Test host get."""
        # create
        self.host_create(hostname)
        self.test_host_add_attribute(False, hostname, 'Description', 'test1')
        self.test_host_add_attribute(False, hostname, 'Description', 'test2')
        self.test_host_add_attribute(False, hostname, 'Description', 'test3')

        # get attributes
        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        for attribute in ti.attributes():
            assert attribute
            break
        else:
            assert False

        # delete
        self.host_delete(hostname)

    def test_host_get_tags(self, hostname='www.hostname-title-64235.com'):
        """Test host get."""
        # create
        self.host_create(hostname)
        self.test_host_add_tag(False, hostname, 'One')
        self.test_host_add_tag(False, hostname, 'Two')

        # get tags
        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        for tag in ti.tags():
            assert tag.get('name')
            break
        else:
            assert False

        # delete
        self.host_delete(hostname)

    def test_host_get_include(self, hostname='www.hostname-title-78159.com'):
        """Test host get."""
        self.host_create(hostname)
        self.test_host_add_attribute(False, hostname, 'Description', 'test123')
        self.test_host_add_label(False, hostname, 'TLP:RED')
        self.test_host_add_tag(False, hostname, 'PyTest')

        parameters = {'includes': ['additional', 'attributes', 'labels', 'tags']}
        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        r = ti.single(params=parameters)
        ti_data = r.json()
        assert r.status_code == 200
        assert ti_data.get('status') == 'Success'
        assert ti_data.get('data').get('host').get('hostName') == hostname
        assert ti_data.get('data').get('host').get('attribute')[0].get('value') == 'test123'
        assert ti_data.get('data').get('host').get('securityLabel')[0].get('name') == 'TLP:RED'
        assert ti_data.get('data').get('host').get('tag')[0].get('name') == 'PyTest'

        # delete
        self.host_delete(hostname)

    def host_create(self, hostname='www.hostname-title-65341.com'):
        """Test host create."""
        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        r = ti.create()
        ti_data = r.json()
        assert r.status_code == 201
        assert ti_data.get('status') == 'Success'
        assert ti_data.get('data').get('host').get('hostName') == hostname

    def test_host_add_attribute(
        self,
        should_create=True,
        hostname='www.hostname-title-nkjvb.com',
        attribute_type='Description',
        attribute_value='Example Description.',
    ):
        """Test host attribute add."""
        if should_create:
            self.host_create(hostname)

        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        r = ti.add_attribute(attribute_type=attribute_type, attribute_value=attribute_value)
        attribute_data = r.json()
        assert r.status_code == 201
        assert attribute_data.get('status') == 'Success'
        assert attribute_data.get('data').get('attribute').get('value') == attribute_value
        if should_create:
            self.host_delete(hostname)

    def test_host_add_label(
        self, should_create=True, hostname='www.hostname-title-ds4vb.com', label='TLP:GREEN'
    ):
        """Test host attribute add."""
        if should_create:
            self.host_create(hostname)

        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        r = ti.add_label(label=label)
        label_data = r.json()
        assert r.status_code == 201
        assert label_data.get('status') == 'Success'
        if should_create:
            self.host_delete(hostname)

    def test_host_add_tag(
        self, should_create=True, hostname='www.hostname-title-fdsv23.com', name='Crimeware'
    ):
        """Test host attribute add."""
        if should_create:
            self.host_create(hostname)

        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        r = ti.add_tag(name=name)
        tag_data = r.json()
        assert r.status_code == 201
        assert tag_data.get('status') == 'Success'
        if should_create:
            self.host_delete(hostname)

    def host_delete(self, hostname='www.hostname-title-523fa.com'):
        """Test host delete."""
        # create indicator
        self.host_create(hostname)

        # delete indicator
        ti = self.ti.host(hostname, owner=tcex.args.tc_owner)
        r = ti.delete()
        ti_data = r.json()
        assert r.status_code == 200
        assert ti_data.get('status') == 'Success'

    def test_host_update(self, hostname='www.hostname-title-b3da3.com'):
        """Test host update."""
        # create indicator
        self.host_create(hostname)

        # update indicator
        ti = self.ti.host(hostname, owner=tcex.args.tc_owner, rating=5, confidence=10)
        r = ti.update()
        ti_data = r.json()
        assert r.status_code == 200
        assert ti_data.get('status') == 'Success'
        assert ti_data.get('data').get('host').get('rating') == 5.0
        assert ti_data.get('data').get('host').get('confidence') == 10

        # delete indicator
        self.host_delete(hostname)
