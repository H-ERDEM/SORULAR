#1-) http://45.87.173.173/interface.kou/get.php adresine sürekli cihaz değerlerini gönderen bir aracımız var. Bu aracın sıcaklık değerini sürekli güncel olarak çekip yazdıran bir python kodu yazın. (Request modülü )
import requests
import time
r=requests.get('http://45.87.173.173/interface.kou/get.php')
r=r.json()
print(f"Anahtarlar: {r.keys()}")

while True:
    r=requests.get('http://45.87.173.173/interface.kou/get.php')
    r=r.json()
    print(f"{r.get('temperature')}")
    time.sleep(3)


