import datetime
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import timezone
from selenium import webdriver
from . import page
from gold.models import Bitcoin



class BitcoinTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        
        self.driver.set_window_size(1920, 1080)
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
        self.bitcoin.save()


    def tearDown(self):
        self.driver.close()


    def test_indexpage(self):
        self.driver.get(self.live_server_url)
        index_page = page.IndexPage(self.driver)
        assert index_page.is_title_matches()
        assert index_page.is_index_heading_displayed_correctly()
        assert index_page.is_intro_link_works()
        assert index_page.is_intro_close_button_works()
        assert index_page.is_signals_link_works()
        assert index_page.is_signals_close_button_works()
        assert index_page.is_about_link_works()
        assert index_page.is_about_close_button_works()
        assert index_page.is_contact_link_works()
        assert index_page.is_subscribe_form_works()
