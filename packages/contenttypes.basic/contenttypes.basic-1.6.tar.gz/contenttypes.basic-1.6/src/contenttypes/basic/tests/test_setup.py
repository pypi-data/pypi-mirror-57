# -*- coding: utf-8 -*-
from contenttypes.basic.testing import CONTENTTYPES_BASIC_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that contenttypes.basic is properly installed."""

    layer = CONTENTTYPES_BASIC_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if contenttypes.basic is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'contenttypes.basic'))

    def test_browserlayer(self):
        """Test that IContenttypesBasicLayer is registered."""
        from contenttypes.basic.interfaces import (
            IContenttypesBasicLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IContenttypesBasicLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CONTENTTYPES_BASIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['contenttypes.basic'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if contenttypes.basic is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'contenttypes.basic'))

    def test_browserlayer_removed(self):
        """Test that IContenttypesBasicLayer is removed."""
        from contenttypes.basic.interfaces import \
            IContenttypesBasicLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IContenttypesBasicLayer,
            utils.registered_layers())
