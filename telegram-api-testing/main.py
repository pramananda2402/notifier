from telethon import TelegramClient


API_ID = "25586620"
API_HASH = "e083e4de48554525267639785c2a9f64"
SESSION_NAME = "my_session" 

async def main():
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        print("Logged in as:", await client.get_me())

        

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
