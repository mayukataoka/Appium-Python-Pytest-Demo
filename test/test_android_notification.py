import pytest
import os
import textwrap

from appium import webdriver
from helpers import take_screenhot_and_logcat, ANDROID_APP_PATH, EXECUTOR

PACKAGE = 'io.appium.android.apis'
INCOMING_MESSAGE_ACTIVITY = '.app.IncomingMessage'


def get_desired_capabilities():
    desired_caps = {
        'deviceName': os.getenv('UDID', 'Pixel_2_API_28'),
        'udid': os.getenv('UDID', 'emulator-5556'),
        'platformName': 'Android',
        'app': ANDROID_APP_PATH,
        'automationName': 'UIAutomator2',
        'appActivity': INCOMING_MESSAGE_ACTIVITY
    }

    return desired_caps


class TestAndroidBasicInteractions():


    @pytest.fixture(scope='function')
    def driver(self, request, device_logger):
        calling_request = request._pyfuncitem.name
        driver = webdriver.Remote(
            command_executor=EXECUTOR,
            desired_capabilities=get_desired_capabilities()
        )

        yield driver

        take_screenhot_and_logcat(driver, device_logger, calling_request)
        driver.quit()

    def test_should_send_notification_and_verifies_it(self, driver):

        notification_trigger_button = driver.find_element_by_id('notify_app')
        notification_trigger_button.click()
        driver.implicitly_wait(100)

        driver.open_notifications()
        notification_from_joe = driver.find_element_by_id('android:id/title')

        assert notification_from_joe.text == 'Joe'


