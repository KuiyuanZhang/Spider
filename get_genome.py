#coding=utf-8
import requests
import os,sys
import re
from bs4 import BeautifulSoup
import lxml


def down_genome(name):
    can_not = []
    can = []
    txt = requests.get(url='https://www.ncbi.nlm.nih.gov/genome/?term='+name).text
    soup = BeautifulSoup(txt,'lxml')
    x = soup.find('div').find(class_="refgenome_sensor")
    if x is None:
        print(name+'can not be download!!!!!!!!')
        can_not.append(name)
        pass
    else:
        a_list = x.find_all('a')
        for i in a_list:
            if 'genome' in i:
                link = i.get('href')
                if link.endswith('gz'):
                    print (name+'--------'+link)
                    can.append(name)
                    cmd = 'wget '+link
                    os.system(cmd)

def main():
    flag = 0
    file = open(sys.argv[1],'r')
    for i in file:
        name = i.strip().replace(' ','+')
        flag += 1
        print ('正在下载第'+str(flag)+'个基因组~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        down_genome(name)
    file.close()
    print('已经下载的如下：')
    print(can)
    print('不能下载的如下：')
    print(can_not)



if __name__ == '__main__':
    main()
