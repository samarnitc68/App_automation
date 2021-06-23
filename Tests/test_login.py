import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import pytest
class Test_Cases:


    @pytest.fixture()
    def setup(self):
        desired_caps = {
            "deviceName": "Redmi",
            "platformName": "Android",
            "udid": "9cf2caba",
            "appPackage": "com.decurtis.crew.embark",
            "appActivity": "com.decurtis.crew.embark.MainActivity",
            "autowebview": True,
            "chromedriverExecutable": "C:\\Users\\AmbrishShukla\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        time.sleep(40)
        self.contexts = self.driver.contexts
        print(self.contexts)
        self.driver.switch_to.context(self.contexts[1])
    def test_login_code(self,setup):
        user = "Shubhra.vyas"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()

        password = "Gomo7411"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)

        # Enter Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        # Confirm Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        # Checking for login Confirmation
        name = self.driver.find_element_by_xpath("//div[@class='dashboard-profile__name']").text
        print(name)
        name1 = name.split('!')
        print(name1[1][1:])
        l = user.split('.')
        print(l[0])

        # check login failed or passed
        assert l[0].upper() == name1[1][1:], "Login Not succesfull "
        print("login Successfull")
        self.driver.implicitly_wait(5)
        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()


    def test_click_hamburger(self,setup):
        user = "Shubhra.vyas"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()

        password = "Gomo7411"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)

        # Enter Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        # Confirm Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[@class='HamburgerButton']").click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()

    def test_click_notifications(self,setup):
        user = "Shubhra.vyas"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()

        password = "Gomo7411"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)

        # Enter Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        # Confirm Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[@class='HamburgerButton']").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//div[@id='AUTOTEST__sidebar__simple__Notifications']").click()
        self.driver.implicitly_wait(10)
        TouchAction(self.driver).tap(x=77, y=159).perform()
        self.driver.implicitly_wait(5)
        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()

    def test_logout(self,setup):
        user = "Shubhra.vyas"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()

        password = "Gomo7411"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)

        # Enter Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        # Confirm Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[@class='HamburgerButton']").click()
        self.driver.implicitly_wait(20)
        TouchAction(self.driver).press(x=385, y=1725).move_to(x=388, y=532).release().perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//div[@class='sidebar-exit sidebar-panel__exit']").click()
        self.driver.find_element_by_xpath("//button[text()='Logout']").click()

        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()


    def test_wrong_password(self,setup):

        user = "Shubhra.vyas"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()

        password = "Gomo7412"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)
        val1=self.driver.find_element_by_xpath("//div[@class='error-message']").text
        print(val1)
        assert "Server" not in val1,"password is incorrect"
        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()

    # def test_wrong_user(self,setup):
    #     user = "jkjoioi"
    #     el1 = self.driver.find_element_by_xpath("//input[@id='username']")
    #     el1.click()
    #     el1.send_keys(user)
    #     TouchAction(self.driver).tap(x=984, y=2126).perform()
    #     password = "Gomo7411"
    #     el2 = self.driver.find_element_by_xpath("//input[@id='password']")
    #     el2.click()
    #     el2.send_keys(password)
    #     TouchAction(self.driver).tap(x=984, y=2107).perform()
    #     self.driver.implicitly_wait(10)
    #     val = self.driver.find_element_by_xpath("//div[@class='error-message']").text
    #     assert "incorrect" not in val, "user name or password incorrect"
    #     self.driver.switch_to.context(self.contexts[0])
    #     self.driver.quit()


    def test_wrong_user_password(self,setup):
        user = "jkjoioi"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()
        password = "Gomo7412"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)
        val = self.driver.find_element_by_xpath("//div[@class='error-message']").text
        assert "incorrect" not in val, "user name or password incorrect"
        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()
    def test_load_incident(self,setup):
        user = "Shubhra.vyas"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()

        password = "Gomo7411"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)

        # Enter Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        # Confirm Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[@class='HamburgerButton']").click()
        self.driver.implicitly_wait(20)
        TouchAction(self.driver).press(x=385, y=1725).move_to(x=388, y=532).release().perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//div[@id='AUTOTEST__sidebar__simple__Incident-Management']").click()
        time.sleep(15)
        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()

    def test_create_incident(self,setup):
        user = "Shubhra.vyas"
        el1 = self.driver.find_element_by_xpath("//input[@id='username']")
        el1.click()
        el1.send_keys(user)
        TouchAction(self.driver).tap(x=984, y=2126).perform()

        password = "Gomo7411"
        el2 = self.driver.find_element_by_xpath("//input[@id='password']")
        el2.click()
        el2.send_keys(password)
        TouchAction(self.driver).tap(x=984, y=2107).perform()
        self.driver.implicitly_wait(10)

        # Enter Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        # Confirm Pin
        for i in range(4):
            self.driver.find_element_by_xpath("//button[@id='KeyboardKey-1']").click()
        TouchAction(self.driver).tap(x=823, y=1968).perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[@class='HamburgerButton']").click()
        self.driver.implicitly_wait(20)
        TouchAction(self.driver).press(x=385, y=1725).move_to(x=388, y=532).release().perform()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//div[@id='AUTOTEST__sidebar__simple__Incident-Management']").click()
        time.sleep(15)
        TouchAction(self.driver).tap(x=968, y=2084).perform()
        self.driver.find_element_by_xpath("//div[@class='react-select__value-container react-select__value-container--has-value css-1hwfws3']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='react-select-3-option-1']").click()
        time.sleep(5)
        el3=self.driver.find_element_by_xpath("//input[@id='stateroom']")
        # el3.click()
        el3.send_keys("Shubra")
        self.driver.hide_keyboard()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='incidentCategoryTypes']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='react-select-4-option-0']").click()
        TouchAction(self.driver).press(x=480, y=1200).move_to(x=490, y=710).release().perform()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='incidentParentType']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[text()='Account/Billing']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='incidentCategories']").click()
        time.sleep(5)

        self.driver.find_element_by_xpath("//div[text()='Onboard Credit Not Applied']").click()
        time.sleep(3)
        TouchAction(self.driver)   .press(x=475, y=1800)   .move_to(x=480, y=1200)   .release()   .perform()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='assignedToTeamMember']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='react-select-8-option-0']").click()
        time.sleep(3)
        TouchAction(self.driver).press(x=487, y=1764).move_to(x=497, y=1219).release().perform()
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='description']").send_keys("hello you need to do")
        self.driver.find_element_by_xpath("//input[@id='raisedByNotes']").send_keys("hello ")
        self.driver.find_element_by_xpath("//input[@id='attendedByNotes']").send_keys("cheking")
        #self.driver.find_element_by_xpath("//input[@id='externalRefId']").send_keys("hey")
        time.sleep(5)
        self.driver.hide_keyboard()

        time.sleep(3)
        TouchAction(self.driver).press(x=487, y=1864).move_to(x=497, y=1219).release().perform()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='incidentReporter']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='react-select-10-option-1']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[text()='CREATE']").click()
        time.sleep(10)

        self.driver.switch_to.context(self.contexts[0])
        self.driver.quit()
