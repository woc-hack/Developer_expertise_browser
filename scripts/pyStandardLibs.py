import os
from bs4 import BeautifulSoup
dir = './Python_Module_Index/'
standard_libs = set()
for file in os.listdir(dir):
    if file == '.DS_Store':
        continue
    print(dir+file)
    soup = BeautifulSoup(open(dir+file), features='html.parser')
    for code in soup.find_all('code'):
        module_name = code.string.split('.')[0]
        standard_libs.add(module_name)
print(list(standard_libs))