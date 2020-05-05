from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1_element = browser.find_element_by_css_selector("#num1")
    num2_element = browser.find_element_by_css_selector("#num2")
    sum_nums = int(num1_element.text) + int(num2_element.text)

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(sum_nums)) # ищем элемент с текстом равным сумме    
            
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла