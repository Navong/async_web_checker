import aiohttp
import asyncio

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.reddit.com"
]

async def fetch_status(session, url):
    try:
        async with session.get(url) as response:
            print(f"{url} : {response.status}")
    except Exception as e:
        print(f"Error fetching {url} : {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
