from selenium import  webdriver

class Login:
    def __init__(self,driver):
        self.driver=driver

    def login_jenkins(self,un,pwd):
        # Logint to application - section 2 >>S2
        self.driver.find_element_by_id("j_username").send_keys(un)
        self.driver.find_element_by_name("j_password").send_keys(pwd)
        self.driver.find_element_by_name("Submit").click()