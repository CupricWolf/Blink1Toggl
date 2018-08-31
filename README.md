# Blink1Toggl

A small script that sets the color of a blink1 to the color of the currently running Toggl project's color. Requires the [blink1 cli tool][blink1-tool].

------

## Usage

`python3 Blink1Toggle.py [--root | --sudo]`

You'll need your Toggl account's API token set as the environment variable `TOGGL_API_KEY`.
The token can be found by following the directions [here][toggl_directions].
You can put the line `TOGGL_API_KEY="<Your key here>"` at the top of your crontab to set it for a cronjob call.

The optional argument `--root` or `--sudo` are for when your OS requires `blink1-tool` to be run as root (such as a Linux like OS).

[blink1-tool]: https://blink1.thingm.com/blink1-tool/
[toggl_directions]: https://github.com/toggl/toggl_api_docs#api-token

