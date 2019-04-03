# Download and install 'requests' library: pip install beautifulsoup4
# Download and install 'beautifulsoup4' library: pip install requests

import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

repeats = ("2019 Cable News Network","Listen to CNN (low-bandwidth usage)","Go to the full CNN experience")

r = requests.get('http://lite.cnn.io/en')
html_doc = BeautifulSoup(r.text, 'html.parser')
for link in html_doc.find_all('a', href=re.compile("/en/article")):
    url = 'http://lite.cnn.io' + link.get('href')
    r1 = requests.get(url, stream=True)
    for chunk in r1.iter_content(chunk_size=99):
        if chunk:
            f = open('news.txt', 'a')
            doc = BeautifulSoup(r1.text, 'html.parser')
            for para in doc.find_all('p'):
                content = para.string
                if not any(s in content for s in repeats):
                    # pprint(content)
                    f.write("{c}\n".format(c=content))
        f.close()
