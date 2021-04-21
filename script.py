from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def headless():
    options = Options()
    options.headless = True
    return options

def startDriver():
    driver=webdriver.Edge()
    #driver = webdriver.Firefox(executable_path='/home/skaarface/Apps/WebDrivers/geckodriver')
    #driver = webdriver.Firefox(options=headless(),executable_path='/home/skaarface/Apps/WebDrivers/geckodriver')
    driver.get('https://www.91mobiles.com/phonefinder.php')
    return driver

def shutDown(driver):
    driver.close()

def scrollToEnd(driver):
    driver.execute_script("window.scrollTo(0,2500)")
    return

def nextListPage(driver):
    print(type(driver.find_element_by_xpath("//div[contains(@class, 'listing-btns4')]").is_enabled()))
    driver.find_element_by_xpath("//div[contains(@class, 'listing-btns4')]").click()

def isPageReady(driver,num):
    delay = 3
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-row="{}"]'.format(num))))
        return True
    except TimeoutException:
        return True

def getRow(driver):
    return driver.find_element_by_xpath("//div[contains(@class, 'filter-grey-bar')]")

def getName(elems):
    return elems.find_element_by_xpath("//a[@class='hover_blue_link name gaclick']").text

def getSpecLink(elems):
    return elems.find_element_by_xpath("//div[contains(@class, 'compare3')]").click()





def getRows(driver):
    return [item for item in driver.find_elements_by_xpath("//div[contains(@class, 'filter-grey-bar')]")]


"""
def makeList(names,getNames,driver):
    [names.append(name.text) for name in getNames(driver)]
    return



"""

driver=startDriver()
names,row_num=[],14
scrollToEnd(driver) 
time.sleep(3)
if isPageReady(driver,23):
    print(getName(getRow(driver)))
    getSpecLink(getRow(driver))
    


# TODO: Go into page


shutDown(driver)