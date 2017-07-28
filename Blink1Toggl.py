#!/usr/bin/env python

import urllib2, json, base64
from subprocess import call

# This script is run every minute or so by a cron job.
# It changes the color of a Blink1 according to the color associated with a toggl project.

# Variables
apiKey = b'INSERTAPIKEYHERE'

# Helper Methods
def apiRequestOpen (requestUrl):
    request = urllib2.Request(requestUrl)
    basicAuthString = (b'Basic ' + (apiKey + b':api_token')
                       .encode('base64').replace('\n', ''))
    request.add_header('Authorization', basicAuthString)
    return urllib2.urlopen(request)

# Main
timeEntryUrl = 'https://www.toggl.com/api/v8/time_entries/current'
responseCurrent = apiRequestOpen(timeEntryUrl)
timeEntryJson = json.load(responseCurrent)
projectId = str(timeEntryJson['data']['pid'])

projectUrl = 'https://www.toggl.com/api/v8/projects/' + projectId
responseProject = apiRequestOpen(projectUrl)
projectJson = json.load(responseProject)
colorHex = str(projectJson['data']['hex_color'])

#3: pair color # with actual RGB values

#4: send RGB values to blink1
