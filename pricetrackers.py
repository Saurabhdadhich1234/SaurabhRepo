import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL='https://www.amazon.in/dp/B00HK8QV44/ref=cm_sw_r_apa_i_yGtQEb30RJAR4'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
def check_price():
    page=requests.get(URL, headers=headers)
    soup=BeautifulSoup(page.content,'html-parser')
    
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[0:5])
    
    if(converted_price>1.700):
        send_mail()
    print(converted_price)    
    print(title.strip())

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('example@gmail.com','****your_password****')
    subject="Price fell down"
    body='Check the amazon link  https://www.amazon.in/dp/B00HK8QV44/ref=cm_sw_r_apa_i_yGtQEb30RJAR4'
    
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail('example8@gmail.com','example@gmail.com',msg)
    print("Email has been sent")
    server.quit()
while(True):
    check_price()
    time.sleep(60*60)
