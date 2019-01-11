import pytest
import os
import textwrap


from appium import webdriver
from helpers import take_screenhot_and_logcat, ANDROID_APP_PATH, EXECUTOR
from screens.incoming_message import IncommingMessage
from screens.notification import Notification

PACKAGE = 'io.appium.android.apis'
INCOMING_MESSAGE_ACTIVITY = '.app.IncomingMessage'


def get_desired_capabilities():

    if os.getenv('PLATFORM') == 'Android':
        desired_caps = {
            'deviceName': 'Android Emulator',
            'avd': os.getenv('AVD', 'Pixel_2_API_28'),
            'platformName': 'Android',
            'app': ANDROID_APP_PATH,
            'automationName': 'UIAutomator2',
            'appActivity': INCOMING_MESSAGE_ACTIVITY
        }

    return desired_caps


class TestAndroidBasicInteractions():


    @pytest.fixture(scope='function')
    def driver(self, request, device_logger):
        os.system('cd /Users/mayukataoka/Library/Android/sdk/emulator')
        command = './emulator -avd ' + str(os.getenv('AVD'))
        os.system(command)

        calling_request = request._pyfuncitem.name
        driver = webdriver.Remote(
            command_executor=EXECUTOR,
            desired_capabilities=get_desired_capabilities()
        )

        yield driver

        driver.press_keycode(4)
        take_screenhot_and_logcat(driver, device_logger, calling_request)
        driver.quit()
        os.system('adb emu kill')

    def test_should_send_notification_and_verifies_it(self, driver):

        screen = IncommingMessage(driver)
        screen.trigger_notification()

        driver.implicitly_wait(100)

        system_tray = Notification(driver)
        system_tray.pull_down_system_tray()

        assert system_tray.check_notification_from_joe()

