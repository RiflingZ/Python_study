def get_next_target(page):
    start_link = page.find('<a href=')#找到网页中第一个url前面的获取链接代码的位置
    if start_link == -1:#若找不到,返回None,0
        return None, 0
    start_quote = page.find('"', start_link)#找到第一个url前的一个引号的位置
    end_quote = page.find('"', start_quote + 1)#找到第一个引号后的引号,也就是url后的第一个引号的位置
    url = page[start_quote + 1:end_quote]#url就是之前找到的两个引号中间的值
    return url, end_quote#返回url和url之后的那个引号的位置


def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)#输出url
            page = page[endpos:]#接下来的网页从之前找到的url后的第一个引号开始
        else:
            break
