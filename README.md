## How to test a notification in your system tray using Appium, Python and Pytest fixture. 
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
export AVD=Pixel_2_API_28 
cd /Users/<username>/Library/Android/sdk/emulator
./emulator -avd $AVD
``` 
2. Open the screen with a button that triggers a notification. 

Instead of opening each screen one by one to reach the destination screen, directly open target activity.

```
    desired_caps = {
        'deviceName': os.getenv('UDID', 'Pixel_2_API_28'),
        'udid': os.getenv('UDID', 'emulator-5556'),
        'platformName': 'Android',
        'app': ANDROID_APP_PATH,
        'automationName': 'UIAutomator2',
        'appActivity': INCOMING_MESSAGE_ACTIVITY
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
## Test env

### .bash_profile 
```
export ANDROID_HOME=/Users/<YOUR-USERNAME>/Library/Android/sdk
export ANDROID_SDK_ROOT=$ANDROID_HOME
export JAVA_HOME=$(/usr/libexec/java_home)

PATH=$PATH:$ANDROID_SDK_ROOT/tools/bin
PATH=$PATH:$ANDROID_SDK_ROOT/emulator
PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools
PATH=$PATH:$JAVA_HOME/bin
```
### Update SDK tools and packages
```
sdkmanager "platform-tools" "platforms;android-26"
sdkmanager "system-images;android-26;google_apis;x86"
```
### Create AVD
avdmanager create avd -n TestAvd -k "system-images;android-26;google_apis;x86" -d "Nexus 5X"
