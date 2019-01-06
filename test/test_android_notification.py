import pytest
import os
import textwrap

from appium import webdriver
from helpers import take_screenhot_and_logcat, ANDROID_APP_PATH, EXECUTOR

class TestAndroidBasicInteractions():
    PACKAGE = 'io.appium.android.apis'
    INCOMING_MESSAGE_ACTIVITY = '.app.IncomingMessage'

    @pytest.fixture(scope='function')
    def driver(self, request, device_logger):
        calling_request = request._pyfuncitem.name
        driver = webdriver.Remote(
            command_executor=EXECUTOR,
            desired_capabilities={
                'app': ANDROID_APP_PATH,
                'platformName': 'Android',
                'automationName': 'UIAutomator2',
                'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '9',
                'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'emulator-5554',
                'appActivity': self.INCOMING_MESSAGE_ACTIVITY
            }
        )

        yield driver

        take_screenhot_and_logcat(driver, device_logger, calling_request)
        driver.quit()

    def test_should_send_notification_and_verifies_it(self, driver):

        notification_trigger_button = driver.find_element_by_id('notify_app')
        notification_trigger_button.click()
        driver.open_notifications()
        notification_from_joe = driver.find_element_by_id('android:id/title')

        assert notification_from_joe.text == 'Joe'


