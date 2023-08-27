import requests
from bs4 import BeautifulSoup
import smtplib


url="https://camelcamelcamel.com/product/B01NBKTPTS?context=search"
headers = {
    "Accept-Language":"bg-BG,bg;q=0.9,en;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "referer":"https://www.google.com/",
}
response = requests.get(url=url, headers=headers).text


soup = BeautifulSoup(response, "lxml")
a = soup.find(name="span", class_="green").getText()
price = float(a.split("$")[1])
print(price)
title = soup.find(name="a", style="overflow-wrap: break-word;").getText()
title_split = title.split(",")
title_name = title_split[0]


BUY_PRICE = 200

if price < BUY_PRICE:
    message = f"{title_name} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="EMAIL TO SEND",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
