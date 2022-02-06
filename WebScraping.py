# Spring 2022 HackSC Project!

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import warnings
from selenium.webdriver.common.by import By
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)
url = "https://www.pb-resources.com/bhm.html"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome('/Users/aditi/Downloads/chromedriver', chrome_options=chrome_options)
driver.get(url)
html = driver.page_source
soup = bs(html, "html.parser")
nameDiv = soup.select_one("html body div#insides div div p#name")
secretName = nameDiv.get_text()
button = driver.find_element(By.XPATH, "/html/body/div/div[5]/div/div[1]/button")
driver.execute_script("arguments[0].click();", button)
descDiv = soup.select_one("html body div#insides div div div#blurbContainer p#text")
desc = "A" + descDiv.get_text()
desc = desc.split(".")
driver.close()

secretWord = list(secretName)
spaceIdx = 0
printString = ""
score = 100
flag = 0

# Instructions
print("\nWelcome to Black History Month Wordle!")
print("-" * 15)
time.sleep(2)
print("In this Wordle-like game you will have to guess the Black historical figure")
print("Upon correct guessing, you'll be rewarded with more information about the historical figure")
print("-" * 15)
time.sleep(4)
print("If you guess a letter correctly, it will appear.\nIf you guess the correct letter in the wrong spot, it'll be presented as a '~'")
print("-" * 15)
time.sleep(3)
print("You will start off with 100 points")
print("During each turn you will be prompted to guess or have a letter revealed to you")
print("Each turn will deduct 10 points from your total score")
print("Guess the Black historical figure before you're out of turns!")
print("Good luck!"'')
print("-" * 15)
time.sleep(6)
print("Credit for all historical figure names and information goes to Alexis Williams, the creator of pb-resources.com")

# Initializing guess output
for num in range(0, len(secretWord)):
    if secretWord[num] == " ":
        printString += " "
        spaceIdx = num
    else:
        printString += "*"
printStringList = list(printString)

while score > 0 and printStringList != secretWord:

    if flag == 0:
        guess = printStringList
        flag = 1
        type = "guess"
    else:
        print('\n'"Will you be entering a guess or need to reveal a letter?")
        type = input("Type: 'guess' or 'letter' exactly as shown: "'\n')
        while type != "guess" and type != "letter":
            print("ERROR: Print either 'guess' or 'letter'")
            type = input("Type: 'guess' or 'letter' exactly as shown: "'\n')

    while len(guess) != len(secretWord) or guess[spaceIdx] != " ":
        print('\n'"ERROR: Your guess must match the format below:")
        guess = input("Enter a guess:\n" + printString + '\n')

    # if they select the letter option
    if type == "letter":
        score = score - 15
        for char in range(0, len(secretWord)):
            if printStringList[char] != secretWord[char]:
                printStringList[char] = secretWord[char]
                break

    # If they type guess
    if type == "guess":
        guess = input('\n'"Enter a guess:\n" + printString + '\n')
        score = score - 10
        for char in range(0, len(guess)):
            if guess[char].lower() == secretWord[char].lower():
                printStringList[char] = secretWord[char]
        for char1 in range(0, len(guess)):
            if (guess[char1] in secretWord) and (guess[char1] not in printStringList):
                printStringList[char1] = "~"

    if printStringList == secretWord:
        if score <= 0:
            print("You lost, the correct word is: ")
        printString = "".join(printStringList)
        print(printString)
        print('\n'"Congrats! You guessed the correct historical figure with", score, "points left"'\n')
        print(printString)
        print("-"*15)
        desc = "\n ".join(desc)
        print(desc)
        print("Read about", printString, "and more at pb-resources.com!")
        break

    printString = "".join(printStringList)
    print(printString)
if printStringList != secretWord:
    print('\n'"You lost, the correct historical figure is: ", "".join(secretWord))
