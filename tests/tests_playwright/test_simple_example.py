import re

import allure
import pytest
from playwright.sync_api import Page, expect


def test_homepage_has_playwright_in_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Fast and reliable end-to-end testing for modern web apps | Playwright "))


def test_open_subscription(page: Page):
    url = 'http://localhost:3000/automation-lab/subscription'
    page.goto(url)

    expect(page).to_have_url(url)
    expect(page).to_have_title('Task Management Board')


def test_open_login(page: Page):
    url = 'http://localhost:3000/login'
    page.goto(url)

    url = 'http://localhost:3000/automation-lab/subscription'
    page.goto(url)

    page.screenshot(path="simple_screenshot.png")

    url = 'https://playwright.dev/'
    page.goto(url)

    page.screenshot(path="full_page_screenshot.png", full_page=True)

    expect(page).to_have_url('http://localhost:3000/login')
    expect(page).to_have_title('Task Management Board1')


def test_example(page: Page) -> None:
    page.goto("http://localhost:3000/")
    page.locator("div").filter(has_text=re.compile(r"^Категории$")).click()

    page.get_by_role("link", name="Открыть →").nth(1).click()

    expect(page.get_by_test_id("period-section")).to_be_visible()
    expect(page.locator("div").filter(has_text="Номер картыММ / ГГCVV").nth(5)).to_be_visible()
    expect(page.get_by_test_id("tariffs-section")).to_be_visible()
    expect(page.get_by_test_id("summary-section")).to_be_visible()
    expect(page.get_by_test_id("promo-input")).to_be_visible()
    expect(page.get_by_role("main")).to_contain_text(
        "Форма для тестирования сервиса подписки, для практики техник тест-дизайна")
    expect(page.get_by_role("main")).to_match_aria_snapshot(
        "- heading \"Выберите период\" [level=2]\n- radiogroup \"Период подписки\":\n  - button \"1 месяц\"\n  - button /3 месяца -\\d+%/\n  - button /\\d+ месяцев -\\d+%/\n- heading \"Подключи подписку\" [level=2]\n- paragraph: Выбери период для подключения. Чем больше срок, тем больше выгода.\n- text: /\\d+/\n- heading \"Базовый\" [level=3]\n- text: /\\d+ ₷ за месяц При оплате/\n- strong: /2 \\d+ ₷/\n- text: /раз в \\d+ месяцев/\n- list:\n  - listitem: ✓ HD качество\n  - listitem: ✓ 1 устройство\n- text: /\\d+ \\d+%/\n- heading \"Премиум\" [level=3]\n- text: /\\d+ ₷ за месяц При оплате/\n- strong: /4 \\d+ ₷/\n- text: /раз в \\d+ месяцев/\n- list:\n  - listitem: /✓ [\\d,.]+[bkmBKM]+ Ultra HD/\n  - listitem: ✓ 4 устройства\n  - listitem: ✓ Без рекламы\n- text: /\\d+ \\d+%/\n- heading \"Семейный\" [level=3]\n- text: /\\d+ ₷ за месяц При оплате/\n- strong: /7 \\d+ ₷/\n- text: /раз в \\d+ месяцев/\n- list:\n  - listitem: /✓ [\\d,.]+[bkmBKM]+ Ultra HD/\n  - listitem: ✓ 6 устройств\n  - listitem: ✓ Без рекламы\n  - listitem: ✓ Детский профиль\n- paragraph: /1 месяц равен \\d+ календарным дням/\n- heading \"Промокод\" [level=2]\n- textbox \"Введите промокод\"\n- button \"Применить\" [disabled]\n- img\n- text: Номер карты\n- textbox \"Номер карты\":\n  - /placeholder: 0000 0000 0000 0000\n- text: ММ / ГГ\n- textbox \"ММ / ГГ\":\n  - /placeholder: MM/YY\n- text: CVV\n- textbox \"CVV\":\n  - /placeholder: •••\n- button \"Показать CVV\":\n  - img\n- heading \"Введи карту\" [level=2]\n- paragraph: /для подключения подписки StreamVibe\\. \\d+ месяцев за 7 \\d+ ₷, продление \\d+ мая \\d+ по этой же цене\\. Оплата пройдёт за \\d+ часа до продления\\./\n- text: /Тариф Семейный Период \\d+ месяцев Скидка за период -1 \\d+ ₷ Экономия 1 \\d+ ₷/\n- button /Подключить за 9 \\d+ 7 \\d+ ₷/ [disabled]")


