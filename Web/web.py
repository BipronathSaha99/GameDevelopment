import requests

import bs4

# Take url link from user and getting scraped html data from website url 
url=input("enter website url: ")
# The get() method sends a GET request to the specified url.
response=requests.get(url)
file_name="main.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")
#The prettify() method formatted html code and display as human readable code.
formate_text=bs.prettify()
print(formate_text)

#using file handling to get the html codes in a different html file 
with open(file_name,"w+") as file:
    file.write(formate_text)

#find it if website has backgroung images
list_imgs=bs.find_all('img')
number_imgs=len(list_imgs)
print("Number of background images:",number_imgs)


#find it if website has anchor text
list_as=bs.find_all('a')
number_as=len(list_as)
print("Number of anchors:",number_as)
