# Import datetime module
import datetime
# Import WebDriver from Selenium
from selenium import webdriver
# Import StaticLiveServerTestCase from Django's testing module
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# Import timezone utility from Django
from django.utils import timezone

# Import Bitcoin model from gold app
from gold.models import Bitcoin
# Import page module from the current package
from . import page


class BitcoinTest(StaticLiveServerTestCase):
    """
    Test case for Bitcoin functionality using Selenium and live server.
    """

    def setUp(self):
        # Set up the test case with necessary preconditions
        # Initialize WebDriver instance for Chrome
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        
        # Set browser window size
        self.driver.set_window_size(1920, 1080)

        # Create a Bitcoin instance with predefined values
        self.bitcoin = Bitcoin(
            title = 'btc-usd',
            dema = 1000,
            ema = 1000,
            ht = 1000,
            kama = 1000,
            sar = 1000,
            sma = 1000,
            trima = 1000,
            wma = 1000,
            date_added = datetime.datetime.now(tz=timezone.utc)
        )
        # Save the Bitcoin instance to the database
        self.bitcoin.save()


    def tearDown(self):
        # Clean up after the test case
        # Close the WebDriver instance
        self.driver.close()


    def test_indexpage(self):
        # Test various functionalities on the index page
        # Open the live server URL in the browser
        self.driver.get(self.live_server_url)

        # Create an instance of IndexPage with the current WebDriver
        index_page = page.IndexPage(self.driver)

        # Assert that the title matches the expected value
        assert index_page.is_title_matches()

        # Assert that the index heading is displayed correctly
        assert index_page.is_index_heading_displayed_correctly()

        # Assert that the intro link works as expected
        assert index_page.is_intro_link_works()

        # Assert that the intro close button works as expected
        assert index_page.is_intro_close_button_works()

        # Assert that the signals link works as expected
        assert index_page.is_signals_link_works()

        # Assert that the signals close button works as expected
        assert index_page.is_signals_close_button_works()

        # Assert that the about link works as expected
        assert index_page.is_about_link_works()

        # Assert that the about close button works as expected
        assert index_page.is_about_close_button_works()

        # Assert that the contact link works as expected
        assert index_page.is_contact_link_works()

        # Assert that the subscribe form works as expected
        assert index_page.is_subscribe_form_works()
