from selenium import webdriver
import requests
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="/home/jyotichauhan/Downloads/chromedriver_linux64/chromedriver")
browser.get("https://flipkart.com")

username=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
username.send_keys("9492116836")
password=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
password.send_keys("kumar5678")
login=browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button")
login.send_keys(Keys.ENTER)
searchbox=browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
searchbox.send_keys("oppo")
submit=browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
submit.send_keys(Keys.ENTER)
j=1
while j<=2:
    browser.get("https://www.flipkart.com/search?q=realme&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(j))
    soup=BeautifulSoup(browser.page_source,"html.parser")

    main_div=soup.findAll("div",class_="_2kHMtA")
    List_for_Flipkart_Detail=[]
    for i in main_div:
        Dict_for_Flipkart_Deatil={}
        for_name=i.find("div",class_="_4rR01T")
        Dict_for_Flipkart_Deatil['Name']=for_name.text
        allData=i.findAll("li",class_="rgWa7D")
        for k in allData:
            if "RAM"  in k.text:
                Dict_for_Flipkart_Deatil['RAM']=k.text
            elif "Display" in k.text:
                Dict_for_Flipkart_Deatil['Display']=k.text
            elif "Camera" in k.text:
                Dict_for_Flipkart_Deatil['Camera']=k.text
            elif "Battery" in k.text:
               Dict_for_Flipkart_Deatil['Battery']=k.text
            elif "Processer" in k.text:
                Dict_for_Flipkart_Deatil['Processer'] in k.text
            
        List_for_Flipkart_Detail.append(Dict_for_Flipkart_Deatil)
    j=j+1
with open("DetailsOfPhones.json","w") as f:
    json.dump( List_for_Flipkart_Detail,f,indent=4)
