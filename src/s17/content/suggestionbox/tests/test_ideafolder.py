# -*- coding: utf-8 -*-

import unittest2 as unittest

from AccessControl import Unauthorized

from zope.component import createObject
from zope.component import queryUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID

from sc.essencis.ideias.content import IIdeaFolder
from sc.essencis.ideias.testing import INTEGRATION_TESTING

ctype = 's17.content.suggestionbox.ideafolder'


class IntegrationTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory(ctype, 'obj')
        self.obj = self.folder['obj']

    def test_adding(self):
        self.assertTrue(IIdeaFolder.providedBy(self.obj))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name=ctype)
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name=ctype)
        schema = fti.lookupSchema()
        self.assertEquals(IIdeaFolder, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name=ctype)
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(IIdeaFolder.providedBy(new_object))

    def test_is_referenceable(self):
        self.assertTrue(IReferenceable.providedBy(self.obj))
        self.assertTrue(IAttributeUUID.providedBy(self.obj))

    def test_allowed_content_types(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        types = ['s17.content.suggestionbox.idea']
        allowed_types = [t.getId() for t in self.obj.allowedContentTypes()]
        for t in types:
            self.assertTrue(t in allowed_types)

        # trying to add any other content type raises an error
        self.assertRaises(ValueError,
                          self.obj.invokeFactory, 'Document', 'foo')

        try:
            self.obj.invokeFactory('s17.content.suggestionbox.idea', 'foo')
        except Unauthorized:
            self.fail()


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
