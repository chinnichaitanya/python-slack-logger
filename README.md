# Python Slack Logger

A custom message logger to Slack for Python 3.
This project was built using [`slackclient`](https://github.com/slackapi/python-slackclient)
and the latest [Block Kit UI](https://api.slack.com/block-kit).

This is the Slack alternative to [`discord-logger`](https://github.com/chinnichaitanya/python-discord-logger) package for Discord.

<a href="https://pypi.org/project/python-slack-logger/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/python-slack-logger"></a>
[![PyPI version](https://badge.fury.io/py/python-slack-logger.svg)](https://badge.fury.io/py/python-slack-logger)
<a href="https://pepy.tech/project/python-slack-logger"><img alt="Downloads" src="https://static.pepy.tech/badge/python-slack-logger"></a>
<a href="https://pypi.org/project/python-slack-logger/#files"><img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/python-slack-logger"></a>
[![License: MIT](https://img.shields.io/pypi/l/python-slack-logger)](https://github.com/chinnichaitanya/python-slack-logger/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## Install

Install via pip: `pip install python-slack-logger`

## Basic Usage

```python
from slack_logger import SlackLogger

token = "your slack app token"
options = {
    "service_name": "Backend API",
    "service_environment": "Production",
    "display_hostname": True,
    "default_level": "info",
}

logger = SlackLogger(token=token, **options)

channel = "#my_channel"
response = logger.send(
    channel=channel,
    title="Health Check",
    description="All services are running normally!",
)
```

![Image](https://raw.githubusercontent.com/chinnichaitanya/python-slack-logger/master/images/basic_message.png "Basic Usage")

## Configure various options

There are numerous configurations available to customise the message.

```python
options = {
    # Service name would be the name of the service sending the message to your Slack channel
    # This would usually be the name of the application sending the notification
    # If unset, the default value would be "Service"
    "service_name": "Backend API",

    # Usually services would run in staging and production environments
    # This field is to specify the environment from which the application is reponding for easy identification
    # If unset, this block would not appear in the message
    "service_environment": "Production",

    # An option to specify whether or not to display the hostname in the messages
    # The hostname is set by default, but it could be disabled by specifically setting this to `False`
    "display_hostname": True,

    # The default importance level of the message
    # The left bar color of the message would change depending on this
    # Available options are
    # - default: #1F2225
    # - error: #DB2828
    # - warn: #FBBD08
    # - info: #2185D0
    # - verbose: #6417C9
    # - debug: #2185D0
    # - success: #21BA45
    # If the `error` field is set during the construction of the message, the `level` is automatically set to `error`
    # If nothing is specified, `default` color would be used
    "default_level": "info",
}
```

## Emojis inbuilt! 😃

An appropriate emoji is automatically added before the title depending on the `level`.

Following is the map between `level` and the emoji added.

- default = `:mega:` 📣
- error = `:x:` ❌
- warn = `:warning:` ⚠️
- info = `:bell:` 🔔
- verbose = `:loud_sound:` 🔊
- debug = `:microscope:` 🔬
- success = `:rocket:` 🚀

## Examples

### Set Service Name and Environment for easy identification

You can configure the log message with service name and environment for easy identification.
The `Host` field which is the hostname of the server is automatically added for every message.

You can even send any meta information like the data in the variables, module names, metrics etc with the `metadata` field while constructing the message.
These data should be passed as a dictionary.

```python
from slack_logger import SlackLogger

token = "your slack app token"
options = {
    "service_name": "Backend API",
    "service_environment": "Production",
    "default_level": "info",
}

logger = SlackLogger(token=token, **options)

channel = "#my_channel"
response = logger.send(
    channel=channel,
    title="Health Check",
    description="Issue in establishing DB connections!",
    error="Traceback (most recent call last):\n ValueError: Database connect accepts only string as a parameter!",
    metadata={"module": "DBConnector", "host": 123.332},
)
```

![Image](https://raw.githubusercontent.com/chinnichaitanya/python-slack-logger/master/images/error_message.png "Message with Service Name, Icon and Environment")

### Send messages without Hostname

In case you do not want the hostname to be displayed in the message, disable it by setting `"display_hostname": False` in the `options` as follows.

```python
from slack_logger import SlackLogger

token = "your slack app token"
options = {
    "service_name": "Backend API",
    "service_environment": "Production",
    "display_hostname": False,
    "default_level": "info",
}

logger = SlackLogger(token=token, **options)

channel = "#my_channel"
response = logger.send(
    channel=channel,
    title="Health Check",
    description="All services are running normally!",
)
```

![Image](https://raw.githubusercontent.com/chinnichaitanya/python-slack-logger/master/images/basic_message_without_hostname.png "Basic message without Hostname")

### Send messages with different log-levels

The log-level indicates the importance of the message.
It changes the color of the Slack message in particular.
Currently supported levels are,

- `error`
- `warn`
- `info`
- `verbose`
- `debug`
- `success`

The log-level can be set during construction of the message like through the parameter `level`.

If the parameter isn't provided, it'll be set to the one given in `default_level`.
Any invalid input would be ignored and the log-level would be automatically be set to `default`.

Any complicated nested dictionary can be passed to the `metadata` field and the message gets forrmatted accordingly for easy reading.

```python
from slack_logger import SlackLogger

token = "your slack app token"
options = {
    "service_name": "Backend API",
    "service_environment": "Production",
    "default_level": "info",
}

logger = SlackLogger(token=token, **options)

channel = "#my_channel"
response = logger.send(
    channel=channel,
    title="Celery Task Manager",
    description="Successfully completed training job for model v1.3.3!",
    level="success",
    metadata={
        "Metrics": {
            "Accuracy": 78.9,
            "Inference time": "0.8 sec",
            "Model size": "32 MB",
        },
        "Deployment status": "progress",
    },
)
```

![Image](https://raw.githubusercontent.com/chinnichaitanya/python-slack-logger/master/images/success_message.png "Message with success log-level")

### Send complete error traceback

The `error` field can contain any error message.
It will be automatically be formatted in the final message.
For example, you can send a complete traceback of an error message to debug faster!

```python
import traceback

from slack_logger import SlackLogger


def get_traceback(e):
    tb = (
        "Traceback (most recent call last):\n"
        + "".join(traceback.format_list(traceback.extract_tb(e.__traceback__)))
        + type(e).__name__
        + ": "
        + str(e)
    )
    return tb


token = "your slack app token"
options = {
    "service_name": "Backend API",
    "service_environment": "Production",
    "default_level": "info",
}

err = KeyError("'email' field cannot be None")

logger = SlackLogger(token=token, **options)

channel = "#my_channel"
response = logger.send(
    channel=channel,
    title="Runtime Exception",
    description=err.__str__(),
    error=get_traceback(err),
    metadata={"email": None, "module": "auth", "method": "POST"},
)
```

![Image](https://raw.githubusercontent.com/chinnichaitanya/python-slack-logger/master/images/complete_error_traceback.png "Message with complete error traceback")
