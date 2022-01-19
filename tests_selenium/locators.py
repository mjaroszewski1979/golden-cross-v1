from selenium.webdriver.common.by import By

class IndexPageLocators(object):
    
    INDEX_HEADING = (By.CLASS_NAME, 'index-heading')
    INTRO_LINK = (By.LINK_TEXT, 'INTRO')
    INTRO_HEADING = (By.CLASS_NAME, 'intro-heading')
    CLOSE_BUTTON = (By.CLASS_NAME, 'close')
    SIGNALS_LINK = (By.LINK_TEXT, 'SIGNALS')
    SIGNALS_HEADING = (By.ID, 'signals-heading')
    SIGNALS_CLOSE_BUTTON = (By.XPATH, "//div[@id='main']//article[@id='signals']//div[@class='close']")
    ABOUT_LINK = (By.LINK_TEXT, 'ABOUT')
    ABOUT_HEADING = (By.CLASS_NAME, 'about-heading')
    ABOUT_CLOSE_BUTTON = (By.XPATH, "//div[@id='main']//article[@id='about']//div[@class='close']")
    CONTACT_LINK = (By.LINK_TEXT, 'CONTACT')
    SUB_PARA = (By.CLASS_NAME, 'subscribe-para')
    EMAIL_FIELD = (By.NAME, 'email')
    SUCCESS_MSG = (By.TAG_NAME, 'blockquote')





