import webbrowser

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary(r"C:\Program Files (x86)\TorBrowser\Browser\firefox.exe")
# profile = FirefoxProfile(r"C:\Program Files (x86)\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default")
# driver = webdriver.Firefox(binary)

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(r"C:\Program Files (x86)\TorBrowser\Browser\firefox.exe"))

driver.get("http://stackoverflow.com")
driver.save_screenshot("screenshot.png")
driver.quit()