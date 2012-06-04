# -*- coding: utf-8 -*-

from five import grok

from plone.directives import dexterity

from Products.CMFPlone.utils import getToolByName

from sc.essencis.ideias.content import IIdeaFolder, IIdea

grok.templatedir("templates")

class IdeaFolderView(dexterity.DisplayForm):
    grok.context(IIdeaFolder)
    grok.name("view")
    grok.template('ideafolder_view')
    grok.require("zope2.View")

class IdeaView(dexterity.DisplayForm):
    grok.context(IIdea)
    grok.name("view")
    grok.template('idea_view')
    grok.require('zope2.View')

    def images(self):
        ct = getToolByName(self.context,'portal_catalog')
        images = ct(portal_type='Image',path = '/'.join(self.context.getPhysicalPath()))
        if images:
            images = [ image.getObject() for image in images ]
            return images
        else:
            return None

    def files(self):
        ct = getToolByName(self.context,'portal_catalog')
        files = ct(portal_type='File',path = '/'.join(self.context.getPhysicalPath()))
        if files:
            return files
        else:
            return None
