from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try:
	link = "http://suninjuly.github.io/get_attribute.html" 
	browser = webdriver.Chrome()
	browser.get(link)
	# Открыть ссылку в браузере
	
	xelement = browser.find_element(By.ID, "treasure")
	valuex = xelement.get_attribute("valuex")
	# Найти значение x
	
	xcalc = calc(valuex)
	fieldanswer = browser.find_element(By.ID, "answer")
	fieldanswer.send_keys(xcalc)
	# посчитать решение по формуле и ввести его в поле
	
	checkbot = browser.find_element(By.ID, "robotCheckbox")
	checkbot.click()
	# Поставить отметку в чекбоксе
	
	radiobot = browser.find_element(By.ID, "robotsRule")
	radiobot.click()
	# Поставить отметку в радиобаттоне
	
	but = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
	but.click()
	# Нажать на кнопку Submit
	

finally:
	time.sleep(10)
	browser.quit()
	
