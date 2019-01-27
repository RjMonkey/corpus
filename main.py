import csv
import os
from bs4 import BeautifulSoup

def convertToInt(label_str):
    label = 0
    if label_str == "First Party Collection/Use":
        label = 0
    if label_str == "Third Party Sharing/Collection":
        label = 1
    if label_str == "User Choice/Control":
        label = 2
    if label_str == "User Access, Edit, & Deletion":
        label = 3
    if label_str == "Data Retention":
        label = 4
    if label_str == "Data Security":
        label = 5
    if label_str == "Policy Change":
        label = 6
    if label_str == "Do Not Track":
        label = 7
    if label_str == "International & Specific Audiences":
        label = 8
    if label_str == "Other":
        label = 9
    return label


file_list = os.listdir("./annotation/")
result = []
for policy_name in file_list:

    html_name = policy_name.replace('.csv', '.html')
    soup = BeautifulSoup(open('./sanitized_policies/' + html_name), features="lxml")
    # print(soup.get_text())
    segments = soup.get_text().split('|||')
    i = 0
    with open('./annotation/'+policy_name) as csvfile:
        spamreader = list(csv.reader(csvfile))
        for row in spamreader:
            id = str(row[3]) + "_" + str(row[4]) + "_" + str(i)
            label_str = row[5]
            label = convertToInt(label_str)
                # print(label)
                # if int(row[4]) == i:
                    # print("jsd")
                    # print(label)
                    # label_result[label] = "1"

            # label_result = ''.join(label_result)

            result.append([id, label, segments[int(row[4])]])
            i = i + 1

with open('./result/result_3.tsv',  'w', newline='') as tsvfile:
    # fieldnames = ['id', 'sentiment', 'reviews']
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerows(result)
    # for item in result:






