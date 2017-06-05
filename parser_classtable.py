from bs4 import BeautifulSoup
from Crosslink_Anaylize import Crosslink_Anaylize as CA
from pyquery import PyQuery as pq
import requests
import ast

anaylze = CA()
search_name = "林品潔"
profile_url = anaylze.search_whos_profile(search_name)
print(profile_url)
req_s = requests.Session() # 建連線
r = req_s.get(profile_url)
# print(r.text)
web = pq(r.text)
table = web(".col-md-9").find(".content")
# print(table)
# print(table("div").eq(1).attr("data-react-props"))
dict_table = ast.literal_eval(table("div").eq(1).attr("data-react-props"))
# print(dict_table)
# print(dict_table["current_courses"])
course_array = dict_table["current_courses"]
for i in course_array:
	# print(i)
	course_dict = ast.literal_eval(str(i))
	print(course_dict["name"])
#
# use beautiful soup to parser table
# soup = BeautifulSoup(r.text)
# print(soup.select(".col-md-9"))
#for course in soup.select(".course-name")
#	print(course)
#print(soup.select(".#simulator-table"))
# [<div class="col-md-9"><div class="white-block"><div class="page-header">105學年第二學期</div><div class="content"><div data-react-class="Simulator.Table" data-react-props='{"current_courses":[{"id":188869,"name":"數值計算","time_pairs":[{"M":["09:10","10:00"]},{"T":["10:20","11:10"]},{"T":["11:20","12:10"]}],"lecture":"鮑興國","credits":3,"users_count":50,"no":"CS3017301"},{"id":188867,"name":"資料庫系統","time_pairs":[{"T":["15:30","16:20"]},{"T":["16:30","17:20"]},{"F":["09:10","10:00"]}],"lecture":"吳怡樂","credits":3,"users_count":77,"no":"CS3010301"},{"id":188707,"name":"體育(網球)","time_pairs":[{"F":["10:20","11:10"]},{"F":["11:20","12:10"]}],"lecture":"楊正群","credits":0,"users_count":15,"no":"CC3511052"},{"id":188870,"name":"編譯器設計","time_pairs":[{"T":["13:20","14:10"]},{"T":["14:20","15:10"]},{"R":["10:20","11:10"]}],"lecture":"黃元欣","credits":3,"users_count":53,"no":"CS3020301"},{"id":188874,"name":"iOS程式設計","time_pairs":[{"M":["13:20","14:10"]},{"M":["14:20","15:10"]},{"R":["11:20","12:10"]}],"lecture":"黃元欣","credits":3,"users_count":16,"no":"CS3042701"},{"id":188875,"name":"穿戴式電子應用設計","time_pairs":[{"W":["10:20","11:10"]},{"W":["11:20","12:10"]},{"R":["15:30","16:20"]}],"lecture":"鄭欣明","credits":3,"users_count":20,"no":"CS3043701"},{"id":189399,"name":"新聞英文","time_pairs":[{"M":["10:20","11:10"]},{"M":["11:20","12:10"]}],"lecture":"吳景龍","credits":2,"users_count":25,"no":"FE1821704"},{"id":189883,"name":"永續綠色智慧生活","time_pairs":[{"R":["13:20","14:10"]},{"R":["14:20","15:10"]}],"lecture":"蘇威年","credits":2,"users_count":21,"no":"TCG053301"}]}'></div></div></div></div>]
#print(soup.select(".col-md-9 .content > .data-react-props"))
# print(soup.find(".col-md-9").text)
