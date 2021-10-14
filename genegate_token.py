import random
import pyqrcode
import time
import requests
import os

sT = time.time()

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
router = 'http://kavkev.kg/'

dir = os.path.join("QRCODES")
if not os.path.exists(dir):
    os.mkdir(dir)

for n in range(0, 100):

    token =''

    for i in range(0, 25):
        token += random.choice(chars)

    url = router+token
    urls = pyqrcode.create(url)
    urls.png(f'./QRCODES/myqr{n+1}.png', scale = 6)
    data = {
            "token": token,
            "slug": token
            }
    siteURL = 'http://localhost:8888/api/token/'
    response = requests.post(siteURL, data)


finT = time.time()-sT
finT = round(finT, 1)

print(f'{finT} seconds')