import time
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options

def Signature(har, url):
    for entry in har["log"]["entries"]:
        if entry["request"]["url"].startswith(url):
            for query in entry["request"]["queryString"]:
                if query["name"] == "_signature":
                    return query["value"]

username = input("Username: ")

server = Server('browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--user-agent=DuckDuckBot')

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
proxy.new_har()

driver.get(f'https://www.tiktok.com/@{username}')

time.sleep(5) #Wait for page to load

print("Discover Signature: {0}".format(Signature(proxy.har, "https://m.tiktok.com/node/share/discover")))
print("User Detail Signature: {0}".format(Signature(proxy.har, "https://m.tiktok.com/api/user/detail")))
print("Post Signature: {0}".format(Signature(proxy.har, "https://m.tiktok.com/api/item_list")))