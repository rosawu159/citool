import os
from time import sleep
import pytest
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'GBAZCY02D044NV4'
        desired_caps['app'] = PATH('/home/rw/Downloads/app-debug.apk')
        desired_caps['appPackage'] = 'brahma.vmi.apportal'
        desired_caps['appActivity'] = 'brahma.vmi.brahmalibrary.wcitui.BrahmaLoginWITCActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    def test_a_find_elements(self):

        sleep(5)

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("112.121.106.180")
        textfields[1].send_keys("3000")
        textfields[2].send_keys("bigrain")
        textfields[3].send_keys("s123")

        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("brahma.vmi.apportal:id/vmi")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("brahma.vmi.apportal:id/standard")').click()

        el = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("brahma.vmi.apportal:id/buttonWCITLogin")')
        el.click()

        r = self.driver.get_window_size()
        x=r['width']*0.5
        y1=r['height']*0.5
        y2=r['height']*0.3
        action = TouchAction(self.driver)
        sleep(2)
        action.tap(None,500,1500,1).perform()
        sleep(5)
        action.press(None, x, y1).move_to(None, x, y2).release().perform()
        sleep(2)
        #action.tap(None,40,800,1).perform()#scanner
        action.press(None, x, y2).move_to(None, x, y1).release().perform()
        sleep(2)
        action.tap(None,250,850,1).perform()#firefox
        sleep(2)
        action.tap(None,400,300,1).perform()#clickURL
        driver.find_element_by_id("user_name").send_keys("fnngj")







if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)