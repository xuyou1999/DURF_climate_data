import webbrowser
def auto_open(filename, start, end):
    f = open(filename, 'r')
    urls = f.readlines()
    for i in range(start - 1, end):
        url = urls[i]
        url = url.strip()
        webbrowser.open(url)
    f.close()

def get_total_line(filename):
    f = open(filename, 'r')
    urls = f.readlines()
    return len(urls)

if __name__ == "__main__":
    filename = input('filename? ')
    total_line = get_total_line(filename)
    print('There are in total', total_line, 'lines')
    startline = int(input('start line? '))
    endline = int(input('end line? '))
    auto_open(filename, startline, endline)