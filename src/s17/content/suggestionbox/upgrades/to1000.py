# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName

from s17.content.suggestionbox.config import PRODUCTS

PROJECT = 's17.content.suggestionbox'


def fromZero(context):
    ''' Upgrade from Zero to version 1000
    '''

    qi = getToolByName(context, 'portal_quickinstaller')

    # Install dependencies for this upgrade
    # List package names
    packages = [
                 'collective.upload',
                 'cioppino.twothumbs',
               ]
    # (name,locked,hidden,install,profile,runProfile)
    dependencies = [(name, locked, hidden, profile) for name, locked, hidden, install,
                                                     profile, runProfile in
                    PRODUCTS if ((name in packages) and install)]

    for name, locked, hidden, profile in dependencies:
        qi.installProduct(name, locked=locked, hidden=hidden, profile=profile)
