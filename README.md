# Upload Instagram Profile Pic

Logs in to Instagram and uploads a photo using [instabot](https://github.com/instagrambot/instabot).

This is for personal use. Use it within Instagram's terms of service.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

On Windows, activate the virtualenv with `venv\Scripts\activate`.

Edit `.env` and set the variables below. The photo path and caption are the `PathOfPicInMachine` and `Caption` arguments in `main.py`.

## Environment variables

| Variable | Required | Description |
| --- | --- | --- |
| `INSTAGRAM_USERNAME` | yes | Instagram username |
| `INSTAGRAM_PASSWORD` | yes | Instagram password |

If either value is missing, the script prints the missing names and exits before logging in.

## Run

```bash
python main.py
```
