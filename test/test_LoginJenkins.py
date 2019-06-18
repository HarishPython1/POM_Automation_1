from pages.LoginPage import Login
from data.TestData import *
import pytest

#Launch browser and navigate to url- section 1 >>S1
@pytest.mark.usefixtures("test_setup")
class Test_Jenkins:
    def test_login(self):
        driver=self.driver
        lp=Login(driver)
        lp.login_jenkins(USER_NAME,PASSWORD)



#Logout from application - section 3 >>S3
# def test_logout():
#     driver.find_element_by_xpath("//b[text()='log out']").click()