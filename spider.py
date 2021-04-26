import json
import time
from secret import siteUrl
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def openFile(file_name):
    with open(file_name) as ip:
        stark= json.load(ip)
    return stark

def headless():
    options = Options()
    options.headless = True
    return options

def startDriver(link):
    #driver = webdriver.Firefox(executable_path='/home/skaarface/Apps/WebDrivers/geckodriver')
    driver = webdriver.Firefox(options=headless(),executable_path='/home/skaarface/Apps/WebDrivers/geckodriver')
    driver.get(siteUrl+link)
    return driver

def collectLabels(driver):
    return driver.find_elements_by_xpath("//td[contains(@class,'spec_ttle')]")

def collectValues(driver):
    return driver.find_elements_by_xpath("//td[contains(@class,'spec_des')]")

info=openFile("outputs/step1.json")
fin=[]
done=0
for i in info:
    mini_driver=startDriver(info[i])
    dic={}
    dic["Name"]=mini_driver.find_element_by_xpath("//h1[contains(@class,'h1_pro_head')]").text
    for label,values in zip(collectLabels(mini_driver),collectValues(mini_driver)):
        dic[label.text]=values.text
    fin.append(dic)
    done+=1
    print(done)
    mini_driver.close()
    #mini_driver.close()

with open("outputs/step2.json","w") as op:
    json.dump(fin, op)

