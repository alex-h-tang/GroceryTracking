import bs4
from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import csv
import datetime
import shutil
import os
import time
import threading

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# headers = ["Date", "Product Price", "Average Price", "Price Checked"]

def getURLs():
    myURLs = [
        # 'https://www.lidl.com/products/1068506',
        'https://www.heb.com/product-detail/h-e-b-select-ingredients-fat-free-milk-1-gal/314132',
    ]
    # #Get all URLs from URLs.txt located in the same folder as the script
    # with open('URLs.txt', 'r') as f:
    #     myURLs = [line.rstrip() for line in f.readlines()]
    return myURLs

#loop through all URLs provided
def update_prices(myURLs):
    filenames = []
    for URL in myURLs:
        # uClient = uReq(URL)
        # page_html = uClient.read()
        # uClient.close()
        response  = requests.get(URL, headers=HEADERS)
        page_html = response.content
        print(response.text)
        #html parsing
        page_soup = soup(page_html, "html.parser")

        #Get product name
        # product_name = page_soup.h1.text
        
        #Get product price
        product_price = page_soup.find("meta",{"itemprop":"price"})
        product_price = ["content"]

    #     #Get current date
    #     x = datetime.datetime.now()
    #     date = x.strftime("%x")

    #     average_price = float(product_price)
    #     price_checked_count = 1

    #     newrow = [date,product_price,average_price,price_checked_count]
        
    #     filename = product_name.replace(" ", "_") + ".csv"
        
    #     if filename not in filenames:
    #         filenames.append(filename)
            
    #     #Try opening file if they exist to add new data and create a new file if it doesn't exist
    #     try:
    #         with open(filename, 'r', newline='') as f, open(filename + '.temp', 'w', newline='') as fout:
    #             reader = csv.reader(f)
    #             writer = csv.writer(fout)
    #             lastrow = []
    #             checked = False
                
    #             for row in reader:
    #                 if date in row[0]:
    #                     checked = True
    #                     break
    #                 elif lastrow == headers:
    #                     price_checked_count = int(row[3])
    #                     average_price = ((float(row[2])*price_checked_count)+float(product_price))/(price_checked_count+1)
    #                     price_checked_count = price_checked_count+1
    #                     newrow = [date,product_price,average_price,price_checked_count]
    #                     writer.writerow(newrow)
    #                 writer.writerow(row)
    #                 lastrow = row
    #             if checked == True:
    #                 os.remove(filename + '.temp')
    #                 break
    #             else:
    #                 shutil.move(filename + '.temp', filename) 
    #     except FileNotFoundError:
    #         with open(filename, 'w') as csvfile:
    #             filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #             filewriter.writerow(headers)
    #             filewriter.writerow(newrow)
    # print(filenames)
    threading.Timer(86400, update_prices).start()

if __name__ == '__main__':                
    update_prices(getURLs())



