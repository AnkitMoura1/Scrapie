from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class Scrapie:
    try:
        def __init__(self):
            self.driver = webdriver.Chrome()
    except Exception as e:
        raise Exception("__init__ unable to create driver\n" + str(e))

    def close_window(self):
        """
        This function closes current tab
        :return:
        """
        try:
            self.driver.close()
            return True
        except Exception as e:
            raise Exception("(close_window): Failed to close current window\n" + str(e))

    def close_all_windows(self):
        """
        This function closes all tabs
        :return:
        """
        try:
            self.driver.quit()
            return True
        except Exception as e:
            raise Exception("(close_all_windows): Failed to close all windows\n" + str(e))

    def open_page(self, url):
        """
        This function opens Flipkart website
        :return:
        """
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            raise Exception("(open_page): Failed to open given page\n" + str(e))

    def get_element_by_xpath(self, xpath):
        """
        This function returns an html page element by Xpath
        :param xpath:
        :return:
        """
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element
        except Exception as e:
            raise Exception("(get_element_by_xpath): failed to get element\n" + str(e))

    def get_element_by_class(self, class_name):
        """
        This function returns element using class name
        :param class_name:
        :return:
        """
        try:
            return self.driver.find_element(By.CLASS_NAME, class_name)
        except Exception as e:
            raise Exception("(get_element_by_class): failed" + str(e))

    @staticmethod
    def click_element(element):
        """
        This Function Clicks given element
        :param element:
        :return:
        """
        try:
            element.click()
            return True
        except Exception as e:
            raise Exception("(click_element): Failed to click given element\n" + str(e))

    def double_click(self, element):
        """
        double click given element
        :param element:
        :return:
        """
        try:
            action = ActionChains(self.driver)
            action.double_click(element)
            action.perform()
            return True
        except Exception as e:
            raise Exception(f"(double click):failed to click {element}\n" + str(e))

    def wait_for_element_to_be_located_by_xpath(self, element_xpath):
        """
        This function stops driver to wait until a given element is
        located using xpath
        :param element_xpath:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, element_xpath))
            )
            return element
        except Exception as e:
            raise Exception(f"(wait_for_element_to_be_located_by_xpath): Failed to find {element_xpath}\n" + str(e))

    def maximize_window(self):
        """
        This function maximize the current tab
        :return:
        """
        try:
            self.driver.maximize_window()
            return True
        except Exception as e:
            raise Exception("(maximize_window): Failed to maximize current window\n" + str(e))

    def wait_for_element_to_be_located_by_id(self, element_id):
        """
        This function stops driver to wait until a given element is
        located using id
        :param element_id:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.ID, element_id))
            )
            return element
        except Exception as e:
            raise Exception("(wait_for_element_to_be_located_by_id): Failed\n" + str(e))

    def wait_for_element_to_be_located_by_name(self, element_name):
        """
        This function stops driver to wait until a given element is
        located using element name
        :param element_name:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.NAME, element_name))
            )
            return element
        except Exception as e:
            raise Exception("(wait_for_element_to_be_located_by_name): Failed\n" + str(e))

    def is_element_present_using_class(self, elements_class):
        """
        This function returns true if element is available in current page
        using class_name
        :param elements_class:
        :return:
        """
        try:
            element = self.wait_for_element_to_be_located_by_class_name(elements_class)
            if bool(element) != 0:
                return True
            else:
                return False
        except Exception as e:
            raise Exception("(is_element_present_using_class): Failed" + str(e))

    def wait_for_element_to_be_located_by_class_name(self, element_class_name):
        """
        This function stops driver to wait until a given element is
        located using class name
        :param element_class_name:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, element_class_name))
            )
            return element
        except Exception as e:
            raise Exception("(wait_for_element_to_be_located_by_class_name): Failed\n" + str(e))

    def wait_for_element_to_be_located_by_tag_name(self, element_tag_name):
        """
        This function stops driver to wait until a given element is
        located using tag name
        :param element_tag_name:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.TAG_NAME, element_tag_name))
            )
            return element
        except Exception as e:
            raise Exception("(wait_for_element_to_be_located_by_tag_name): Failed\n" + str(e))

    def wait_for_element_to_be_located_by_link_text(self, elements_link_text):
        """
        This function stops driver to wait until a given element is
        located using elements link text
        :param elements_link_text:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.LINK_TEXT, elements_link_text))
            )
            return element
        except Exception as e:
            raise Exception("(wait_for_element_to_be_located_by_link_text): Failed\n" + str(e))

    @staticmethod
    def type_something_in_given_element(element, text):
        """
        This function types given text in a given element like search box or in forms
        :param element:
        :param text:
        :return:
        """
        try:
            element.send_keys(text)
            return True
        except Exception as e:
            raise Exception(f"(type_something_in_given_element): Failed to type text in {element}\n" + str(e))

    @staticmethod
    def extract_text_from_element(element):
        """
        This functions returns text from given element
        :param element:
        :return:
        """
        try:
            return element.text
        except Exception as e:
            raise Exception(f"(extract_text_from_element): Failed to extract text from {element}\n" + str(e))

    def find_all_elements_of_given_class(self, class_name):
        """
        This function return all elements of given class
        :param class_name:
        :return:
        """
        try:
            if self.is_element_present_using_class(class_name):
                elements = self.driver.find_elements(By.CLASS_NAME, class_name)
                return elements
        except Exception as e:
            raise Exception(f"(find_all_elements_of_given_class): Failed class = {class_name}\n" + str(e))

    def switch_window(self, new_window):
        """
        This function switches current window
        :return:
        """
        try:
            self.driver.switch_to.window(new_window)

        except Exception as e:
            raise Exception(f"(switch_window): failed to switch to {new_window}\n" + str(e))

    def is_element_present_using_xpath(self, element_xpath):
        """
        This function returns true if element is available in given page
        :param element_xpath:
        :return:
        """
        try:
            element = self.wait_for_element_to_be_located_by_xpath(element_xpath)
            if bool(element) != 0:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(f'(is_element_present): failed to work' + str(e))

    def find_all_elements_by_xpath(self, xpath):
        """This function returns list of all elements using xpath
        """
        try:
            if self.is_element_present_using_xpath(xpath):
                lst = self.driver.find_elements(By.XPATH, xpath)
                return lst
        except Exception as e:
            raise Exception("(find_all_elements_by_xpath): failed\n" + str(e))

    def wait_for_new_window_to_open(self, current_handle):
        """
        This function puts driver to sleep until new window is opened
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(ec.new_window_is_opened([current_handle]))
        except Exception as e:
            raise Exception("(wait_for_new_window_to_open):failed\n" + str(e))
