#!/bin/bash

set -e

# first, create some pot containing anything
i18ndude rebuild-pot --pot s17.suggestionbox.pot --create s17.suggestionbox --merge manual.pot ..

# finally, update the po files
i18ndude sync --pot s17.suggestionbox.pot  `find . -iregex '.*\.po$'|grep -v plone`

