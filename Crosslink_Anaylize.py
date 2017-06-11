# -*- coding: utf-8 -*-

import urllib.request
from pyquery import PyQuery as pq
import urllib,sys,requests,time
class Crosslink_Anaylize:
    def __init__(self):
        self.host_path = "https://www.crosslink.tw"
        self.course_herf = ""
        self.profile_herf = ""
    def search_course_web(self, code):
        search_course_herf = "https://www.crosslink.tw/courses?utf8=%E2%9C%93&q%5Byear_eq%5D=1051&q%5Buniversity_id_eq%5D=1&q%5Bno_cont%5D=" + code + "&q%5Bname_or_lecture_cont%5D=&commit=Search"
        # print(search_course_herf)
        req_s = requests.Session() # 建連線
        r = req_s.get(search_course_herf)
        # print(r.text)
        q = pq(r.text) #將原始碼丟入 進行解析
        self.course_herf = self.host_path + q(".course-name").find("a").attr("href")
        return(self.course_herf)

    def search_whos_profile(self, name):
        '''找到那個人的主頁'''
        name_web = "https://www.crosslink.tw/explorers?utf8=%E2%9C%93&q%5Buniversity_id_eq%5D=&q%5Bstories_desc_start%5D=&q%5Bname_or_full_name_cont%5D=" + name + "&commit=Search"
        req_s = requests.Session() # 建連線
        r = req_s.get(name_web)
        # print(r.text)
        q = pq(r.text) #將原始碼丟入 進行解析
        # print(q.text())
        self.profile_herf = self.host_path + q(".white-block").find("a").attr("href")
        return(self.profile_herf)

    def search_classmate(self):
        # q=pq(url="https://www.crosslink.tw/users/5444#")
        req_s = requests.Session() # 建連線
        r = req_s.get(self.course_herf)
        q = pq(r.text) #透過pyquery分析字串
        print()
        req_user=requests.Session()
        users_list = q("#course-users-container").find(".user-list")
        # print(users_list)
        for user in users_list("li"):
            # print(q(user).find("a").attr("href"))
            # print(user("a").text())
            # 獲得選課的user id
        # user = users_list("li").eq(0)
            user_profile_link = self.host_path + q(user).find("a").attr("href")
            print(user_profile_link)
            # 去個人頁面
            q= pq(req_user.get(user_profile_link).text)
            # 抓取主頁的大頭貼
            # print(q)
            user_profile_bar = q(".profile-headline")
            print(user_profile_bar.text())
            try:
                user_name = q(user_profile_bar).find("a").find("img").attr("alt")
                user_pic_herf = "http:" + q(user_profile_bar).find("a").find("img").attr("src")
                # print(user_pic_herf)
            
                info_set = "?type=large&width=640&height=640"
                user_pic_herf = user_pic_herf[0:user_pic_herf.find("?")] + info_set
                # 擷取字串為 中文名+id
                fb_id = user_pic_herf [user_pic_herf .find("com")+4:user_pic_herf .find("/picture")]
                title = user_name + " " + user_profile_link[user_profile_link.rfind("/")+1:] + " " +fb_id + ".png"
                # print("title = ", title)
                # 注意檔名還是不可取?/\之類的奇怪保留字
                urllib.request.urlretrieve(user_pic_herf, title)  
                # urllib.request.urlretrieve(網址,要取的名子)        
                print("successfully download " + user_name + "'s photo")
            except Exception:
                print("failed to download  photo")
        # print(user.attr("altl"))
        print("Done")
if __name__ == '__main__':
    test = Crosslink_Anaylize()
    # test.search_course_web("MI3510701")
    # test.search_classmate()
    # print("測試")
    search_name = '林品潔'
    # print(search_name)
    print(test.search_whos_profile(search_name))
    # print(test.search_whos_profile(search_name))

    # print(href)
