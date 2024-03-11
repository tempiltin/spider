import requests
import re
from urllib.parse import urljoin

target_url = "samtuit.uz"
target_links=[]
def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def extract_links_from(url):
    response = request(url)
    return re.findall(r'<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>', response.text)

href_links = extract_links_from(target_url)
for link in href_links:
    link = urljoin("http://" + target_url, link)

    if "#" in link:
        link = link.split("#"[0])
    if target_url in link and link not in target_links:
        target_links.append(link)
        print(link)
