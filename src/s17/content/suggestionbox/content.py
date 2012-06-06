# -*- coding: utf-8 -*-

from plone.directives import form

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from s17.content.suggestionbox import MessageFactory as _


class ISuggestionBox(form.Schema):

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(''),
        required=False,
    )

class ISuggestion(form.Schema):

    text = RichText(
        title=_(u'Body text'),
        description=_(''),
        required=False,
    )