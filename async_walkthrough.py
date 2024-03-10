import logging
import asyncio
import time


async def download_site(timer, url):
    # Imitate the call to the url
    await asyncio.sleep(timer)
    # Imitate some calculations done on the data returned by the site
    time.sleep(timer)


async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 10
    await asyncio.gather(
        download_site(0, 'https://www.jython.org'),
        download_site(4, 'http://olympus.realpython.org/dice'),
        download_site(1, 'https://api.artic.edu/api/v1/artworks')
    )


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')