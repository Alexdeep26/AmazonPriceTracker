from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'Gaming Laptop'
CURRENCY = '$'
MIN_PRICE = '1000'
MAX_PRICE = '2500'
FILTERS = {
    'min' : MIN_PRICE,
    'max' : MAX_PRICE
}
BASE_URL = "https://www.amazon.ca/"

def get_chrome_driver(options) :
    return webdriver.Chrome('./chromedriver.exe',chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-error')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_automation_as_head_less(options):
    options.add_argument('--headless')