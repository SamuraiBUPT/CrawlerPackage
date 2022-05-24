import os
import xlwt
import requests
import json

Mypath = os.path.split(os.path.realpath(__file__))[0]  # 首先截取当前文件的文件地址 然后通过split把路径与文件名分离，这里得到的就是MyFirstPC.py这个文件的前面的所有路径
# print(Mypath)
savepath = Mypath + '\\MyExcel.xls'  # 保存这个文件的文件名
# print(savepath)
book = xlwt.Workbook(encoding="UTF-8", style_compression=0)  # 建立excel工作簿  workbook

sheet = book.add_sheet('Mysetu', cell_overwrite_ok=True)  # 新建sheet表

col = ('pid', 'page', 'uid', 'title', 'author', 'r18', 'tags', 'url')  # 在这里写excel表格的标签  这是一个元组
for i in range(0, 8):
    sheet.write(0, i, col[i])  # 第一个参数是行 第二个参数是列 第三个参数是要写入的东西 这里的意思就是把col元组里面的东西写入excel表格

url = "https://api.lolicon.app/setu/v2"
date = {
    "proxy": "i.pixiv.re",  # 代理
    "r18": 1
}  # 这是一个字典类  里面记录键值对

headers = {'User-Agent': 'mozilla/5.0 (windows nt 6.1; wow64) applewebkit/537.36 (khtml, like gecko) chrome/27.0.1453.94 safari/537.36'}  #
r = requests.get(url, params=date)  # params就是这个方法的参数 此处是用语法：标注和冒号的形式来确保data的传入 但是这个参数是可选的 并不是必须有
result = r.json()

n = input('请输入要图的数量：')
n = int(n)
k = 0

for i in range(0, n):
    k += 1
    if k == 10:
        book.save(savepath)  # savepath在前面定义过了 这里是个字符串 即文件路径名  这句话就是保存这个工作簿  保存名字为savepath的路径
        k = 0
    r = requests.get(url, params=date)  # 使用request.get()之后 返回的是一个字典类  这个是接口的响应  这种响应是json格式的的数据
    result = r.json()
    datalist = [result['data'][0]['pid'],
                result['data'][0]['p'],
                result['data'][0]['uid'],
                result['data'][0]['title'],
                result['data'][0]['author'],
                result['data'][0]['r18'],
                result['data'][0]['tags'],
                result['data'][0]['urls']['original']]
    for j in range(0, 8):
        sheet.write(i+1, j, datalist[j])  # 从第一行开始写读取到的东西 0列 1 列 2列……写入对应的datalist list内容
    setuurl = result['data'][0]['urls']['original']
    print(setuurl)
    print(result['data'][0]['title'])
    if result['data'][0]['r18'] == True:
        print('R18')
    if not os.path.exists(Mypath + '\\Mysetu'):  #如果不存在这个Mysetu文件夹
        os.mkdir(Mypath + '\\Mysetu')  # 创建这个目录 按照参数里给的路径来
    setupath = Mypath + '\\Mysetu'
    if not os.path.exists(Mypath + '\\Mysetu\\R18'):
        os.mkdir(Mypath + '\\Mysetu\\R18')
    myfile = requests.get(setuurl, headers=headers)  # 返回一个json的数据表
    if result['data'][0]['r18'] == True:
        open(setupath + '\\R18' + '\\' + result['data'][0]['title'] + '.' + result['data'][0]['ext'], 'wb').write(myfile.content)  # 打开这个路径 形式为'wb',把爬取到的东西写进去  就是myfile.content



book.save(savepath)
