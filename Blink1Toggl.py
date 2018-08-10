#!/usr/bin/env python

import json
from base64 import b64encode
from urllib.request import Request, urlopen
from subprocess import call
from os import getenvb

# This script is run every minute or so by a cron job.
# It changes the color of a Blink1 according to the color associated with a toggl project.

# Variables
apiKey = getenvb(b'TOGGL_API_KEY')

# Helper Methods
def apiRequestOpen (requestUrl):
    """Opens url with authentication."""
    request = Request(requestUrl)
    basicAuthString = b'Basic ' + b64encode(b'%s:%s' % (apiKey, b'api_token'))
    request.add_header('Authorization', basicAuthString)
    return urlopen(request)

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# Main
timeEntryUrl = 'https://www.toggl.com/api/v8/time_entries/current'
responseCurrent = apiRequestOpen(timeEntryUrl)
timeEntryJson = json.load(responseCurrent)
if (timeEntryJson['data'] != None and 'pid' in timeEntryJson['data']):
    projectId = str(timeEntryJson['data']['pid'])

    projectUrl = 'https://www.toggl.com/api/v8/projects/' + projectId
    responseProject = apiRequestOpen(projectUrl)
    projectJson = json.load(responseProject)
    colorHex = str(projectJson['data']['hex_color'])

    red, green, blue = hex_to_rgb(colorHex)

    #4: send RGB values to blink1
    call(['blink1-tool', '--rgb',
      str(red) + ',' + str(green) + ',' + str(blue)])
else:
    call(['blink1-tool', '--rgb', '0,0,0'])
