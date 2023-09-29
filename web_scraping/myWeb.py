import asyncio

from playwright.async_api import async_playwright


async def kun_uz_play():
    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://kun.uz/news/category/jahon')
        await page.screenshot(path='news.png', full_page=False)
        await page.wait_for_timeout(3000)


asyncio.run(kun_uz_play())

