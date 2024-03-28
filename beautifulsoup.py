import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque


async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()  # Await the response text coroutine
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

def is_valid(url, domain):
    parsed = urlparse(url)
    return bool(parsed.netloc) and parsed.netloc == domain


async def get_all_links_recursive(url, domain, visited, max_links=100):
    if url in visited or max_links == 0:
        return

    visited.add(url)
    async with aiohttp.ClientSession() as session:  # Create session within the loop
        try:
            html_content = await fetch_url(session, url)
            if html_content:
                soup = BeautifulSoup(html_content, "html.parser")
                for a_tag in soup.find_all("a", href=True):
                    href = a_tag.get("href")
                    if href:
                        href = urljoin(url, href)
                        if is_valid(href, domain) and href not in visited:
                            print(href)  # Print the unique URL directly
                            await get_all_links_recursive(url, domain, visited.copy(), max_links - 1)
        except Exception as e:
            print(f"Error processing {url}: {e}")


async def main(url, domain, max_links=100):
    visited = set()
    async with aiohttp.ClientSession() as session:  # Create session outside the loop
        await get_all_links_recursive(url, domain, visited, max_links)

if __name__ == "__main__":
    url = input("Please enter the URL: ")
    domain = urlparse(url).netloc
    asyncio.run(main(url, domain))
