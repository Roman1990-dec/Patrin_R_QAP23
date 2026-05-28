from playwright.sync_api import Page, expect

from core.base_page import BasePage


class AutomationLabPage(BasePage):

    path = '/automation-lab'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.hero_title = page.locator('.hero-title')
        self.section_title = page.get_by_role('heading', name='Категории', exact=True)
        self.savings_card = page.get_by_test_id('feature-card-savings')
        self.open_savings_link = self.savings_card.get_by_role('link', name='Открыть →')

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.hero_title).to_contain_text('Web Automation Torture Lab')
        expect(self.section_title).to_be_visible()
        expect(self.savings_card).to_be_visible()

    def open_savings_page(self) -> None:
        self.open_savings_link.click()