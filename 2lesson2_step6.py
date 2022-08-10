from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# Открыть ссылку в браузере
	
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	field = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", field)
	field.send_keys(y)
	# Посчитать значение и заполнить поле
	
	checker = browser.find_element(By.ID, "robotCheckbox")
	checker.click()
	# Найти и отметить чекбокс
	
	radiobut = browser.find_element(By.ID, "robotsRule")
	radiobut.click()
	# Найти и отметить радиобаттон
	
	but = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
	but.click()
	
finally:
	time.sleep(10)
	browser.quit()
	
