# Import WebDriverWait class with alias W
from selenium.webdriver.support.ui import WebDriverWait as W
# Import expected_conditions class with alias EC
from selenium.webdriver.support import expected_conditions as EC

# Import locators from the local module
from .locators import IndexPageLocators



class BasePage(object):
    """
    Base page class containing common actions performed on web pages.
    """

    def __init__(self, driver):
        # Initialize with a web driver instance
        self.driver = driver

    def do_clear(self, locator):
        # Wait for element to be visible and clear its contents
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        # Wait for element to be visible and click it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        # Wait for element to be visible and submit it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        # Wait for element to be visible and send text input to it
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        # Wait for element to be visible and return it
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        # Wait for all elements to be visible and return them
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        # Wait for element to be visible and return its text
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

class IndexPage(BasePage):
    """
    Index page class containing specific actions performed on the index page.
    """

    def is_title_matches(self):
        # Check if the title matches the expected value
        return 'Digital Gold | Home' in self.driver.title

    def is_index_heading_displayed_correctly(self):
        # Get text of the index heading element
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'DIGITAL GOLD'
        # Return True if text is found in the index heading, else False
        return text in index_heading

    def is_intro_link_works(self):
        # Click on the intro link element
        self.do_click(IndexPageLocators.INTRO_LINK)
        # Get text of the intro heading element
        intro_heading = self.get_element_text(IndexPageLocators.INTRO_HEADING)
        # Return True if text is found in the intro heading, else False
        return 'BITCOIN IS A DECENTRALIZED' in intro_heading

    def is_intro_close_button_works(self):
        # Click on the close button element
        self.do_click(IndexPageLocators.CLOSE_BUTTON)
        # Get text of the index heading element
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'DIGITAL GOLD'
        # Return True if text is found in the index heading, else False
        return text in index_heading

    def is_signals_link_works(self):
        # Click on the signals link element
        self.do_click(IndexPageLocators.SIGNALS_LINK)
        # Get text of the signals heading element
        signals_heading = self.get_element_text(IndexPageLocators.SIGNALS_HEADING)
        # Return True if text is found in the signals heading, else False
        return 'BTC/USD TECHNICAL SIGNALS' in signals_heading

    def is_signals_close_button_works(self):
        # Click on the signals close button element
        self.do_click(IndexPageLocators.SIGNALS_CLOSE_BUTTON)
        # Get text of the index heading element
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'DIGITAL GOLD'
        # Return True if text is found in the index heading, else False
        return text in index_heading

    def is_about_link_works(self):
        # Click on the about link element
        self.do_click(IndexPageLocators.ABOUT_LINK)
        # Get text of the about heading element
        about_heading = self.get_element_text(IndexPageLocators.ABOUT_HEADING)
        # Return True if text is found in the about heading, else False
        return 'TECHNICAL ANALYSIS IS A RESEARCH' in about_heading

    def is_about_close_button_works(self):
        # Click on the about close button element
        self.do_click(IndexPageLocators.ABOUT_CLOSE_BUTTON)
        # Get text of the index heading element
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'DIGITAL GOLD'
        # Return True if text is found in the index heading, else False
        return text in index_heading

    def is_contact_link_works(self):
        # Click on the contact link element
        self.do_click(IndexPageLocators.CONTACT_LINK)
        # Get text of the subscribe paragraph element
        subscribe_para = self.get_element_text(IndexPageLocators.SUB_PARA)
        # Return True if text is found in the subscribe paragraph, else False
        return 'Subscribe to our CryptoStrategy eNewsletter' in subscribe_para
    
    def is_subscribe_form_works(self):
        # Clear the email field element
        self.do_clear(IndexPageLocators.EMAIL_FIELD)
        # Send keys to the email field element
        self.do_send_keys(IndexPageLocators.EMAIL_FIELD, 'digitalmj@gmail.com')
        # Submit the email field element
        self.do_submit(IndexPageLocators.EMAIL_FIELD)
        # Get text of the success message element
        success_msg = self.get_element_text(IndexPageLocators.SUCCESS_MSG)
        # Return True if text is found in the success message, else False
        return 'Thank you for your email.' in success_msg

    
   
