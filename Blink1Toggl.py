#!/usr/bin/env python3

import urllib2, json, base64
from subprocess import call

# This script is run every minute or so by a cron job.
# It changes the color of a Blink1 according to the color associated with a toggl project.

# Variables
apiKey = b'INSERTAPIKEYHERE'

# Helper Methods
def apiRequestOpen (requestUrl):
    request = urllib2.Request(requestUrl)
    basicAuthString = b'Basic ' + (apiKey + b':api_token').encode('base64')
    request.add_header('Authorization', basicAuthString)
    return urllib2.urlopen(request)

# Main
responseCurrent = apiRequestOpen('https://www.toggl.com/api/v8/time_entries/current')
timeEntryJson = json.load(responseCurrent)
projectId = str(timeEntryJson['data']['pid'])

#2: GET from https://www.toggl.com/api/v8/projects/{project_id} for project color

#3: pair color # with actual RGB values

#4: send RGB values to blink1
