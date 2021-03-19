from appium import webdriver
import unittest


def des_cap_calendar_app():
    desired_caps = dict(
        platformName='iOS',
        platformVersion='12.4.5',
        automationName='XCUITest',
        udid='120a5ede58d4aeab0f4641213dac1f913b4ec6e0',
        deviceName='Qualitia',
        bundleId='com.apple.MobileSMS')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


