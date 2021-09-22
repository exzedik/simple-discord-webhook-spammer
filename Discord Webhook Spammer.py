import requests
import time
import os
logo = " ____ ____ ____ ____ ____ ____ ____  \n||D |||S |||P |||A |||M |||E |||R ||\n||__|||__|||__|||__|||__|||__|||__||\n|/__\|/__\|/__\|/__\|/__\|/__\|/__\|\nMade by github.com/exzedik\n\n\n"
os.system('mode 37,17')
os.system('color 04')
os.system("title dSpammer by github.com/exzedik")
print(logo)
content = input("What do you want me to say? ")
username = input("What do you want my username to be?")
num = input("How many times should I send that? ")
delay = input("Delay? (s): ")
webhook = input("Webhook url: ")
data = {
	"content" : content,
   	"username" : username,
    "avatar_url" : "https://media.discordapp.net/attachments/808273939629473796/872240739067756544/blank.png"
	}
for x in range(int(num)):
    requests.post(webhook, json = data)
    print("[+1]")
    time.sleep(float(delay))
print('Job completed, exiting in 10 seconds')
time.sleep(10)
os.system('exit')