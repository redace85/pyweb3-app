from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

PROXY = "127.0.0.1:7890"
webdriver.DesiredCapabilities.CHROME['proxy'] = {
"httpProxy": PROXY,
"ftpProxy": PROXY,
"sslProxy": PROXY,
"proxyType": "MANUAL",
}

options = Options()
#options.page_load_strategy = 'eager'
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get('https://www2.javhdporn.net/video/mkmp-130/')

original_window = driver.current_window_handle

# click the play button this page will jump to ad page
playbtn = driver.find_element(By.CLASS_NAME, 'play-button')
playbtn.click()

# close the original-window and switch to new window
for window_handle in driver.window_handles:
    if window_handle == original_window:
        driver.close()
    else:
        driver.switch_to.window(window_handle)

#time.sleep(5)
# click play button again
#playbtn = driver.find_element(By.CLASS_NAME, 'play-button')
#playbtn.click()

# find the blob from playeriframe
#playeriframe = driver.find_element(By.ID, 'playeriframe')
#print(playeriframe.get_dom_attribute('src'))
#print(playeriframe.get_property('src'))

with open('source_page.html','w') as f:
    f.write(driver.page_source)

print('done')
