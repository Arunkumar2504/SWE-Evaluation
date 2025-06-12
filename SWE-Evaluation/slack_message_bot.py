from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random
import time

client = WebClient(
    token="xoxb-9030018654706-9032585784292-4jvnaN4fVeOX2D9Y86bVwQ5B")

users = ["Alice", "Bob", "Charlie"]
channels = ["announcements", "daily_updates",
            "bugs", "tasks", "questions"]
messages = [
    "Just pushed my code!",
    "Looking into this issue now.",
    "Today's update is done.",
    "Any blockers from your side?",
    "Ready for the review call."
]

for _ in range(5):
    try:
        client.chat_postMessage(
            channel=random.choice(channels),
            text=random.choice(messages),
            username=random.choice(users)
        )
        time.sleep(2)
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")
