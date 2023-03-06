from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, 'span#num1.nowrap').text
    x_element2 = browser.find_element(By.CSS_SELECTOR, 'span#num2.nowrap').text
    x = int(x_element1) + int(x_element2)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))  # ищем элемент с текстом "Python"


    button1 = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button1.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла