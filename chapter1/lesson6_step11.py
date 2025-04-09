from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = " http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поле First name
    first_name = browser.find_element(By.XPATH, "//div[@class='first_block']/div[1]/input")
    first_name.send_keys("Ivan")

    # Заполняем поле Last name
    last_name = browser.find_element(By.XPATH, "//div[@class='first_block']/div[2]/input")
    last_name.send_keys("Ivanov")

    # Заполняем поле Email
    email = browser.find_element(By.XPATH, "//div[@class='first_block']/div[3]/input")
    email.send_keys("Ivanov@ivan.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
