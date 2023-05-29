from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


website = 'https://tracksino.com/crazytime'
path = '/Users/matteoforesti/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website) #here a Chrome window will be opened

plays = driver.find_elements(By.TAG_NAME, 'tr') #with this the code is going to get all the rows of the website, in the shape of a list


#here empty lists are created in order to store the different columns of the rows scraped before
date_time = []
slot_result = []
slot_multiplier = []
spin_result = []
multiplier = []
total_winners = []
total_payout = []

i = 0
print(plays)
while i in range(100):
    for play in plays[1:]:
        date_time.append(play.find_element(By.XPATH, './td[1]').text)
        slt_result = (play.find_element(By.XPATH, './td[2]/span/i')).get_attribute("class")
        slot_result.append(slt_result)
        slot_multiplier.append(play.find_element(By.XPATH, './td[2]/span').text)
        result = (play.find_element(By.XPATH, './td[3]/center/i')).get_attribute("class")
        spin_result.append(result)
        multiplier.append(play.find_element(By.XPATH, './td[4]/span').text)
        total_winners.append(play.find_element(By.XPATH, './td[5]').text)
        total_payout.append(play.find_element(By.XPATH, './td[6]').text)
    next_page_button = driver.find_element(By.XPATH, "//*[@aria-label='Go to next page']")
    driver.execute_script("arguments[0].click();", next_page_button)
    time.sleep(0.1)
    i += 1

driver.close()
#driver.quit() #this will close the driver once the scraping process is finished

#storing the data scraped into a df
df = pd.DataFrame({'date_time' : date_time, 'slot_result':slot_result, 'slot_multiplier':slot_multiplier, 'spin_result':spin_result, 'multiplier':multiplier,'total_winners' : total_winners, 'total_payout' : total_payout})
df.to_csv('log_eventi_tracksino2.csv') #index=False is for avoiding the automatic creation of the column of index
print(df)


