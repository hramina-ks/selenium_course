import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.mark.parametrize('number', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_nlo_is_here(browser, number):
	link = f"https://stepik.org/lesson/{number}/step/1"
	browser.get(link)
	answer = str(math.log(int(time.time())))
	textarea = browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea")
	button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
	textarea.send_keys(answer)
	button.click()
	res = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
	res_text = res.text
	assert res_text == "Correct!", f"Неверно! Ожидаю 'Correct!', получаю {res_text}."

