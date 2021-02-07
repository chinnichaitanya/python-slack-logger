from socket import gethostname

import slack
from yaml import dump

from .utils import bold, code, divider_block, fields_block, mrkdwn_block


class SlackLogger:
    """
    Python message transporter for Slack
    """

    COLORS = {
        "default": "#1F2225",
        "error": "#DB2828",
        "warn": "#FBBD08",
        "info": "#2185D0",
        "verbose": "#6417C9",
        "debug": "#2185D0",
        "success": "#21BA45",
    }
    EMOJIS = {
        "default": ":mega:",
        "error": ":x:",
        "warn": ":warning:",
        "info": ":bell:",
        "verbose": ":loud_sound:",
        "debug": ":microscope:",
        "success": ":rocket:",
    }

    def __init__(self, token, **kwargs):
        if token is None:
            raise ValueError("The field token cannot be:", token)
        self.token = str(token)

        self.service_name = kwargs.get("service_name", "Service")
        if self.service_name is not None:
            self.service_name = str(self.service_name)

        self.service_environment = kwargs.get("service_environment")
        if self.service_environment is not None:
            self.service_environment = str(self.service_environment)

        self.host_name = gethostname()
        if kwargs.get("display_hostname") is False:
            self.host_name = None

        self.default_level = kwargs.get("default_level")
        if self.default_level not in self.COLORS.keys():
            self.default_level = "default"

        self.slack = slack.WebClient(token=self.token)

    def _construct_heading_block(self):
        _heading = "<!channel>"

        _block = mrkdwn_block(_heading)
        return _block

    def _construct_title_block(self, title=None, level=None):
        _emoji = None
        if level is not None:
            _emoji = self.EMOJIS.get(level)

        _title = ""
        if title is not None:
            _title = bold(title)
        if _emoji is not None:
            _title = _emoji + " " + _title

        _block = mrkdwn_block(_title)
        return _block

    def _construct_description_block(self, description=None):
        _description = ""
        if description is not None:
            _description = str(description)

        _block = mrkdwn_block(_description)
        return _block

    def _construct_error_block(self, error=None):
        _error = ""
        if error is not None:
            _error = str(error)

        _block = mrkdwn_block(bold("Error:") + "\n" + code(_error))
        return _block

    def _construct_metadata_block(self, metadata=None):
        _metadata = ""
        if metadata is not None:
            _metadata = dump(
                metadata, indent=4, default_flow_style=False, sort_keys=False
            )

        _block = mrkdwn_block(
            ":house_buildings: " + bold("Metadata:") + "\n" + code(_metadata)
        )
        return _block

    def _construct_environment_block(self):
        fields = {"Service": self.service_name}
        if self.host_name is not None:
            fields.update(
                {
                    "Host": self.host_name,
                }
            )
        if self.service_environment is not None:
            fields.update({"Environment": self.service_environment})

        _block = fields_block(fields=fields)
        return _block

    def send(
        self,
        channel,
        title=None,
        description=None,
        level=None,
        error=None,
        metadata=None,
    ):
        if channel is None:
            raise ValueError("The field channel cannot be:", channel)
        _channel = str(channel)

        _title = ""
        if title is not None:
            _title = str(title)

        _description = ""
        if description is not None:
            _description = str(description)

        _level = level
        if _level is None:
            _level = self.default_level
        if error is not None:
            _level = "error"
        _color = self.COLORS.get(_level)

        # The final list of all the blocks to be sent in the notification
        _blocks = list()

        _heading_block = self._construct_heading_block()
        _blocks.append(_heading_block)

        _title_block = self._construct_title_block(_title, _level)
        _blocks.append(_title_block)

        _description_block = self._construct_description_block(_description)
        _blocks.append(_description_block)

        if error is not None:
            # _blocks.append(divider_block())

            _error_block = self._construct_error_block(error)
            _blocks.append(_error_block)

        if metadata is not None:
            # _blocks.append(divider_block())

            _metadata_block = self._construct_metadata_block(metadata)
            _blocks.append(_metadata_block)

        _blocks.append(divider_block())

        _environment_block = self._construct_environment_block()
        _blocks.append(_environment_block)

        payload = {
            "channel": _channel,
            "attachments": [{"color": _color, "blocks": _blocks}],
        }

        response = self.slack.chat_postMessage(**payload)
        return response
