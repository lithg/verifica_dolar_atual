from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import telepot
import time
import schedule

def verificaDolar():

    bot = telepot.Bot('xxxxxxxxxxxxxxxxxxxx')  # your bot token
    date = time.strftime("[%A] %d/%m/%Y - %H:%M:%S")

    print("Inicializando...")

    req = Request('https://www.melhorcambio.com/dolar-hoje', headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    soup.prettify()

    lista_valores = []

    for valor in soup.findAll('td', class_='tdvalor'):
        lista_valores.append(valor.text)

    dolar = lista_valores[2].split('R$')
    dolar = int(dolar[1].replace(',', '.'))

    print(dolar)

    if dolar < 3.5:
        bot.sendMessage(99999999, 'O valor do dolar está abaixo de R$ 3.50!!')  # 99999999 = your telegram id
        bot.sendMessage(99999999, 'Última atualização: ' + date)

        schedule.every(10).minutes.do(verificaDolar)


while True:
    schedule.run_pending()
    time.sleep(1)
