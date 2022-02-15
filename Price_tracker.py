import requests
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.amazon.in/New-Apple-iPhone-XR-64GB/dp/B08L8DCR87/ref=sr_1_1_sspa?keywords=iphone+xr&qid=1640702597&sprefix=iph%2Caps%2C260&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNE5XRzdLQkJNM0EzJmVuY3J5cHRlZElkPUEwNDcyNjg1MTFIMzMySDVLSjUzMiZlbmNyeXB0ZWRBZElkPUEwNDc4NjI1MkFEWUNWM1dNQU1MNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")


def check():
    title = soup.find(id="productTitle").getText()
    price = soup.find(class_="a-offscreen").getText()
    price = price.replace(",", "")
    conv_price = float(price[1:6])

    print(title)
    print(conv_price)

    if conv_price < 40000:
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("diganta.19032001@gmail.com", "D2@diganta1903")

    subject = "Price just fell down!"
    body = "Check the amazon link https://www.amazon.in/New-Apple-iPhone-XR-64GB/dp/B08L8DCR87/ref=sr_1_1_sspa?keywords=iphone+xr&qid=1640702597&sprefix=iph%2Caps%2C260&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNE5XRzdLQkJNM0EzJmVuY3J5cHRlZElkPUEwNDcyNjg1MTFIMzMySDVLSjUzMiZlbmNyeXB0ZWRBZElkPUEwNDc4NjI1MkFEWUNWM1dNQU1MNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

    msg = f"Subject {subject}\n\n{body}"

    server.sendmail(
        "diganta.19032001@gmail.com", "diganta.nayak.ece23@heritageit.edu.in", msg
    )
    print("EMAIL SENT")

    server.quit()


check()
