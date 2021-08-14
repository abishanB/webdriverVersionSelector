from selenium import webdriver
import time
import os
PATH = os.getcwd()
drivers=[]
for file in os.listdir():
    if file.endswith(".exe"):
        drivers.append(file)    

def run():
    for driverVersion in drivers:
        try:
            driver = webdriver.Chrome(PATH + "\\" + driverVersion)
            time.sleep(0.75)
            print("\nPlease use " + driverVersion)
            print("Your chrome version is: " + driver.capabilities["browserVersion"])
            driver.quit()
            return True
        except:
            pass
    return False

if not run():
    print("Could not find chrome version")

input("")