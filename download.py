from urllib import request,parse
from urllib.request import urlretrieve
import os

def download(filename, outputfolder, username = '', password = ''):    
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

                passman = request.HTTPPasswordMgrWithDefaultRealm()
                passman.add_password(None, url.strip(), username, password)
                auth_handler = request.HTTPBasicAuthHandler(passman)
                opener = request.build_opener(auth_handler)
                request.install_opener(opener)
                request.urlopen(url.strip())

                try:
                    urlretrieve(url.strip(), f.strip())
                    print('%s %i/%i' % (category, i, n_urls))
                except:
                     print('%s %i/%i' % (category, i, n_urls), 'no file')
                     

if __name__ == '__main__':
    download('C:\\Users\\xuyou\\Desktop\\DURF_climate_data\\Shanghai\\test.txt', 'SH')