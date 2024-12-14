""" Using Python Selenium Automation and Actionchains do Drag and Drop operations """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#Action chains
from selenium.webdriver.common.action_chains import ActionChains

#python selenium Exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class Data:
    URL="https://jqueryui.com/droppable/"

class Locators:
    SOURCE = "draggable"
    TARGET = "droppable"
class DragAndDropUsingActionChains(Data,Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actions = ActionChains(self.driver)
    def drag_drop(self):
        try:

            self.driver.maximize_window()
            self.driver.get(self.URL)
            sleep(3)
            self.driver.switch_to.frame(0) #the draggable and droppable element are inside the iframe
            source = self.driver.find_element(by=By.ID, value=self.SOURCE)
            target = self.driver.find_element(by=By.ID, value=self.TARGET)
            self.actions.drag_and_drop(source, target).perform()
            print("SUCCESS:Drag and Drop operation is Done!!!")
            sleep(3)

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(error)
        finally:
            self.driver.quit()
            print("Browser Closed")


if __name__ == "__main__":
    action = DragAndDropUsingActionChains()

    action.drag_drop()



