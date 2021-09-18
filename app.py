from bs4 import BeautifulSoup
import time, requests


def getting_top_items():
    html_file = requests.get('https://www.flipkart.com').text
    soup = BeautifulSoup(html_file, 'lxml')
    links_obj = soup.find_all('a', class_='_6WQwDJ')
    prods_obj = soup.find_all('div', class_='_3LU4EM')
    timer_obj = soup.find('div', class_='EiX-pS')
    costs_obj = soup.find_all('div', class_='_2tDhp2')
    links = []
    products = []
    cost_details = []

    with open('topDeal.txt', 'w') as file_to_write:
        file_to_write.write(timer_obj.text+"\n")
        file_to_write.write("<----------------------------------->")
        file_to_write.close()
    for i in range(len(links_obj)):
        products.append(prods_obj[i].text)
        links.append(f"www.flipkart.com{links_obj[i]['href']}")
        cost_details.append(costs_obj[i].text)
        with open('DealOfTheDay/topDeal.txt', 'a') as file_to_write:
            file_to_write.write("\n"+products[i]+"\n")
            try:
                file_to_write.write(cost_details[i]+"\n")
            except UnicodeEncodeError:
                file_to_write.write("--Discount or cost data not available---\n")
            file_to_write.write(links[i]+"\n\n")
    t = time.localtime()
    print("---------------------------------------------------------------")
    print(f"updated at {time.strftime('%H:%M:%S', t)}.")
    print("---------------------------------------------------------------")
    print(f"{timer_obj.text} for these deals")


if __name__ == '__main__':
    while True:
        t = 1  # Change this value to the time interval for updating the Top Deals!
        getting_top_items()
        print(f"Next Update will be in {t} minutes...\n\n")
        # print("////  To stop this process enter 'ctrl+c' or 'cmd+c'")
        time.sleep(t*60)


