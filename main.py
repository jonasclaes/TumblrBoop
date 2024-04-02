import asyncio

import pyotp
from playwright.async_api import async_playwright

from config import ACCOUNT_EMAIL, ACCOUNT_PASSWORD, ACCOUNT_TOTP_SECRET, ACCOUNT_TO_BOOP, AMOUNT_OF_BOOPS_TO_SEND


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.tumblr.com/")
        await page.frame_locator("#cmp-app-container iframe").get_by_role("button", name="I Agree!").click()
        await page.get_by_label("Log in").click()
        await page.get_by_label("Continue with email").click()
        await page.get_by_placeholder("Email").click()
        await page.get_by_placeholder("Email").fill(ACCOUNT_EMAIL)
        await page.get_by_role("button", name="Next").click()
        await page.get_by_placeholder("Password", exact=True).click()
        await page.get_by_placeholder("Password", exact=True).fill(ACCOUNT_PASSWORD)
        await page.locator("#glass-container").get_by_label("Log in").click()

        if ACCOUNT_TOTP_SECRET:
            totp = pyotp.TOTP(ACCOUNT_TOTP_SECRET)
            await page.get_by_placeholder("Enter auth code").click()
            await page.get_by_placeholder("Enter auth code").fill(totp.now())
            await page.locator("#glass-container").get_by_label("Log in").click()

        await page.get_by_label("Account", exact=True).wait_for()

        await page.goto(f"https://www.tumblr.com/{ACCOUNT_TO_BOOP}")

        for boop_number in range(0, AMOUNT_OF_BOOPS_TO_SEND):
            print(f"Sending {ACCOUNT_TO_BOOP} boop number: {boop_number+1}")
            await page.get_by_test_id("scroll-container").get_by_label("Boop").click()
            await page.get_by_label("boop", exact=True).click()
            await asyncio.sleep(1.5)

        await context.close()
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
