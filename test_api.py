import requests
from time import time
t = time()
url = "http://127.0.0.1:8000/variation?input_image"
payload={}
files=[

('input_image',('2.jpg',open('./312.jpg','rb'),'image/jpg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
# response = requests.request("GET", url)
print(response.text)

print('Successful, results saved in Output directory')
print(f"Elapsed time is {time()-t}")