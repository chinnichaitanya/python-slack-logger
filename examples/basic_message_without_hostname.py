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
