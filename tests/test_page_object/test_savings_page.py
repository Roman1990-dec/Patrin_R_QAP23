import pytest
from playwright.sync_api import Page

from pages.automation_lab_page import AutomationLabPage
from pages.savings_page import SavingsPage


@pytest.mark.only
def test_open_savings_page_directly(page: Page):
    savings_page = SavingsPage(page)
    savings_page.open()

    savings_page.verify_page_opened()
    savings_page.verify_empty_state()


@pytest.mark.only
def test_open_savings_page_via_automation_lab(page: Page):
    automation_lab_page = AutomationLabPage(page)
    automation_lab_page.open()
    automation_lab_page.verify_page_opened()

    automation_lab_page.open_savings_page()

    savings_page = SavingsPage(page)
    savings_page.verify_page_opened()
    savings_page.verify_empty_state()