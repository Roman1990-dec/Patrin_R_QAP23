from playwright.sync_api import Page, expect

from core.base_page import BasePage


class SavingsPage(BasePage):

    path = '/automation-lab/savings'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.goals_page = page.get_by_test_id('goals-page')
        self.page_title = page.locator('.savings-title')
        self.page_subtitle = page.locator('.savings-subtitle')
        self.create_goal_button = page.get_by_test_id('create-goal-button')
        self.empty_state = page.get_by_test_id('goals-empty-state')
        self.empty_state_title = page.locator('.savings-empty-title')
        self.empty_state_text = page.locator('.savings-empty-text')
        self.create_goal_cta = page.get_by_test_id('create-goal-cta')

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.goals_page).to_be_visible()

    def verify_empty_state(self) -> None:
        expect(self.page_title).to_have_text('Мои цели')
        expect(self.page_subtitle).to_contain_text('Копите на мечту по плану')
        expect(self.create_goal_button).to_be_visible()
        expect(self.create_goal_button).to_have_text('+ Создать цель')
        expect(self.empty_state).to_be_visible()
        expect(self.empty_state_title).to_have_text('Пока нет ни одной цели')
        expect(self.empty_state_text).to_contain_text('Создайте первую цель')
        expect(self.create_goal_cta).to_be_visible()
        expect(self.create_goal_cta).to_have_text('Создать первую цель')