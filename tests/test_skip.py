import pytest
from  selene.support.shared import browser
from selene import have

@pytest.mark.parametrize('browser_windows_size', [(1980, 1080), (1500, 1000), (1300, 1100)], indirect=True)
def test_github_desktop(browser_size):
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.skip()
@pytest.mark.parametrize('browser_windows_size', [(600, 800)], indirect=True)
def test_github_mobile(browser_size):
     browser.element('.btn-mktg').click()
     browser.element(
          'a[href= "/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fuser_email%3D%26source%3Dform-home-signup"]'
                    ).click()
     browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
