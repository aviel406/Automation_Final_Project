
import pytest
from runners.aluminum_runner import AluminumRunner

@pytest.fixture
def aluminum():
    runner = AluminumRunner()
    yield runner
    runner.quit()

def test_open_login_page(aluminum):
    aluminum.open_url("https://atidcollege.co.il/members/orgs/testnet/")