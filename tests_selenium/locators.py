from selenium.webdriver.common.by import By

class IndexPageLocators(object):

    # Locator for the main heading on the index page
    INDEX_HEADING = (By.CLASS_NAME, 'index-heading')

    # Locator for the 'INTRO' link
    INTRO_LINK = (By.LINK_TEXT, 'INTRO')

    # Locator for the heading under the 'INTRO' section
    INTRO_HEADING = (By.CLASS_NAME, 'intro-heading')

    # Locator for the close button element
    CLOSE_BUTTON = (By.CLASS_NAME, 'close')

    # Locator for the 'SIGNALS' link
    SIGNALS_LINK = (By.LINK_TEXT, 'SIGNALS')

    # Locator for the heading under the 'SIGNALS' section
    SIGNALS_HEADING = (By.ID, 'signals-heading')

    # Locator for the close button within the 'SIGNALS' section
    SIGNALS_CLOSE_BUTTON = (By.XPATH, "//div[@id='main']//article[@id='signals']//div[@class='close']")

    # Locator for the 'ABOUT' link
    ABOUT_LINK = (By.LINK_TEXT, 'ABOUT')

    # Locator for the heading under the 'ABOUT' section
    ABOUT_HEADING = (By.CLASS_NAME, 'about-heading')

    # Locator for the close button within the 'ABOUT' section
    ABOUT_CLOSE_BUTTON = (By.XPATH, "//div[@id='main']//article[@id='about']//div[@class='close']")

    # Locator for the 'CONTACT' link
    CONTACT_LINK = (By.LINK_TEXT, 'CONTACT')

    # Locator for the subscribe paragraph element
    SUB_PARA = (By.CLASS_NAME, 'subscribe-para')

    # Locator for the email input field
    EMAIL_FIELD = (By.NAME, 'email')

    # Locator for the success message element
    SUCCESS_MSG = (By.TAG_NAME, 'blockquote')





