from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

cur_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "file.txt")
print(cur_file)

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Ivan")
    browser.find_element(By.NAME, "email").send_keys("Ivan")
    browser.find_element(By.ID, "file").send_keys(cur_file)

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
