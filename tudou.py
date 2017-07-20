import urllib.request
import requests
import hashlib


url1 = 'https://i.360.cn/login/?src=pcw_home&destUrl=https://www.360.cn/'
# url2 = 'https://login.360.cn'
session = requests.session()

headers = {
    'host': "login.360.cn",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'accept-language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    'accept-encoding': "gzip, deflate, br",
    'content-type': "application/x-www-form-urlencoded",
    # 'content-length': "383",
    'referer': "http://trends.so.com/index",
    # 'cookie': "__huid=105x2iQwF03SRrao%2B2vteGrJeWtSSdo%2FT97HTl0eHKkfU%3D; __guid=17324128.2994798245766499840.1497621952001.3354; __gid=54771369.942090841.1499863040948.1499863040948.1; quCryptCode=D6TqMQxFsplN%252FMtzPlEGkr7QxbUYWOAEXiWSktSMm%252BsoCAnWurixHUyOjj%252BOfA%252FrFRyMN%252B54KSo%253D; quCapStyle=2",
    'connection': "keep-alive",
    'upgrade-insecure-requests': "1",
    'cache-control': "no-cache",
    # 'postman-token': "942aa6c0-da43-a761-3b94-d05ad2bc42f8"
    }

res = session.request('GET', url1, headers=headers)
pw = '3646287'
password = hashlib.md5(pw.encode('utf-8')).hexdigest()
payload = {'account': 13784855457, 'password': password}
res1 = session.request('POST', url1, headers=headers, data=payload)
print(res1.text)













# # url = 'http://static.youku.com/v20170420.0/v/custom/upsplayer/player.swf?playerId=tdnws&autoPlay=true&skin=http://static.youku.com/v20170420.0/v/custom/upsplayer/skin/tdnws.swf&lang=td&vcode=XMjg4NDc0MjQ2OA==&cna=APG%2FETSZzWMCASRuKSqGTYDS&ytid=-1&winType=interior&adext='
#
# def cbk(a, b, c):
# 	'''回调函数
# 	@a: 已经下载的数据块
# 	@b: 数据块的大小
# 	@c: 远程文件的大小
# 	'''
# 	per = 100.0 * a * b / c
# 	if per > 100:
# 		per = 100
# 	print('%.2f%%' % per)
#
# videos = [
# 	# 'http://58.216.104.74/youku/697391607A240836D229A13757/03000201005964F880296106B4571D4BB67BBC-33B3-A994-7221-09495A0E204E.flv?sid=049982966568012cb8809&ctype=12&ccode=0402&duration=60&expire=18000&psid=21d62ea1ca04f05a9f683951814cf7a6&ups_client_netip=36.110.41.42&ups_ts=1499829665&ups_userid=&utid=APG%2FETSZzWMCASRuKSqGTYDS&vid=XMjg4NDc0MjQ2OA%3D%3D&vkey=Af918ba8c8950d8cae8c4ad5020ff0bd5&nk=59089876751_24997161067&ns=0_216384&special=true',
# 	# 'http://58.216.104.74/youku/697391607A240836D229A13757/03000201005964F880296106B4571D4BB67BBC-33B3-A994-7221-09495A0E204E.flv?sid=049982966568012cb8809&ctype=12&ccode=0402&duration=60&expire=18000&psid=21d62ea1ca04f05a9f683951814cf7a6&ups_client_netip=36.110.41.42&ups_ts=1499829665&ups_userid=&utid=APG%2FETSZzWMCASRuKSqGTYDS&vid=XMjg4NDc0MjQ2OA%3D%3D&vkey=Af918ba8c8950d8cae8c4ad5020ff0bd5&nk=315149794591_24997161076&ns=0_2720040&special=true',
# 	# 'http://58.216.104.74/youku/697391607A240836D229A13757/03000201005964F880296106B4571D4BB67BBC-33B3-A994-7221-09495A0E204E.flv?sid=049982966568012cb8809&ctype=12&ccode=0402&duration=60&expire=18000&psid=21d62ea1ca04f05a9f683951814cf7a6&ups_client_netip=36.110.41.42&ups_ts=1499829665&ups_userid=&utid=APG%2FETSZzWMCASRuKSqGTYDS&vid=XMjg4NDc0MjQ2OA%3D%3D&vkey=Af918ba8c8950d8cae8c4ad5020ff0bd5&nk=315149794603_24997161095&ns=720040_2720040&special=true',
# 	# 'http://58.216.104.74/youku/697391607A240836D229A13757/03000201005964F880296106B4571D4BB67BBC-33B3-A994-7221-09495A0E204E.flv?sid=049982966568012cb8809&ctype=12&ccode=0402&duration=60&expire=18000&psid=21d62ea1ca04f05a9f683951814cf7a6&ups_client_netip=36.110.41.42&ups_ts=1499829665&ups_userid=&utid=APG%2FETSZzWMCASRuKSqGTYDS&vid=XMjg4NDc0MjQ2OA%3D%3D&vkey=Af918ba8c8950d8cae8c4ad5020ff0bd5&nk=85681172980_24997161112&ns=1440080_2720040&special=true',
# 	# 'http://58.216.104.74/youku/697391607A240836D229A13757/03000201005964F880296106B4571D4BB67BBC-33B3-A994-7221-09495A0E204E.flv?sid=049982966568012cb8809&ctype=12&ccode=0402&duration=60&expire=18000&psid=21d62ea1ca04f05a9f683951814cf7a6&ups_client_netip=36.110.41.42&ups_ts=1499829665&ups_userid=&utid=APG%2FETSZzWMCASRuKSqGTYDS&vid=XMjg4NDc0MjQ2OA%3D%3D&vkey=Af918ba8c8950d8cae8c4ad5020ff0bd5&nk=411362345968_24997161130&ns=2160120_236050&special=true',
# 	'http://coding.imooc.com/e4e40f02-1a29-4e92-a234-95835d08f4f6'
# ]
# for i, url in enumerate(videos):
# 	urllib.request.urlretrieve(url, '%s.mp4' % i, cbk)






