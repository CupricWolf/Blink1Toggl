#!/usr/bin/env python3

import urllib2
import json
from subprocess import call

# This script is run every minute or so by a cron job.
# It changes the color of a Blink1 according to the color associated with a toggl project.

# Variables
