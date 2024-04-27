import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# driver.implicitly_wait(30)
#
# driver.get(r"C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\iframe.html")
# time.sleep(2)
#
# ## switcing to frame1
# driver.switch_to.frame('FR1')       ## id/name/xpath
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('python')
# time.sleep(1)
#
# ## switching back to parent frame
# driver.switch_to.parent_frame()
# time.sleep(1)
#
# ## switching to second frame
# driver.switch_to.frame('FR2')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="name"]').send_keys('Ram')

#-----------------------------------------------------------------------------------------

## EG2
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(20)
act_chain_obj = ActionChains(driver)

driver.get('https://www.linkedin.com/')
time.sleep(2)

element = driver.find_element('xpath', '//h2[contains(text(), "Explore collaborative articles")]')
act_chain_obj.scroll_to_element(element).perform()
time.sleep(2)

## switching to frame
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')
driver.switch_to.frame(google_frame)
time.sleep(2)

driver.find_element('xpath', '//span[text()="Continue with Google"]').click()

## switching back to parent frame
driver.switch_to.parent_frame()
time.sleep(2)

youtube_ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues, classmates, and friends on LinkedIn.")]')
act_chain_obj.scroll_to_element(youtube_ele).perform()
time.sleep(2)

youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
driver.switch_to.frame(youtube_frame)
time.sleep(1)

driver.find_element('xpath', '//button[@title="Play"]').click()

































































