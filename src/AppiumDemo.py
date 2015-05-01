__author__ = 'WP8Dev'
import os
import unittest
from appium import webdriver
''' ScrollTest.com by Promode '''
''' This Test Case Just Click on the Refresh Button My Application '''
''' Just Click and Verify it in you Phone '''
''' Copyright 2015 '''


class ContactAppTestAppium(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'A102'
        desired_caps['app'] = 'C:\PyEditor\Appium_ScrollTest\src\WitStatus.apk'
        desired_caps['appPackage'] = 'com.witmergers.getstatus'
        desired_caps['appActivity'] = '.MainActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_ClickRefreshLink(self):
        refreshButton  = self.driver.find_element_by_id("com.witmergers.getstatus:id/fab")
        self.assertTrue(refreshButton.is_displayed())
        refreshButton.click()
        ## Right now we are just verify the displayed message on the Phone
        ## You can right code to handle that toast message and Verify that message


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)


