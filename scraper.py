import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.jumia.com.ng/hp-250-g7-intel-core-i3-2.0ghz-8gb-ram1tb-hdd-wins-10.-46125209.html'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

def checkPrice():
    
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="-fs20 -pts -pbxs").get_text()
    price = soup.find(class_="-b -ltr -tal -fs24").get_text()
    converted_price = float(price[2:10].replace(',', ''))

    if converted_price > 200000:
        sendMail()
    print(converted_price)

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    Email = ''
    Password = ''
    server.login(Email, Password)

    subject = 'Price fell down'
    body = 'check the jumia link'

    msg =f"Subject:{subject}\n\n{body} https://www.jumia.com.ng/hp-250-g7-intel-core-i3-2.0ghz-8gb-ram1tb-hdd-wins-10.-46125209.html"

    server.sendmail(
        Email,
        Email,
        msg
    )

    print('Email sent successfully')
    server.quit()

checkPrice()