def test_element_screenshot(page: Page) -> None:
    page.goto("http://localhost:3000/")
    page.locator("[class='hero hero--home']").screenshot(path='element_screenshot.png')



def test_locators(page: Page) -> None:
    page.goto("http://localhost:3000/automation-lab/subscription")

    hint = page.locator('[class="promo-hint-btn"]')
    container_card = page.locator('.payment-card-visual')
    card_fields = page.locator("//*[@class='card-fields']")

    text_title = page.get_by_text('Подключение подписки StreamVibe')
    text_enter_card = page.locator('text=Введи карту')

    pay_button = page.get_by_test_id("pay-button")
    goal = page.locator('[data-testid="task-goals-btn"]')

    date_exp = page.get_by_placeholder("MM/YY")
    date_exp_css = page.locator('[placeholder="MM/YY"]')


    container_family = page.locator('[data-tariff="premium"]').locator('.tariff-period-badge')
    container_family_2 = page.locator('.tariff-card').filter(has_text='Премиум')

    expect(hint).to_be_visible()
    expect(container_card).to_be_visible()
    expect(container_family_2).to_be_visible()
    expect(container_family).to_be_visible()
    expect(date_exp_css).to_be_visible()
    expect(date_exp).to_be_visible()
    expect(goal).to_be_visible()
    expect(pay_button).to_be_visible()
    expect(text_enter_card).to_be_visible()
    expect(text_title).to_be_visible()
    expect(card_fields).to_be_visible()


@pytest.mark.only
@allure.title("Ввод недействующего промокода")
@allure.description("При вводе истекшего промокода появляется сообщение об ошибке")
@allure.link("http://localhost:3000/automation-lab/subscription", name="Website")
@allure.issue("TMS-123")
@allure.testcase("tc-1231")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("UI", "Subscription", "Promocode")

@allure.epic('UI')
@allure.feature('Subscription')
@allure.story('Promocode')
def test_enter_old_promocode(page: Page) -> None:
    page.set_viewport_size({"width": 1960, "height": 1280})
    page.goto("http://localhost:3000/automation-lab/subscription")
    expect(page.locator('.promo-section')).to_be_visible()

    with allure.step('Ввод промокода'):
        input_promo = page.get_by_test_id('promo-input')
        expect(input_promo).to_be_editable()
        input_promo.fill('WELCOME10')

        png_bytes = page.screenshot()
        allure.attach(
            png_bytes,
            name="promoce",
            attachment_type=allure.attachment_type.PNG
        )


    with allure.step('Нажатие кнопки'):
        apply_button = page.get_by_test_id('promo-apply-btn')
        expect(apply_button).to_be_enabled()
        apply_button.click()

        png_bytes = page.screenshot()
        allure.attach(
            png_bytes,
            name="button",
            attachment_type=allure.attachment_type.PNG
        )

    assert_step(page)

    png_bytes = page.screenshot()
    allure.attach(
        png_bytes,
        name="result",
        attachment_type=allure.attachment_type.PNG
    )

@allure.step('Проверка отображения сообщения')
def assert_step(page):
    promo_message = page.get_by_test_id('promo-message')
    expect(promo_message).to_be_visible()
    expect(promo_message).to_contain_text('Промокод истек 31.12.2024')
    expect(promo_message).to_have_class('promo-message error')
    expect(promo_message).to_have_count(1)
    expect(promo_message).to_have_css(name='color', value='rgba(255, 90, 95, 0.95)')


def test_form_promocode(page: Page) -> None:
    page.set_viewport_size({"width": 1960, "height": 1280})
    page.goto("http://localhost:3000/automation-lab/subscription")

    input_promo = page.get_by_test_id('promo-input')
    expect(input_promo).to_have_attribute(name='maxlength', value='20')
    expect(input_promo).to_be_editable()
    input_promo.clear()

    apply_button = page.get_by_test_id('promo-apply-btn')
    expect(apply_button).to_be_disabled()

    input_promo.type('ALWAYS')

    promo_message = page.get_by_test_id('promo-message')
    expect(promo_message).to_be_hidden()