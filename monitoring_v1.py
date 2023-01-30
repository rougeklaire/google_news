from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *


root = Tk()
root.title("Google News Searcher")
root.geometry("300x300")

search_list = ["battery passport", "battery pass", "battery regulation", "battery recycling", 
"battery reuse", "battery remanufacturing", "battery repairability", "resource efficiency", 
"battery performance", "circular design", "circular battery design", "battery design", 
"sustainable battery", "battery durability", "EV batteries", "resource availability", 
"battery raw material", "mobility scenario", "e-mobility", "cell manufacturing", "Li-ion battery", 
"battery maufacturing", "battery production", "product passport", "battery composition", 
"cobalt mining", "lithium mining", "giga factory", "circular economy"]

def search():
    driver = webdriver.Firefox() #!!geckodriver has to be in the same directory as the script!!
    for i in search_list:
        search_string = f"https://news.google.com/search?q={i}%20when%3A7d&hl=de&gl=DE&ceid=DE%3Ade"
        driver.get(search_string)
        driver.execute_script(f"window.open('{search_string}');")
        try:
            driver.find_element(By.CLASS_NAME, "lssxud").click()
        except:
            pass

search_button = Button(root, text = "Search Google News", command = search)
search_button.pack()

root.mainloop()