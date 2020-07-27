#A program which takes in the Terms & Conditions of sites and simplifies it for you so you can brush over all the important parts!
from selenium import webdriver
PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

web_url=input("enter the url of the website's privacy policy you want:")

driver.get(web_url)
body = driver.find_element_by_tag_name('body')
text = body.text

list_tostore = []
list_tostore = text.split(".")
#print(list_tostore)
for i in list_tostore:
    if "information" or "rights" or "delete" in i:
        print(i)
