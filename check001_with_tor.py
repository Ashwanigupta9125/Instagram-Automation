
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import webbrowser
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


url = 'https://www.google.com'

driver=webdriver.firefox(webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(r"C:\Program Files (x86)\TorBrowser\Browser\firefox.exe")).get('firefox'))
driver.get(url)


