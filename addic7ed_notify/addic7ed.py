import requests
from bs4 import BeautifulSoup
import time
import sys
import webbrowser

animation = "|/-\\"

def orderRequest():
    page = requests.get('http://www.addic7ed.com')

    soup = BeautifulSoup(page.text, 'html.parser')

    newReleases = soup.findAll('td', class_='versales')

    return newReleases

def getNewReleases(newReleases, busca):
    for i in range(9):
        if busca.lower() in newReleases[i].a.string.lower():
            #sys.stdout.write('\nhttp://www.addic7ed.com/' + newReleases[i].a['href'])
            url = 'http://www.addic7ed.com/' + newReleases[i].a['href']
            webbrowser.open(url)
            exit()

    for j in range(50):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[j % len(animation)])
        sys.stdout.flush()

    getNewReleases(orderRequest(), busca)

#===============================

busca = raw_input('Digite o termo a ser buscado: ')

getNewReleases(orderRequest(), busca)