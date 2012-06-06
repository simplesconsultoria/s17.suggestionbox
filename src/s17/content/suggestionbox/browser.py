# -*- coding: utf-8 -*-

from five import grok

from plone.directives import dexterity

from Products.CMFPlone.utils import getToolByName

from s17.content.suggestionbox.content import ISuggestionBox, ISuggestion

grok.templatedir("templates")

class SuggestionBoxView(dexterity.DisplayForm):
    grok.context(ISuggestionBox)
    grok.name("view")
    grok.template('suggestionbox_view')
    grok.require("zope2.View")

class SuggestionView(dexterity.DisplayForm):
    grok.context(ISuggestion)
    grok.name("view")
    grok.template('suggestion_view')
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
