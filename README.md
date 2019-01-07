## Simple notification test with Appium, Python and Pytest fixture. 
<img src="notification-screenshot.png" width="400" height="400">

#### Test code

https://github.com/mayukataoka/Appium-Python-Pytest-Demo/blob/master/test/test_android_notification.py

#### Command line test execution.
```
$ pytest test/test_android_notification.py 
```

#### Test steps
1. Start an emulator from command line. 
```
cd /Users/<username>/Library/Android/sdk/emulator
./emulator -avd Pixel_2_API_28
``` 
2. Open the screen with a button that triggers a notification. 

In stead of opening each screen one by one to reach the destination screen, directly open target activity.

```
            desired_capabilities={
                'app': ANDROID_APP_PATH,
                'platformName': 'Android',
                'automationName': 'UIAutomator2',
                'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '9',
                'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'emulator-5554',
                'appActivity': self.INCOMING_MESSAGE_ACTIVITY
            }
```

or 

```
        driver.start_activity(self.PACKAGE, self.ACTIVITY)

```
3. Click on the button to trigger a notification
4. Open the notification screen. 

```
        driver.open_notifications()
```
5. Verify that the correct notification appeared. 
```
        notification_from_joe = driver.find_element_by_id('android:id/title')
        assert notification_from_joe.text == 'Joe'

```
6. Stop the emulator.
```
adb emu kill
```

