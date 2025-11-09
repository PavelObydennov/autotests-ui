import pytest


@pytest.mark.smoke
def test_smoke_case():
    ...
@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.smoke
class TestSuite:
    @pytest.mark.slow
    def test_case1(self):
        ...


    def test_case2(self):
        ...


@pytest.mark.regression
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass