from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r"C:\Program Files (x86)\TorBrowser\Browser\firefox.exe")
profile = FirefoxProfile(r"C:\Program Files (x86)\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default")
print("step 01")
driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
print("step 02")
driver.get("http://stackoverflow.com")
driver.save_screenshot("screenshot.png")
driver.quit()