import requests

from bs4 import BeautifulSoup

url="https://goibibo.com/hotels/hotels-in-shimla-ct/"

#Headers

headers={
    'User-Agent':"Mozilla/5.0 (x11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko Chrome 77.0.3865.90 Safari/537.36)"
}

data = requests.get(url,headers=headers).text
soup = BeautifulSoup(data, 'html.parser')

images = soup.find_all('img',src=True)

print('Number of Images: ', len(images))
print('\n')
for image in images:
    if(image.has_attr('src')):
        print(image['src'])