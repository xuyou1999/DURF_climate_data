from urllib import request,parse
from http.cookiejar import CookieJar
import re
from urllib.request import urlretrieve
import requests
import os
import ssl

def download(filename, outputfolder):    
    categories = [filename]
    folder = os.getcwd() + '\\' + outputfolder
    for category in categories:
        os.makedirs(folder, exist_ok=True)
        with open('%s' % category, 'r') as file:
            urls = file.readlines()
            n_urls = len(urls)
            
            for i, url in enumerate(urls):
                f = folder + '\\' + url.split('/')[-1]
                url = url.strip()
                '''
                dict = {"username":"you.xu@nyu.edu",
                        "password":"NYUShanghai2018",
                        #"redirect_uri": url,
                        "commit": "log in"
                        }
                
                data = bytes(parse.urlencode(dict),encoding="utf-8")
                cookie = CookieJar() 
                opener = request.build_opener(request.HTTPCookieProcessor(cookie))
                response = opener.open(url,data)
                '''
                #print(url)
                #print(requests.get(url.strip(), auth=("you.xu@nyu.edu", "NYUShanghai2018")).content)

                passman = request.HTTPPasswordMgrWithDefaultRealm()
                passman.add_password(None, url.strip(), "you.xu@nyu.edu", "NYUShanghai2018")
                auth_handler = request.HTTPBasicAuthHandler(passman)
                opener = request.build_opener(auth_handler)
                request.install_opener(opener)
                response = request.urlopen(url.strip())
                print(response)

                try:
                    urlretrieve(url.strip(), f.strip())
                    print('%s %i/%i' % (category, i, n_urls))
                except:
                     print('%s %i/%i' % (category, i, n_urls), 'no file')
                     

if __name__ == '__main__':
    download('C:\\Users\\xuyou\\Desktop\\DURF_climate_data\\Shanghai\\test.txt', 'SH')