import time
import json
from secret import siteUrl
from selenium import webdriver
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
    #driver = webdriver.Firefox(executable_path='/home/skaarface/Apps/WebDrivers/geckodriver')
    driver = webdriver.Firefox(options=headless(),executable_path='/home/skaarface/Apps/WebDrivers/geckodriver')
    driver.get(siteUrl+'phonefinder.php')
    return driver

def shutDown(driver):
    driver.close()

def scrollToEnd(driver):
    driver.execute_script("window.scrollTo(0,2500)")
    return

def nextListPage(driver):
    driver.find_element_by_xpath("//div[contains(@class, 'listing-btns4')]").click()


def isPageReady(driver,num):
    try:
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-row="{}"]'.format(num))))
        return True
    except TimeoutException:
        return True

def getRow(driver):
    return driver.find_element_by_xpath("//div[contains(@class, 'filter-grey-bar')]")

def getNames(driver):
    return driver.find_elements_by_xpath("//a[@class='hover_blue_link name gaclick']")

def getlinks(driver):
    fin,flag=[],0
    for i in driver.find_elements_by_xpath("//span[contains(@class,'blue target_link_new_tab gaclick')]"):
        if flag%2!=0:
            fin.append(i.get_attribute('data-href-url'))
        flag+=1
    return fin

def makeList(items,getNames,driver):
    temp=[name.text for name in getNames(driver)]
    return temp


driver=startDriver()
row_num=14
names,links=[],[]
try:
    while row_num<=1500:
        scrollToEnd(driver)
        if isPageReady(driver, row_num):
            time.sleep(2)
            names+=makeList(names, getNames, driver)
            links+=getlinks(driver)
            time.sleep(2)
            nextListPage(driver)
        row_num+=10    
        print("---"+str(row_num)+"---") 
except:
    print("Last page")
print("---DONE---")

spider = dict(zip(names, links))
#print(spider)
with open("outputs/step1.json","w") as op:
    json.dump(spider, op)
shutDown(driver)