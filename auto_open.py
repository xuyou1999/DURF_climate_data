import webbrowser
def auto_open(filename):
    f = open(filename, 'r')
    urls = f.readlines()
    for url in urls:
        url = url.strip()
        webbrowser.open(url)
    f.close()

if __name__ == "__main__":
    filename = input('filename? ')
    auto_open(filename)