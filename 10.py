from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input1.send_keys(y)

    button1 = browser.find_element(By.XPATH, '//label[text()="Robots rule"]')
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox.form-check-input')
    button2.click()
    button3 = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button3.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


#browser.execute_script("window.scrollBy(0, 100);") 100 пикселей вниз
# // javascript
#button = document.getElementsByTagName("button")[0]; функци в самый низ документа
#button.scrollIntoView(true);

