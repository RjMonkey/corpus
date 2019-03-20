# import csv
# import os
# from bs4 import BeautifulSoup
#
#
#
# file_list = os.listdir("./document/")
# result = []
# j = 0
# for policy_name in file_list:
#
#     f = open('./document/'+policy_name, 'r', encoding='utf-8')
#     document = f.read()
#     segments = document.split('|||')
#
#     for i in segments:
#         i = i.strip().encode("GBK","ignore")
#         result.append([j, 1, i])
#     f.close()
#
# with open('./result/result_3.tsv',  'w', newline='') as tsvfile:
#     # fieldnames = ['id', 'sentiment', 'reviews']
#     writer = csv.writer(tsvfile, delimiter='\t')
#     writer.writerows(result)
#     # for item in result:
#
#
#
#
#
#
def l(b):
    b.remove(2)


a = [1,2,3]
l(a)
print(a)

# b = ''.join(a)
