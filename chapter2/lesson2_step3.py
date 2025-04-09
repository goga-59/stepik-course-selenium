from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "num1").text)
    y = int(browser.find_element(By.ID, "num2").text)

    summ = str(x+y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(summ)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
