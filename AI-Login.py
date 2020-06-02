# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from secrets import username, password

# Finds the driver location
driver = webdriver.Chrome(r"C:\Users\garre\PycharmProject\AI-Login\chromedriver.exe")
# Goes to website URL
driver.get("https://id4.ximble.com/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dspa%26redirect_uri%3Dhttps%253A%252F%252Fapp.ximble.com%252Fauth-callback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520ximbleapi%26state%3D4d7a17ff80d7490e8375eebecc072a8e%26code_challenge%3DtdwfZOTkXDjqwS-wCQsKO-Z7mN2XHMQZs0Nk3kusTL4%26code_challenge_method%3DS256")
# Times out after 15sec
driver.set_page_load_timeout(15)
# Enters username in to Username box
driver.find_elements_by_name("Username")[0].send_keys(username)
# Enters password in to Password box
driver.find_elements_by_name("Password")[0].send_keys(password)
# Presses Enter in to Password box
driver.find_elements_by_name("Password")[0].send_keys(Keys.ENTER)
# Waits for page to load
time.sleep(4)
# Clicks clock in button
btn = driver.find_element_by_xpath('//*[@id="page-holder"]/section/div/div[1]/div[1]/div/div/div[2]/div/button')
btn.click()

time.sleep(3)
# Ends Program
driver.quit()
