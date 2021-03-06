import urllib


def get_page(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def add_to_index(index, keyword, url):
    for keyword in index:
        index[keyword].append(url)
    else:
        # not found, add new keyword to index
        index[keyword] = [url]


def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index


print(crawl_web(get_page('url')))
