import pyqrcode
import time
import requests
import os
import shortuuid

sT = time.time()

router = 'http://kavkev.kg/'

dir = os.path.join("QRCODES")
if not os.path.exists(dir):
    os.mkdir(dir)

for n in range(0, 100):

    token = shortuuid.ShortUUID().random(length=25)

    url = router + token
    urls = pyqrcode.create(url)
    urls.png(f'./QRCODES/myqr{n+1}.png', scale = 6)
    data = {
            "token": token,
            "slug": token
            }
    siteURL = 'http://api-kavkev.kg/api/token/'
    response = requests.post(siteURL, data)


finT = time.time()-sT
finT = round(finT, 1)

print(f'{finT} seconds')