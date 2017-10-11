import argparse, time, os,getpass
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import datetime

browser = webdriver.PhantomJS()
browser.set_window_size(1024, 768)
browser.implicitly_wait(60)

load = ui.WebDriverWait(browser, 10)

def main():
    browser.get("http://kissmanga.com/Manga/Naruto")
    load.until(lambda browser: browser.find_element_by_class_name('listing'))
    browser.save_screenshot('screen1.png')

    browser.quit()

if __name__ == '__main__':
    main()