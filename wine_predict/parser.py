# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:02:51 2018

@author: alalwjrm
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wine_predict.settings")
import django
django.setup()
from parsed_data.models import WineData

def parse_wine(page,driver):    
    driver.get("https://www.winemag.com/?s=&drink_type=wine&wine_type=Red&page="+str(page)+"&sort_by=pub_date_web&sort_dir=desc")
    html=driver.page_source
    
    soup=BeautifulSoup(html,"html.parser")
    
    wine_title=[]
    wine_rating=[]
    wine_region=[]
    wine_price=[]
    
    for title in soup.select("a.review-listing > div.title"):
        wine_title.append(title.text)
    for rating in soup.select("a.review-listing > div > span.rating"):
        wine_rating.append(rating.text[:3].strip())
    for region in soup.select("a.review-listing > div > span.appellation"):
        wine_region.append(region.text)
    for price in soup.select("a.review-listing > div > span.price"):
        wine_price.append(price.text[1:])
        
    result=[]
    for i in range(len(wine_title)):#튜플로 묶어서 리턴
        result.append((wine_title[i],wine_rating[i],wine_region[i],wine_price[i]))
    return result
        
def parse_all_page(driver):
    driver.get("https://www.winemag.com/?s=&drink_type=wine&wine_type=Red&page=1&sort_by=pub_date_web&sort_dir=desc")
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    
    result=soup.select("span.results-count")[0].text#전체 리뷰 개수 가져오기
    result=result.replace(',','')
    result=result.replace(')','')
    index=result.find("of")
    result=int(result[index+2:].strip())
    
    if result % 30==0:#전체 페이지수 계산 
        return int(result/30)
    else:
        return int(result/30)+1

if __name__=="__main__":
    driver=webdriver.PhantomJS("./phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    driver.implicitly_wait(3)
        
    all_page=parse_all_page(driver)
    
    for page in range(99,all_page): 
        temp=parse_wine(page,driver)
        print("Page "+str(page)+" of "+str(all_page)+"......")
        for data in temp:
            _name,_rating,_region,_price=data
            if _price.count('.'):
                str(round(float(_price)))
            try:            
                if ord(_price[0])>=48 and ord(_price[0])<=57:#가격중 "N/A"항목 제외
                    WineData(name=_name,rating=_rating,region=_region,price=_price).save()
            except:
                pass
            
                
        