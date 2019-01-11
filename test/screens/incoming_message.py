
class IncommingMessage():

    def __init__(self, driver):
        self.driver = driver

    def trigger_notification(self):

        notification_trigger_button = self.driver.find_element_by_id('notify_app')
        notification_trigger_button.click()


