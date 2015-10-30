from bs4 import BeautifulSoup
import urllib2
import mechanize
import cookielib
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys 



BASE_URL = "https://www.fanduel.com/games"
BASE_URL_USER = "https://www.fanduel.com/users/"
#cj = cookielib.CookieJar()
#br = mechanize.Browser()
#br.set_handle_robots(False)
#br.set_cookiejar(cj)
#br.open(BASE_URL)
#br.select_form(nr=0)
#br.form['email'] = 'gsgosse01@gmail.com'
#br.form['password'] = 'allstar8'
#br.submit()

driver = webdriver.Firefox()
driver.get(BASE_URL)
elem = driver.find_element_by_name('email')
elem.send_keys("gsgosse01@gmail.com")
elem2 = driver.find_element_by_name('password')
elem2.send_keys("allstar8")
clickbut = driver.find_element_by_name('login')
clickbut.click()

click2 = driver.find_element_by_partial_link_text('Head to Heads')
click2.click()


#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

for i in xrange(0, 100):
    driver.execute_script("window.scrollTo(0, window.scrollMaxY);")


users = {'Users':0}
count = 1
br = mechanize.Browser()
br.set_handle_robots(False)

allcontests = driver.find_elements_by_class_name("contest-name-text")
for contest in allcontests:
    cont = contest.text
    user = cont[8:]
    link = BASE_URL_USER + user
    soup = BeautifulSoup(br.open(link).read())
    #print soup
    table = soup.find("table")
    rows = table.find_all('tr')
    #print rows
    cols = rows[1].find_all('td')
    valneeded = str(cols[0])
    #nfl = str(cols[1])
    #print valneeded
    valtot = int(valneeded[30:-5])
    users[user] = valtot
    #print columns[0].string
    
print users
    
    
    
    #= driver.find_element_by_class_name("contest-name-text").text

#print contests

#contests = driver.find_element_by_name(

#soup = BeautifulSoup(, 'html.parser')

#print soup
#print soup
#print soup.find_all(id = '')
#mycontests = soup.findAll("loading")
#print mycontests


    