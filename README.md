# Asynchronous Web Status Checker

This is a simple Python script that checks the status of multiple websites at the same time using `aiohttp` and `asyncio`. It’s a great way to learn how asynchronous programming works in Python!

---

## What Does This Script Do?

The script sends requests to multiple websites and checks their HTTP status codes (like 200 for success or 404 for not found). It does this all at once (concurrently), which makes it faster than checking each website one by one.

For example:
- If you want to check if a website is working, it will tell you if it’s up (status code 200) or down (status code like 404 or 500).
- If a website doesn’t work (e.g., invalid URL), it will show an error message instead of crashing.

---

You should see output like this:
```
https://www.example.com : 200
https://www.python.org : 200
https://www.github.com : 200
https://www.reddit.com : 200
Error fetching https://www.invalid-url.com : Cannot connect to host www.invalid-url.com:443 ssl:default [Name or service not known]
```

---

## Sample Code

Here’s the code for the script:

```python
import aiohttp
import asyncio

# List of websites to check
urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.reddit.com"
]

# Function to fetch the status of a website
async def fetch_status(session, url):
    try:
        async with session.get(url) as response:
            print(f"{url} : {response.status}")
    except Exception as e:
        print(f"Error fetching {url} : {e}")

# Main function to run all tasks concurrently
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

```

---

## How It Works

1. **URL List**: The script has a list of websites (`urls`) that it will check.
2. **Fetching Status**: For each website, it sends a request and prints the status code (e.g., 200 for success).
3. **Error Handling**: If a website doesn’t work (e.g., invalid URL), it shows an error message instead of crashing.
4. **Concurrency**: Instead of checking websites one by one, it checks them all at the same time using `asyncio.gather`.

---

## Why Is This Useful?

- **Faster**: Checking websites concurrently is much faster than doing it one by one.
- **Error Handling**: The script won’t crash if a website is down or has an invalid URL.
- **Learning Tool**: Great for beginners to learn about asynchronous programming in Python!

---

## Customizing the Script

You can change the list of websites in the `urls` variable to check different websites. For example:
```python
urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com"
]
```

Just replace the URLs with the ones you want to check!