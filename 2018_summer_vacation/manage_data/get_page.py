import urllib


def get_page(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html


print(get_page('url'))
