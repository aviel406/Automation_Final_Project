import pytest
from runners.browseruse_runner import BrowserUseRunner

@pytest.fixture
def browser_use():
    runner = BrowserUseRunner()
    yield runner
    runner.quit()

def test_open_login_page_browseruse(browser_use):
    browser_use.open_url("https://atidcollege.co.il/members/orgs/testnet/")