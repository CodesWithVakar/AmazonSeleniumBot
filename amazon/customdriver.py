from selenium import webdriver
import amazon.constants as const
import os


class CustomDriver(webdriver.Chrome):
    def __init__(self, driver_path=const.DRIVER_PATH, teardown=False):
        self.driver_path= driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        # options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(CustomDriver, self).__init__(executable_path=const.DRIVER_PATH, options=options)
        self.implicitly_wait(10)
        # self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def get_driver(self):
        return self        
        

    
        