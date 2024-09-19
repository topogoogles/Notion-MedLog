import requests
from dotenv import load_dotenv
import os
import argparse
import datetime

# Load environment variables
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

if NOTION_TOKEN is None or DATABASE_ID is None:
    raise ValueError("NOTION_TOKEN and DATABASE_ID must be set")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Add a timestamp to Notion.")
    parser.add_argument(
        "timestamp",
        nargs="?",
        default=None,
        help="Timestamp in YYYY-MM-DD HH:MM:SS format",
    )
    return parser.parse_args()


def add_timestamp_to_notion(timestamp_str=None):
    if timestamp_str is None:
        # Use current time in UTC
        dt = datetime.datetime.now()
        timestamp = int(dt.timestamp())
        timestamp_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        # Parse the timestamp string with UTC timezone
        dt = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        timestamp = int(dt.timestamp())

    url = f"https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Datetime": {"title": [{"text": {"content": f"{timestamp_str}"}}]},
            "Timestamp": {"number": timestamp},
            "Source": {
                "type": "select",
                "select": {"name": "Python", "color": "purple"},
            },
        },
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Timestamp added successfully! {timestamp_str}")
    else:
        print(f"Failed to add timestamp: {response.text}")


if __name__ == "__main__":
    args = parse_arguments()
    add_timestamp_to_notion(args.timestamp)
