import os
import sys

from dotenv import load_dotenv
from instabot import Bot


def upload(username, password):
    bot = Bot()

    bot.login(username=username, password=password)
    bot.upload_photo("PathOfPicInMachine", caption="Caption")


def main():
    load_dotenv()
    username = os.environ.get("INSTAGRAM_USERNAME", "").strip()
    password = os.environ.get("INSTAGRAM_PASSWORD", "").strip()

    missing = []
    if not username:
        missing.append("INSTAGRAM_USERNAME")
    if not password:
        missing.append("INSTAGRAM_PASSWORD")
    if missing:
        print(
            "Missing Instagram credentials: "
            + ", ".join(missing)
            + ". Set them in the environment or in a .env file."
        )
        return 1

    try:
        upload(username, password)
    except (Exception, SystemExit):
        print("Invalid ID or Password: ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
