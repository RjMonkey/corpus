import csv
import os
from bs4 import BeautifulSoup




file_list = os.listdir("./annotation/")

for policy_name in file_list:

    html_name = policy_name.replace('.csv', '.html')
    soup = BeautifulSoup(open('./sanitized_policies/' + html_name), features="lxml")
    # print(soup.get_text())
    segments = soup.get_text()

    with open('./html/' + policy_name.replace('.csv', '.txt'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(segments)
        # for item in result:






