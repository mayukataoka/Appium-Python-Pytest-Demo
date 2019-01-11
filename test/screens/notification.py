
class Notification():

    def __init__(self, driver):
        self.driver = driver

    def pull_down_system_tray(self):

        self.driver.open_notifications()

    def check_notification_from_joe(self):
        return self.driver.find_element_by_id('android:id/title').text == 'Joe'



