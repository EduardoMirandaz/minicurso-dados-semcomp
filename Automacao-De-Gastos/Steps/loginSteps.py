
from ..Pages.loginPage import Browser as bw
import Pages.loginPage as lp
import sys
sys.path.insert(1, './Pages/loginPage')

class LoginSteps:

    def sucessfullLoginSteps():
        driver = bw.inicializarBrowser()

        # Login Input Steps
        login_box = driver.find_element("xpath", lp.fieldUser)
        login_box.click()
        login_box.send_keys('OI')

        # Password Input Steps
        password_box = driver.find_element("xpath", lp.fieldPassword)
        password_box.click()
        password_box.send_keys('123')

        # Password Input Steps
        enter_button = driver.find_element("xpath", lp.btnEnter)
        enter_button.click()

