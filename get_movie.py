# coding:utf-8
import urllib2
import json
import codecs
import time

list_f = []
list_m = []
for i in range(4):
    list_f.append(codecs.open(r'd:\\douban_movies\%d.txt' % i, 'a+', 'utf-8'))
    infoes = list_f[i].readlines()
    list_m.append([])
    for l in infoes:
        list_m[i].append(l.split()[0]) 
    list_f[i].seek(0, 2)

tags = ['爱情', '剧情', '音乐', '歌舞', '家庭', '儿童', '传记', '历史', '战争', '犯罪', '西部', '奇幻', '冒险', '灾难', '武侠', '古装', '鬼怪', '运动', '戏曲', '美国', '中国大陆', '香港', '台湾', '日本', '韩国', '英国', '法国', '意大利', '西班牙', '德国', '泰国', '印度', '加拿大', '澳大利亚', '俄罗斯', '波兰', '丹麦', '瑞典', '巴西', '墨西哥', '阿根廷', '比利时', '奥地利', '荷兰', '匈牙利', '土耳其', '希腊', '爱尔兰', '伊朗', '捷克', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2001-2005', '1996-2000', '1991-1995', '1986-1990', '1981-1985', '70年代', '60年代', '50年代', '40年代', '30年代', '早期']
for t in tags:
    for s in range(0, 200, 20):
        time.sleep(0.2)
        print t.decode('utf-8'), s,
        url = 'http://api.douban.com/v2/movie/search?tag=%s&start=%d' % (t, s)
        resp = urllib2.urlopen(url)
        print 'loaded',
        html = resp.read()
        print 'read',
        data = json.loads(html)
        print 'jsoned',

        if not data['subjects']:
            break
        print 'writing'
        for movie in data['subjects']:
            c = movie['collect_count']

            if c >= 100000:
                m = list_m[3]
                f = list_f[3]
            elif c >= 10000:
                m = list_m[2]
                f = list_f[2]
            elif c >= 1000:
                m = list_m[1]
                f = list_f[1]
            else:
                m = list_m[0]
                f = list_f[0]

            mid = movie['id']
            if mid in m:
                continue

            info = '%s %s %s %s %d %.1f\n' % (
                mid,
                movie['title'],
                movie['original_title'],
                movie['alt'],
                c,
                movie['rating']['average'],
            )
            try:
                print info
            except:
                pass
            f.write(info)

for i in range(4):
    list_f[i].close()
