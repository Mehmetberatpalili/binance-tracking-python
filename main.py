from binance import Client
import csv
import pandas as pd
client = Client(None, None)

def verileriGetir(sembol, periyot, baslangic, bitis):
    mumlar = client.get_historical_klines(sembol, periyot, baslangic, bitis)
    return mumlar

def csvOlustur(sembol, mumlar):
    csvDosya = open(sembol + ".csv", 'w', newline='')
    yazici = csv.writer(csvDosya, delimiter=',')
    for mumVerileri in mumlar:
        yazici.writerow(mumVerileri)
    csvDosya.close()

isim = "XRPUSDT"

def veriCekmeVeCSVOlusturma(client, verileriGetir, csvOlustur):
    semboller = ["XRPUSDT","ATOMUSDT","COMPUSDT"]
    for coin in semboller:
        csvOlustur(coin, verileriGetir(coin, client.KLINE_INTERVAL_1DAY, "1 July 2023", "1 August 2023"))
        print(coin,"Veriler Getirildi.")

#veriCekmeVeCSVOlusturma(client, verileriGetir, csvOlustur)
okunacakCsv = 'ATOMUSDT.csv'

#Open time , Open,High,Low,Close,Volume,Close time,Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume,Ignore)
basliklar=['open_time','open','high','low','close','vol','close_time','qav','nat','tbqav','İgnore']
df=pd.read_csv(okunacakCsv,names=basliklar)

acilis = df['open']
kapanis=('close')
print(kapanis)

