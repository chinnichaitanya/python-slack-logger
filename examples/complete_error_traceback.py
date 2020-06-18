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
