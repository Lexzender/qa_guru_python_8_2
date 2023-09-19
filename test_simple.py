from selene.support.shared import browser
from selene import be, have


def test_search_1():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fgdfgdfhdfhdfhfdhfdhdfhdfh').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу fgdfgdfhdfhdfhfdhfdhdfhdfh ничего не найдено.'))

def test_search_2():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
