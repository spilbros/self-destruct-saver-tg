# Self-Destruct Saver

Simple python script that automatically saves self-destructing photos and videos to your local storage.

## How it works

Listens for incoming self-destructing media in private chats and forwards it to a specified receiver.

## Requirements

- Docker
- Docker Compose

## Configuration

Create a `.env` file in the project root:
```env
API_ID=your_api_id
API_HASH=your_api_hash
RECIEVER=your_telegram_id
```

- `API_ID` and `API_HASH` — get them at [my.telegram.org](https://my.telegram.org)
- `RECIEVER` — Telegram user ID where saved media will be forwarded

## First run

On first launch you need to authorize your Telegram account interactively:
```bash
docker compose run --rm sd-saver
```

Enter your phone number and the confirmation code when prompted. The session will be saved in `./session/` and reused on subsequent runs.

## Run
```bash
docker compose up -d
```

## Logs
```bash
docker compose logs -f
```

