from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    sunduk_element = browser.find_element_by_css_selector("#treasure")
    sunduk_value = sunduk_element.get_attribute("valuex")
    y = calc(sunduk_value)

    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)
      
    checkbox_robot =  browser.find_element_by_css_selector("#robotCheckbox") 
    checkbox_robot.click()
    
    radio_robotsRule =  browser.find_element_by_css_selector("#robotsRule") 
    radio_robotsRule.click()
    
            
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла