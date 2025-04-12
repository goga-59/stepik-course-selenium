from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    browser.switch_to.alert.accept()

    time.sleep(1)

    x = int(browser.find_element(By.ID, "input_value").text)
    y = math.log(abs(12 * math.sin(x)), math.e)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
