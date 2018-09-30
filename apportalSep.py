import os
from time import sleep
import pytest
import unittest
import sys
import threading
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    #device setting
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'FA76X1802626'
        desired_caps['app'] = PATH('/home/rw/Downloads/APPortal_for Rosa.apk')

        desired_caps['appPackage'] = 'brahma.vmi.apportal'
        desired_caps['appActivity'] = 'brahma.vmi.brahmalibrary.wcitui.BrahmaLoginWITCActivity'
        #desired_caps['noReset'] = True
        desired_caps['autoGrantPermissions'] = True

        self.driver = webdriver.Remote('http://localhost:7879/wd/hub', desired_caps)
    
    def test_a_find_elements(self):
        action = TouchAction(self.driver)

        sleep(2)

        #Finded all EditText
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys(sys.argv[1])
        action.tap(None,300,800,1).perform()

        textfields[1].send_keys(sys.argv[2])
        action.tap(None,300,800,1).perform()

        textfields[2].send_keys(sys.argv[3])
        action.tap(None,300,800,1).perform()

        textfields[3].send_keys(sys.argv[4])
        action.tap(None,300,800,1).perform()

        #select radio button
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("brahma.vmi.apportal:id/vmi")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("brahma.vmi.apportal:id/standard")').click()

        #click login button
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("brahma.vmi.apportal:id/buttonWCITLogin")').click()
         
        try:
             #if not found "login button" will be triggle "except". 
             self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("brahma.vmi.apportal:id/buttonWCITLogin")')
             os._exit(1)

        except:
             print("login success!")
             os._exit(0)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
