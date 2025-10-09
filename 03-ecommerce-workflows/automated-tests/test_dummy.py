import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy:
    def test_open_site(self):
        # open your local docker site
        self.driver.get("http://localhost:8080")
        print("Page title:", self.driver.title)
