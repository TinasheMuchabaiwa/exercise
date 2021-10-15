
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options

PATH = "./chromedriver"

driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 10)

def barnesAndNoble():
    url = 'https://www.barnesandnoble.com/h/books/browse'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)
    driver.implicitly_wait(10)

    my_account = driver.find_element_by_xpath("//*[@id=\"rhf_header_element\"]/nav/div/div[2]/ul[2]/li[1]")
    signin = driver.find_element_by_xpath("//*[@id=\"rhf_header_element\"]/nav/div/div[2]/ul[2]/li[1]/div/dd/a[1]")
    action.move_to_element(my_account).move_to_element(signin).click().perform()
    time.sleep(5)


    driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[6]/div/iframe"))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"loginForgotPassword\"]"))).click()
    driver.switch_to_default_content()

    driver.switch_to_frame(5)
    mailField = driver.find_element_by_xpath("//*[@id=\"email\"]")
    time.sleep(5)
    mailField.send_keys("muchabaiwatinashe@gmail.com")

    submit = driver.find_element_by_xpath("//*[@id=\"resetPwSubmit\"]")
    submit.click()
    driver.switch_to_default_content()

    driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[8]/div/iframe"))
    confirmSubmit = driver.find_element_by_xpath("//*[@id=\"resetPwSubmit\"]")
    confirmSubmit.click()
    driver.switch_to_default_content()

barnesAndNoble()
