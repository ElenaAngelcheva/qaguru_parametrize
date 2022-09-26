import pytest
from  selene.support.shared  import browser
from selene import have


@pytest.mark.parametrize('width, height', [pytest.param(1980, 1080, id='browser size: 1980x1080'),
                                           pytest.param(1500, 1000, id='browser size: 1500x1000'),
                                           pytest.param(1300, 1100, id='browser size: 1300x1100')])
def test_github_desktop(browser_open, width, height):
    browser.driver.set_window_size(width=width, height=height)
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('width, height', [
                    pytest.param(400, 882, id='browser size: 400x882')])
def test_github_mobile(browser_open, width, height):
     browser.element('.btn-mktg').click()
     browser.element(
          'a[href= "/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fuser_email%3D%26source%3Dform-home-signup"]'
                    ).click()
     browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))