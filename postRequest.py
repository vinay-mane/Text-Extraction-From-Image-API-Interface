import requests
url = 'http://127.0.0.1:5000/sendImage'
my_img = {'image': open('j.png', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())