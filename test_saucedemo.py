"""Homework 24: test_saucedemo"""
import pytest
# pylint: disable=redefined-outer-name
from playwright.sync_api import (
    sync_playwright,
    expect,
)  # type: ignore[import-not-found]


@pytest.fixture
def page():
    """Fixture that creates a new Playwright page in Chromium"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1500)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_successful_purchase_script(page) -> None:
    """Test_successful_purchase_script"""
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page.locator(".title")).to_have_text("Products")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    expect(page.locator(".title")).to_have_text("Your Cart")
    page.click("#checkout")
    page.fill("#first-name", "Andrey")
    page.fill("#last-name", "Sirota")
    page.fill("#postal-code", "247675")
    page.click("#continue")
    page.click("#finish")
    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!")
    page.click("#back-to-products")
    expect(page.locator(".title")).to_have_text("Products")
