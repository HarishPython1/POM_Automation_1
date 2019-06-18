import pytest

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://localhost:8081/login")
    driver.implicitly_wait(30)
    request.cls.driver = driver
    # yield
    # driver.quit()


#  global driver
# driver = webdriver.Chrome(executable_path="C:/Users/btm-fac/PycharmProjects/POM_Automation/drivers/chromedriver.exe")
#         driver.get("http://localhost:8081/login")