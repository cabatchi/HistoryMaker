from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pyfiglet import figlet_format
from termcolor import cprint
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import names
import time
import random
from random import randint
from colorama import Fore, Back, Style
from colorama import init
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from random import randint
import pickle

init(autoreset=True)



cprint(figlet_format(('historymaker'), font='doom'), attrs=['bold'])

chromepath = ("Windows/chromedriver_win32/chromedriver.exe")



PROXY = input("Input a proxy. If you would like to run on localhost press 0\n")
chrome_options = webdriver.ChromeOptions()

if PROXY != 0:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)


minutes = input("How many minutes would you like to prepare for? ")
type(minutes)

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

class gSearch():
    def __call__(self):
        open('historywords.txt', 'r+')
        lines = open("historywords.txt").readlines() 
        line = lines[0] 
        words = line.split() 
        myword = random.choice(lines)
        
        chrome_options.add_argument("user-data-dir=selenium")
        url = "https://www.google.com/"
        driver.get(url)

        
        
        #login during this time!!!!
        time.sleep(30)

        url = "https://www.google.com/"
        driver.get(url)

        button1 = driver.find_element_by_class_name("gLFyf")
        button1.click()
        button1.send_keys("what is ", myword)
        driver.implicitly_wait(5)

        links = driver.find_elements_by_partial_link_text(':')
        l = links[randint(0, len(links)-1)]
        l.click()


        sleepTime = random.randint(5,180)
        time.sleep(sleepTime)

googleSearch = gSearch()

class yTube():
    def __call__(self):   
        chrome_options.add_argument("user-data-dir=selenium")
        url = "https://youtube.com"
        driver.get(url)

        
        #login during this time!!!!
        time.sleep(30)

        url = "https://youtube.com"
        driver.get(url)

        video = driver.find_elements_by_css_selector("#dismissable")
        videoChoose = video[randint(0, len(video)-1)]
        videoChoose.click()

        sleepTime = random.randint(5,4000)
        time.sleep(sleepTime)

youtube = yTube()

t_end = time.time() + 60 * float(minutes)
while time.time() < t_end:
    functions = [youtube(), googleSearch()]
    random.choice(functions)()





