#2018暑假Python学习记录<!--所有均在Python环境下适用-->

> 2018年07月28日

- 嵌套列表

```list = [['zhuyihua',19],['you',30],'20','10']```

- 小数

在数字后面加```.```使其在加减乘除的结果中得到小数

```print(1350 / 21)```的输出是64,而```print(1350 / 21.)```的结果是64.2857142857

- 字符串与列表在内容改变上的不同

字符串都是通过新建字符串如

```s = 'gg' ```

```s = 'gg' + 'wp'```

最后s的值是ggwp,它并没有改变s的值,而是新建了一个字符串

而列表如

```p = ['H','e','l','l','o']```

```p[0] = 'Y'```

最后p的值是['Y', 'e', 'l', 'l', 'o'],它是直接改变了列表的值

- 列表赋值变更

如果把p赋值给q,这是p和q指的就是同一个列表

当改变q的值时,p的值也会随之改变,即使没有提到p

>2018年7月30日

- 列表像是地址

在Python中,列表非常像C语言中的地址

也就是说在函数设计中无需return列表的值

- 在列表后面可添加元素

```<list>.append(<element>)```

- 列表的追加和长度

追加```<list> + <list>```

长度```len(<list>)```!!长度只表示列表第一层的个数!!

- for和while循环打印列表

```
def print_all_elements(p):
    for e in p:
        print(e)
```

其中e很神奇,第一个循环代表的是列表中第一个元素,第二个循环代表的是列表中第二个元素.

```
def print_all_elements(p):
    i = 0
    while i<len(p):
        print(p[i])
        i = i + 1
```

比while循环要简洁

- Index索引

```<list>.index(<valve>)```

如果传入的值存在于列表中,过程返回找到这个值的第一个位置.并不会返回接下来出现的其他位置.

如果传入的值不存于列表中,则会返回```ValueError: 传入的值 is not in list```

>2018年07月31日

- pop

``
<list>.pop()``

其作用是得到列表中最后的那个值,同时删除列表中最后那个值

>2018年08月01日

- 获取网页源代码

```
import urllib


def get_page(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html


print(get_page(url))
```

- 抓取网页循环

如果用`pop`那么抓取网页会进行深度优先搜索,比如第一个网页有n个url,它会跟随第n个url进行爬取,打开第n个url之后有m个url,它会跟随第m个url进行爬取.这就是深度优先搜索.

- 一个简单的爬虫

```
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


def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(get_page()))
            crawled.append(page)
    return crawled
    
    
print(crawl_web(get_page('url')))
```

这串代码已经被我写到了保存代码的文件夹里,本不该在这里出现.但是由于其重要的意义(基本上我过去所学的Python精华都在于此),我会着重记录.

`start_link = page.find('<a href=')`找到网页中第一个url前面的获取链接代码的位置

```
if start_link == -1:
        return None, 0
```
若找不到,返回None,0

`start_quote = page.find('"', start_link)`找到第一个url前的一个引号的位置

`end_quote = page.find('"', start_quote + 1)`找到第一个引号后的引号,也就是url后的第一个引号的位置

`url = page[start_quote + 1:end_quote]`url就是之前找到的两个引号中间的值

`return url, end_quote`返回url和url之后的那个引号的位置

`page = page[endpos:]`接下来的网页从之前找到的url后的第一个引号开始

`union(tocrawl,get_all_links(get_page()))`添加所有在正在爬取网页上找到的链接到`tocrawl`,这样可以避免在tocrawl中有重复的值

`crawled.append(page)`之前定义过的`get_all_links`函数会返回包含有这个页面上所有链接的列表用`append`会把这些页面添加入已爬取页面的列表中取

>2018年08月03日

- 可变列表

`p = p + [1]`的作用是新建一个列表,原列表保持不变

- for循环的新应用

```
usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]


def total_enrollment(p):
    total_students = 0
    total_tuition = 0
    for name, students, tuition in p:
        total_students = total_students + students
        total_tuition = total_tuition + tuition * students
    return total_students, total_tuition


print(total_enrollment(usa_univs))
```

这里的新应用只是我觉得很新鲜的新,你可以把列表中的列表的每一个元素的值赋值给一个变量,但是经过我测试这样做的条件是列表中的列表的元素个数必须相同, 不然就会报错.