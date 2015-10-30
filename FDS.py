from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import mechanize

# Set up browser
driver = webdriver.Firefox() # Selenium

# Go to login page
BASE_URL = 'https://www.fanduel.com/p/login#login'
BASE_URL_USER = "https://www.fanduel.com/users/"
driver.get(BASE_URL)

# Find email and password input
emailInput = driver.find_element_by_name('email') 
passwordInput = driver.find_element_by_name('password')

#log in
emailInput.send_keys('cdibilio@princeton.edu')
passwordInput.send_keys('blUE32EAglE$'+ Keys.RETURN)

# Go to head to head tab
H2H = driver.find_element_by_partial_link_text('Head to Heads')
H2H.click()

# Iterate through profiles and get data
# Scroll Down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 

users = {'Users':0}
count = 1
br = mechanize.Browser()
br.set_handle_robots(False)

# Pause for page to load
driver.implicitly_wait(10)
allcontests = driver.find_elements_by_class_name("contest-name-text")

# for each element in array allcontests (results)
for contest in allcontests:
    a = driver.execute_script("window.innerHeight + window.scrollY")
    b = driver.execute_script("document.body.offsetHeight")
    if  a >= b:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    cont = contest.text
    user = cont[8:]
    link = BASE_URL_USER + user
    soup = BeautifulSoup(br.open(link).read())
    # On profile page / Get Data
    table = soup.find("table")
    rows = table.find_all('tr')
    cols = rows[1].find_all('td')
    valneeded = str(cols[0])
    valtot = int(valneeded[30:-5])
    users[user] = valtot
    

users.sort()
print users
'''
#driver.quit()