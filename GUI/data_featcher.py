import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_stars_data(hackerrank_id):
    url = r"https://www.hackerrank.com/profile"+"//"+hackerrank_id
    agent = {"User-Agent":'Chrome/123.0.6312.86'}
    response = requests.get(url,headers=agent)

    if response.status_code == 200:
        user_data = {}
        main_html_parser = BeautifulSoup(response.text, 'html.parser')
        badges = main_html_parser.find_all(class_="hacker-badge")
        for i,badge_html in enumerate(badges):
            badge_html_parser = BeautifulSoup(str(badge_html), 'html.parser')
            badge_title = badge_html_parser.find(class_="badge-title").text
            stars = len(badge_html_parser.find_all(class_="star"))
            user_data[badge_title]=stars
        return user_data
    else:
        return 'Failed to retrieve the webpage'
    
def get_certificate_data(hackerrank_id):
    url = r"https://www.hackerrank.com/profile"+"//"+hackerrank_id
    agent = {"User-Agent":'Chrome/123.0.6312.86'}
    response = requests.get(url,headers=agent)
    if response.status_code == 200:
        certificate_titles = []
        main_html_parser = BeautifulSoup(response.text, 'html.parser')
        certificates = main_html_parser.find_all(class_="certificate_v3 certificate_v3-skill")
        for certificate in certificates:
            certificate_titles.append(certificate.find(class_ = "certificate_v3-heading").text)
    return certificate_titles


def get_users_data(path):
    id_data_excel = pd.read_excel(path)
    id_data_excel = pd.DataFrame(id_data_excel)
    fetch_data = {}
    badge_list = ["Problem Solving","CPP","C language","Python","Java","Ruby",
                  "Sql","Days of Code","Days of JS","Days of Statistics"]
    new_name = ["Roll_No","Admission_No","Name","Hackerrank_ID"]
    col_names = id_data_excel.columns
    changes = {}
    for i in range(4): changes[col_names[i]] = new_name[i]
    id_data_excel = id_data_excel.rename(columns=changes)
    for index in range(len(id_data_excel)):
        if type(id_data_excel["Hackerrank_ID"][index]) == float:
            print(id_data_excel["Hackerrank_ID"][index]+" ID is not avaliable")
            continue
        url = r"https://www.hackerrank.com/profile"+"//"+str(id_data_excel["Hackerrank_ID"][index])
        agent = {"User-Agent":'Chrome/123.0.6312.86'}
        response = requests.get(url,headers=agent)
        if response.status_code == 200:
            user_data = {}
            temp = {}
            main_html_parser = BeautifulSoup(response.text, 'html.parser')
            check = main_html_parser.find(class_="cdn-error-view")
            if check != None:
                print(id_data_excel["Name"][index]+" ID is incorrect")
                continue
            badges = main_html_parser.find_all(class_="hacker-badge")
            for i,badge_html in enumerate(badges):
                badge_html_parser = BeautifulSoup(str(badge_html), 'html.parser')
                badge_title = badge_html_parser.find(class_="badge-title").text
                stars = len(badge_html_parser.find_all(class_="star"))
                user_data[badge_title]=stars

            for name in badge_list:
                if name in user_data:
                    temp[name]=user_data[name]
                else: temp[name]=0
            fetch_data[id_data_excel["Name"][index]] = temp
        else:
            print('Failed to retrieve the webpage',id_data_excel["Name"][index])

    excel_data = {}
    for badge_name in badge_list:
        temp = {}
        for name in fetch_data:
            temp[name] = fetch_data[name][badge_name]
        excel_data[badge_name]=temp
    excel_data = pd.DataFrame(excel_data)
    print(excel_data.head())
    excel_data.to_csv("output.csv")
    



