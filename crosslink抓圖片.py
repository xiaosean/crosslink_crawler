#/usr/bin/python3
#-*-coding:utf-8-*-
import urllib.request
from pyquery import PyQuery as pq
import urllib,sys,requests,time
# import sys,io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


# q=pq(url="https://www.crosslink.tw/users/5444#")
req_s = requests.Session() # 建連線
r = req_s.get("https://www.crosslink.tw/courses/145391")
crosslink_herf = "https://www.crosslink.tw"
# print(r.text)
q = pq(r.text)

# print(q.text())
print()
req_user=requests.Session()
users_list = q("#course-users-container").find(".user-list")
# print(users_list)
for user in users_list("li"):
    # print(q(user).find("a").attr("href"))
    # print(user("a").text())
    # 獲得選課的user id
# user = users_list("li").eq(0)
    user_profile_link = crosslink_herf + q(user).find("a").attr("href")
    print(user_profile_link)
    # 去個人頁面
    q= pq(req_user.get(user_profile_link).text)
    # 抓取主頁的大頭貼
    # print(q)
    user_profile_bar = q(".profile-headline")
    print(user_profile_bar.text())
    user_name = q(user_profile_bar).find("a").find("img").attr("alt")
    user_pic_herf = "http:" + q(user_profile_bar).find("a").find("img").attr("src")
    print(user_pic_herf)
    try:
        info_set = "?type=large&width=640&height=640"
        user_pic_herf = user_pic_herf[0:user_pic_herf.find("?")] + info_set
        # 擷取字串為 中文名+id
        fb_id = user_pic_herf [user_pic_herf .find("com")+4:user_pic_herf .find("/picture")]
        title = user_name + " " + user_profile_link[user_profile_link.rfind("/")+1:] + " " +fb_id + ".png"
        # print("title = ", title)
        # 注意檔名還是不可取?/\之類的奇怪保留字
        urllib.request.urlretrieve(user_pic_herf, title)  
        # urllib.request.urlretrieve(網址,要取的名子) 
        print("成功下載 " + user_name + "的大頭貼")
    except Exception:
        print("奇怪 抓不到" + user_name + "的大頭貼")
# print(user.attr("altl"))
print("Done")
