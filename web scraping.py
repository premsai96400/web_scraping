from bs4 import BeautifulSoup as bs
from selenium import webdriver
from twilio.rest import Client
import time
account_sid = "AC750e575cdbd1d6d1e73746d04f6be5e5" # enter the ssid of twilio account
auth_token = "ad557c0881a8b1b4a393417e93b1d18d"  #enter the auth token of your twilio account
path='C:\\Users\\Hi\\AppData\\Local\\Programs\\Python\\chromedriver' # enter the location of your chrome web driver
driver=webdriver.Chrome(path)
driver.get('https://www.covid19india.org/')
time.sleep(100)
page = driver.page_source
driver.quit()
soup = bs(page, 'html.parser')
res=soup.find_all('div',{'class':'level-item is-confirmed'})
sai=res[0].find_all('h1')
a = sai[0].get_text()
b = 'corona cases in india are '+ a
client = Client(account_sid, auth_token)
message = client.messages.create( from_='+12013501575',body =b,to ='+91 9676192575')
