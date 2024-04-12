import requests
import os
from bs4 import BeautifulSoup



url = r"https://www.hackerrank.com/profile/CSEB_21B0101054"
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
    print(user_data)
else:
    print('Failed to retrieve the webpage')



