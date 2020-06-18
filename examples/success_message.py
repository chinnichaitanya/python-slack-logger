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
