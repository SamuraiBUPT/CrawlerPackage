import os
import requests
import xlwt
import json


url_front = 'https://dl.stream.qqmusic.qq.com/'
url_first_req = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w='

mode1 = input('按歌曲名查找 or 按歌手查找 （1/2）：')
mode1 = int(mode1)  # 输入默认是输入为字符串形式的
if mode1 == 2:
    singerName = input('请输入歌手名: ')
    request_1 = requests.get(url_first_req + singerName)
    json_req1 = request_1.text[9: -1]
    json_req1 = json.loads(json_req1)
    song_list = json_req1['data']['song']['list']
    for num in song_list:
        print('歌曲名：' + num['songname'])


songname = input('请输入歌曲名： ')
request_2 = requests.get(url_first_req + songname)
json_req2 = json.loads(request_2.text[9: -1])
music_list = json_req2['data']['song']['list']
print(music_list)
for i in range(len(music_list)):
    print(str(i) + '.' + '歌曲： ' + music_list[i]['songname'] + '                  专辑名： '
          + music_list[i]['albumname'] + '          歌手： ' + music_list[i]['singer'][0]['name'])

find_num = input('请输入曲目前面的数字： ')
songmid = music_list[int(find_num)]['songmid']
song_info_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch", "filename":"M800","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","filename":"M800","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % songmid
response_1 = requests.get(song_info_url).json()

if not response_1['req_0']['data']['midurlinfo'][0]['purl']:
    # 如果没有这个歌曲的purl
    print('该歌曲是VIP曲目')
    exit()

url_final = url_front + response_1['req_0']['data']['midurlinfo'][0]['purl']
print(url_final)

music_content = requests.get(url_final).content
print(response_1['req_0']['data']['midurlinfo'][0]['filename'][19: 22])
# 首先定位这个文件之前的所有位置
init_path = os.path.split(os.path.realpath(__file__))[0]
# 新建一个储存音乐的文件夹
if not os.path.exists(init_path + '\\MusicDownload'):
    os.mkdir(init_path + '\\MusicDownload')
open(init_path + '\\MusicDownload' + '\\' + music_list[int(find_num)]['songname'] +
     '-' + music_list[int(find_num)]['singer'][0]['name'] +
     '.' + response_1['req_0']['data']['midurlinfo'][0]['filename'][19: 22], 'wb').write(music_content)
