import requests
#using this we can access the page and we can pull out some usefull data from the site
from bs4 import  BeautifulSoup
import  smtplib # enabling sending email
import time

URL= 'https://www.amazon.in/dp/B073Q5R6VR/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=TQQ7R990AEATXPY67KN8&pf_rd_t=101&pf_rd_p=773f015c-0ea0-4aea-bca8-db7b2df05eff&pf_rd_i=21479552031'
#not every website work with web scraping some block it also

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

#gives us some information about browser
def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price= float((price[2:8]).replace(',',''))
    if(converted_price<65000):
        send_mail()
    print(converted_price)
    print(title.strip())

    if(converted_price<65000.0):
        send_email()



    #establish a connection between our connection and gmail connection
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()# its command sent by an email server to identify itself when connecting to another email
    server.starttls()
    server.ehlo()

    server.login('nezkumar98@gmail.com','fbjlgmqoxezyivqm')
    subject = 'price of mac just fell down'
    body = 'check the amazon price at link https://www.amazon.in/dp/B073Q5R6VR/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=TQQ7R990AEATXPY67KN8&pf_rd_t=101&pf_rd_p=773f015c-0ea0-4aea-bca8-db7b2df05eff&pf_rd_i=21479552031'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'nezkumar98@gmail.com',
        'shizzkumari007@gmail.com',
        msg

    )

    print("EMAIL HAS SENT")
    server.quit()

'''if __name__ == '__main__':
    while(True):
        check_price()
        time.sleep(60*60*24)'''




