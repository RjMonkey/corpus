import csv
import os
from bs4 import BeautifulSoup


def detect_if_label(label_list):
    copy_list = []
    for i in label_list:
        copy_list.append(int(i))
    copy_list.pop()
    # copy_list = label_list
    max_label = max(copy_list)
    copy_list.remove(max_label)
    
    sec_max_label = max(copy_list)
    if (max_label - sec_max_label) >= 2 or sec_max_label == 0:
        return True
    else:
        return False


def return_label(label_list):

    if detect_if_label(label_list):
        copy_list = []
        for i in label_list:
            copy_list.append(int(i))
        copy_list.pop()
        max_label = max(copy_list)
        if max_label == 0:
            return 9
        else:
            return copy_list.index(max_label)
    else:
        copy_list = []
        for i in label_list:
            copy_list.append(str(i))
        return ' '.join(copy_list)


def convert_to_int(label_str):
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

    with open('./annotation/'+policy_name) as csvfile:

        spamreader = list(csv.reader(csvfile))

        policy_id = policy_name.split('_')[0]

        for row in spamreader:
            segment_id = int(row[4])
            id = str(policy_id) + "_" + str(row[4])
            label_str = row[5]
            label = convert_to_int(label_str)

            result.append([id, label, segments[segment_id]])

final_result = []

label_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
last_policy_id = result[0][0]
last_segment = result[0][2]
for item in result:
    if str(item[0]) == str(last_policy_id):
        # label_list.append(str(item[1]))
        label_list[item[1]] += 1
    else:

        final_result.append([last_policy_id, return_label(label_list), last_segment])
        label_list.clear()
        label_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        last_policy_id = item[0]
        last_segment = item[2]

        label_list[item[1]] += 1


final_result.append([last_policy_id, return_label(label_list), last_segment])
error_list = []
for item in final_result:
    if type(item[1]) != int:
        error_list.append(item)
pass
with open('./result/result.tsv',  'w', newline='') as tsvfile:
    # fieldnames = ['id', 'sentiment', 'reviews']
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerows(final_result)

with open('./result/error.tsv',  'w', newline='') as tsvfile:
    # fieldnames = ['id', 'sentiment', 'reviews']
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerows(error_list)




