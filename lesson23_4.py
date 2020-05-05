from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмём на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # Перекидываемся на новую страницу
    # Решаем капчу
    x_element = browser.find_element_by_css_selector("#input_value")
    y = calc(x_element.text)
    
    input_answer = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла