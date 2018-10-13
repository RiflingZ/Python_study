#Python学习记录
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

>2018年08月05日

- range()函数

start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;


stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5


step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)



实例

`range(10)        # 从 0 开始到 10`


`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`


`range(1, 11)     # 从 1 开始到 11`


`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`


`range(0, 30, 5)  # 步长为 5`


`[0, 5, 10, 15, 20, 25]`


`range(0, 10, 3)  # 步长为 3`


`[0, 3, 6, 9]`


`range(0, -10, -1) # 负数`


`[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]`


`range(0)`


`[]`


`range(1, 0)`


`[]`



`for num in range(len(p)):`

和


```
i = 0
while i < n:
	i = i + 1
```
是一样的

>2018年08月09日

- 多行字符串

```
"""
	内容
	"""
```

这样表示的字符串可以在多行显示,而不是像一行一样无限延伸

- .split的运用

`<string>.split`可以把字符串中的内容以空格为间隔分成一个个元素而构成列表

- 关于This inspection detects equality comparison with a boolean litera的警告

这个警告是出现在代码`if r1 != []`中的

原因是编译器觉得你可以有更简单的表达

解决方法是`if not r1`

这个表达确实更简洁了
>2018年08月15日

- 网络中响应和传输的路程

Internet: message -> bits -> electrons/photons

在终端输入traceroute命令可追踪目标网址

>2018年08月19日

- 增加用户点击信息

```
def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1] + 1


def add_to_index(index, keyword, url):  # format of index: [[keyword, [url,count], [url,count], ...]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url, 0])
            return
    index.append([keyword, [[url, 0]]])
```
如果要在index中增加用户点击次数的信息,则必须把index的格式变成[[keyword, [url,count],[url,count], ...]],...]这样的
然后再通过`record_user_click`函数检查index里面的url是否已经存在,如果存在,点击数加一
>2018年08月30日

- n次方

`x**n` x是底数 n为幂

- 留小数点的除法
>2018年09月24日

- python中`*`的某些运用

```
def make_hashtable_NOT(nbuckets):
    return [[]] * nbuckets

table = make_hashtable_NOT(3)
table[1].append(['1', ['https://www.baidu.com/']])
print(table[1])
print(table[0])
```
这串代码的输出结果是

```
[['1', ['https://www.baidu.com/']]]
[['1', ['https://www.baidu.com/']]]
```
在此代码中table[1]和table[0]的内容是一样的,这显然不是我们所期待的

这个的原因应该是该函数建立的列表中三个元素都是指向同一个内容的,所以改变其中一个就会改变所有,如果我们打印整个列表会发现每个元素都是一样的

```
def make_hashtable(nbuckets):
    for e in range(0, nbuckets):
        table.append([])
    return table
```
所以这串代码应该是一个很好的解决方案

>2018年10月09日

- Python的三种取整方式

https://blog.csdn.net/sinat_32547403/article/details/53375061

>2018年10月11日

- 记忆化

```
cache = {}


def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]
    
    
def cached_fibo(n):
    if n in [0, 1]:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1)
                + cached_execution(cache, cached_fibo, n - 2))


print(cached_execution(cache, cached_fibo, 100))
```
首先,如果直接输出`cached_fibo(100)`,他会耗费很长很长时间,大概直接运行`cached_fibo(40)`需要两分钟才得出结果

原因是如果不缓存的话，运算是指数上升的,fib(n)会占用2^n个栈空间用作递归,n给个100你存就炸了
运行`print(cached_execution(cache, cached_fibo, 100))`后发现,100并不在cache内

于是运行了`proc(proc_input)`,即`cached_fibo(100)`

继续运行
```(cached_execution(cache, cached_fibo, n - 1)
                + cached_execution(cache, cached_fibo, n - 2))
```

这将会使`cached_execution()`这个函数不断的执行,但是与无cache不同的是每当函数的变量重复的时候,cache的字典里已经存在了那个数的斐波那契数,便不再执行`cache[proc_input] = proc(proc_input)`,所以执行时间不再像无cache那样长?

比如说执行(cached_execution(cache, cached_fibo, 99)
                + cached_execution(cache, cached_fibo, 98))
的时候cache = {98:cached_fibo(98), 99: cached_fibo(99), 100:cached_fibo(100)}

因为这样做的斐波那契数列是从最后往前的，在运行98:cached_fibo(98), 99: cached_fibo(99), 100:cached_fibo(100)的时候，不知道之前的数，还不是会重复吗

还是说他在从运行的时候（比如fibo（98））时已经有了运行fibo（99）时的没有结果的fibo（97），直接用了那个没有结果的fibo（97）并且在cache里面创建了fibo（96），所以等于说从fibo（100）到fibo（1）都只过了一遍？

如果这样认为的话，没有结果的fibo（97）为什么可以直接用呢

###`f(3) = f(2) + f(1)`,这一步递归会遇到2个边界，得到`f(2) = 1 & f(1) = 1`

n = N 的时候我们知道不需要算两次,n = N 的时候也知道不需要算两次,直接得出对于任意N我们都是算一次

在运行的过程中cache中的内容创建是从大到小，然后冒号后面的内容待定，然后冒号后面的内容从小到大出现,比如100:x，99:x，……这样的顺序在cache里面出现,然后x从小到大补全.