from playwright.sync_api import Page, expect


def test_open_login(page: Page):
    url = 'http://localhost:3000/login'
    page.goto(url)

    expect(page).to_have_url('http://localhost:3000/login')

    expect(page).to_have_title('Task Management Board')