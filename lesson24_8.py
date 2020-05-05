from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button_book = browser.find_element_by_id("book")

    # Ждём цену = 100
    #price = wait.until(browser.find_element_by_id("price").text,"$100")
    wait = WebDriverWait(browser,12)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'),"$100"))
     
    # Жмём на кнопку book
    button_book.click()
    
    # Решаем капчу
    x_element = browser.find_element_by_css_selector("#input_value")
    y = calc(x_element.text)
    
    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла