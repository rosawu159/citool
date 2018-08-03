"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        # app = os.path.abspath('../../apps/TestApp/build/Release-iphonesimulator/TestApp-iphonesimulator.app')
        # app = os.path.abspath('/Users/switchvmiworld/Library/Developer/Xcode/Archives/AppRTC.app')
        app = os.path.abspath('/Users/switchvmiworld/Desktop/App2018-08-03-15-07-52/archive/Brahma.xcarchive/Products/Applications/AppRTC.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                "platformName": "iOS",
                "platformVersion": "11.4",
                # "deviceName": "iPhone 7",
                "deviceName": "iPhone 5s",
                "automationName": "XCUITest",
                "udid": "91d9a68fe684ddb592e9d99668e86605e1c8b57e",
            })

    def tearDown(self):
        self.driver.quit()

    def test_a_find_elements(self):

        sleep(2)
        # Tap x,y. click Notification allow
        textNotification = self.driver.tap([(228,329)])
        sleep(1)

        # define variable with xpath
        textHost = self.driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="host"]')
        textPort = self.driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="port"]')
        textUser = self.driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="user"]')
        textPasswd = self.driver.find_element_by_xpath('//XCUIElementTypeSecureTextField[@name="userPass"]')
        # select = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="AppStream"])[2]')
        # select2 = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="AD"])[2]')
        btn = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="logginButton"]')
        
        # input host,port,account
        textHost.send_keys("112.121.106.108")
        textPort.send_keys("3000")
        textUser.send_keys("bigrain")
        # click keyborad return 
        btnRutrun = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Return"]')
        btnRutrun.click()
        #input password
        textPasswd.send_keys("s123")
        btnRutrun.click()


        # define variable with xpath 
        # select = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="AppStream"])[2]')
        # select2 = self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="AD"])[2]')

        #select item
        # select.click()
        # select2.click()

        # define variable with xpath
        # btn = self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="logginButton"]')

        # click button
        btn.click()

        sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)