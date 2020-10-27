#############################################
#                                           #
#   ID_GROUP                   -112499374   #
#   start from                 1453075200   #
#   end from                   1603152000   #
#   id Zakha                   327099867    #
#############################################
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import requests
import datetime
from time import sleep
import webbrowser
import requests
from pymongo import MongoClient
import json
import time
import pymongo
import random

client=MongoClient('localhost', 27017)
db = client['test-database']
posts=db.Furry_University
db.Furry_University.create_index("id")
db.Furry_University.create_index("date")
db.Furry_University.create_index("signed_id")


def parsing():
    with open("config.txt","r",encoding="utf-8") as file:
        line=file.readline()
        Group_Key=line.split()[1]
        line=file.readline()
        ID_app=line.split()[1]
        line=file.readline()
        Secur_Key=line.split()[1]
        line=file.readline()
        Servise_Access_Key=line.split()[1]
        line=file.readline()
        AT=line.split()[1]
    offset=0;
    document=dict()
    list_of_posts=list()
    while offset<60000:
        response=requests.get("https://api.vk.com/method/wall.get?owner_id=-112499374&offset="+str(offset)+"&count=100&access_token="+AT+"&v=5.124")
        print(str(response.status_code)+" >> "+str(offset)+"\n"+"-------------\n")
        response=response.json()
        for key in response:
            if key=='response':
                response=response[key]
                for key in response:
                    if key=='items':
                        items=response[key]
        for i in items:
            for key in i:
                if key=="id":
                    document["id"]=i[key]
                if key=="date":
                    document["date"]=i[key]
                if key=="signer_id":
                    document["signer_id"]=i[key]
          #  if "signed_id" not in document:
          #      document["signed_id"]="None"
            list_of_posts.append(document)
            document=dict()
            a=len(list_of_posts)
            if len(list_of_posts)==1000:
                post_id=posts.insert_many(list_of_posts)
                list_of_posts.clear()
        offset+=100
        #time.sleep(5)
    if len(list_of_posts)!=0:
        post_id=posts.insert_many(list_of_posts)
        list_of_posts.clear


def search():
    id_list=list()
    id_stat=dict()
    result=posts.find({"date":1603531604})
    for i in result:
        print(i["date"])
    result=posts.find({"signer_id":{ "$exists": True}})
    for i in result:
        if id_list.count(i["signer_id"])==0:
            id_list.append(i["signer_id"])
    for i in id_list:
        result=posts.find({"signer_id":i}).count()
        print("The "+str(i)+" created "+str(result)+" posts\n")
    result=posts.find({"date":{ "$exists": True}})
    id_list=list()
    id_stat=dict()
    for i in result:
        if id_list.count(i["date"])==0:
            id_list.append(i["date"])
    id_list.sort()
    print(">>> "+str(id_list[0]))
    first_year=0
    second_year=0
    third_year=0
    four_year=0
    fife_year=0
    i=0
    for i in range(len(id_list)):
        if id_list[i]<=1483228800:
            first_year+=1
        if id_list[i]>1483228800 and id_list[i]<=1514764800:
            second_year+=1
        if id_list[i]>1514764800 and id_list[i]<=1546300800:
            third_year+=1
        if id_list[i]>1546300800 and id_list[i]<=1577836800:
            four_year+=1
        if id_list[i]>1577836800:
            fife_year+=1
    print("\nFirst_year >> "+str(first_year)+"\nSecond_year >> "+str(second_year)+"\nThird_year >> "+str(third_year)+"\nFour_year >> "+str(four_year)+"\nFife_year >> "+str(fife_year))



def Destroy_Zakha_Chat():
    driver = Chrome()
    string="https://vk.com/dev/messages.send?params[user_id]=327099867&params[random_id]="+str(random.randint(0,100000000))+"&params[peer_id]=327099867&params[message]=IvanUshka_Interneshanel_Ne_Boley&params[dont_parse_links]=0&params[disable_mentions]=0&params[intent]=default&params[v]=5.124"
    driver.get("https://vk.com/fox.ibks")   #захожу на свою страницу для авторизации в браузере, после мне станет доступно окно отправки тестовых сообщений 
    i=int(input(">>"))
    for z in range(1,50000):
        driver.get(string)
        content = driver.find_elements_by_class_name('dev_page_cont')
        content=content[0]
        flats=content.find_elements_by_class_name('dev_const_params')
        for i in flats:
            button=i.find_elements_by_class_name('flat_button')
            button=button[0]
            button.click()
        string="https://vk.com/dev/messages.send?params[user_id]=327099867&params[random_id]="+str(random.randint(0,100000000))+"&params[peer_id]=327099867&params[message]=IvanUshka_Interneshanel_Ne_Boley "+str(z)+"&params[dont_parse_links]=0&params[disable_mentions]=0&params[intent]=default&params[v]=5.124"
        #time.sleep()


i=input("Parsing - 1\nSearch - 2\n")
if i=="1":
    parsing()
if i=="2":
    search()
if i=="3":
    Destroy_Zakha_Chat()
