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
