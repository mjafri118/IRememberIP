from urllib import urlopen as uReq 
from bs4 import BeautifulSoup as soup 
import datetime, requests
import subprocess

#url = "https://tianchi.aliyun.com/competition/information.htm?raceId=231692"

def getIP():
    command = "ifconfig wlan0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"
    ip = subprocess.check_output(command, shell=True)
    return ip

def date():
    stamp = datetime.datetime.now().strftime("%m/%d/%y %H:%M")
    return stamp

def submitForm():
    with open("url.txt","r") as f:
	id = f.readline().strip("\r").strip("\n")
    formUrl = "https://docs.google.com/forms/d/" + id + "/formResponse"
    data = {
        "usp": "pp_url",
        "entry.1516534648": "Raspberry Pi 3+B",
        "entry.1790167271": getIP(),
	"entry.1363235023": date()
    }
    r = requests.post(url=formUrl, data=data)

submitForm()
