from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.select import Select

try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# Открыть ссылку в браузере
	
	num1 = int(browser.find_element(By.ID, "num1").text)
	num2 = int(browser.find_element(By.ID, "num2").text)
	# найти на странице числа
	
	sum = str(num1+num2)
	# Вычислить сумму чисел и перевести ее в строку
	
	dropdown = Select(browser.find_element(By.ID, "dropdown"))
	dropdown.select_by_value(sum)
	# Найти на странице селект и выбрать на нем пункт, равный сумме чисел
	
	btn = browser.find_element(By.CSS_SELECTOR, ".btn-default")
	btn.click()
	
finally:
	time.sleep(10)
	browser.quit()
		
