   import requests
from selenium import webdriver
import time
import os

path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
brower=webdriver.PhantomJS(path)

brower.get('http://www.126.bz/')
time.sleep(3)

data=brower.find_elements_by_class_name('article-item')
jieguo=[]
for ii in data:
    mm=ii.find_element_by_tag_name('a').get_attribute('href')
    jieguo.append(mm)

# print(jieguo[1])


for url1 in jieguo:
    # url1=i.find_element_by_tag_name('a').get_attribute('href')
    #取得每个链接的网址
    #print(url1)
    brower.get(url1)
    time.sleep(2)
    data1 = brower.find_element_by_id('productdata').find_elements_by_tag_name('img')
    dirname = brower.find_element_by_tag_name('h2').text
    # print(dirname)
    print('开始下载'+dirname+'...')
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    for j in data1:
        # print(j.get_attribute('src'))
        dizhi = j.get_attribute('src')
        filename = dizhi.split('/')[-1]
        with open(dirname + '/' + filename, 'wb')as f:
            f.write(requests.get(dizhi).content)

    page = brower.find_element_by_class_name('pagination').find_elements_by_tag_name('li')[-2].text
    #print(page)

    a=url1.find('.')
    b=url1[a+1:].find('.')
    c=url1[a+1+b+1:].find('.')
    new_url=url1[:a+1+b+1+c]+'-page-'
    #print(new_url)
    for s in range(2, int(page)):
        url = new_url + str(s) + '.html'
        # print(url)
        brower.get(url)
        time.sleep(2)
        data2 = brower.find_element_by_id('productdata').find_elements_by_tag_name('img')
        for m in data2:
            # print(m.get_attribute('src'))
            dizhi = m.get_attribute('src')
            filename = dizhi.split('/')[-1]
            with open(dirname + '/' + filename, 'wb')as f:
                f.write(requests.get(dizhi).content)

    print(dirname+'下载完毕')







# a=data.find('\n')
# b=data[a+1:].find('\n')
# new_data=data[a+1:a+1+b]
brower.close()