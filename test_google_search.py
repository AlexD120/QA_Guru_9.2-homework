from selene import be, have
from conftest import open_browser, browser_window, no_result_search
from selene.support.shared.jquery_style import s


def test_search_google(open_browser, browser_window):
    s('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    s('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_google_cat(open_browser, browser_window, no_result_search):
    s('[name="q"]').should(be.blank).type('купить средне-азиатского котенка циклопа лилового цвета ш312').press_enter()
    s('.card-section').should(have.text("По запросу купить средне-азиатского котенка циклопа лилового цвета ш312 ничего не найдено. "))