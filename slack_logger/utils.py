def bold(text):
    return "*" + str(text) + "*"


def code(text):
    return "```" + str(text) + "```"


def mrkdwn_block(markdown_text=None):
    _markdown_text = ""
    if markdown_text is not None:
        _markdown_text = str(markdown_text)

    return {"type": "section", "text": {"type": "mrkdwn", "text": _markdown_text}}


def fields_block(fields=None):
    _fields = list()
    if fields is not None:
        for key, value in fields.items():
            _field_text = bold(key + ":") + " " + value
            _field_item = {"type": "mrkdwn", "text": _field_text}
            _fields.append(_field_item)

    return {"type": "section", "fields": _fields}


def divider_block():
    return {"type": "divider"}
