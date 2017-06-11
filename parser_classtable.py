# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import jsonify
from flask import request
from bs4 import BeautifulSoup
from Crosslink_Anaylize import Crosslink_Anaylize as CA
from pyquery import PyQuery as pq
import requests
import ast
import sys
import io
import json
from flask import Flask
app = Flask(__name__)
# def unicode_handle():
# 	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def make_summary(name):
	# unicode_handle()
	anaylze = CA()
	search_name = str(name)
	profile_url = anaylze.search_whos_profile(search_name)
	# print(profile_url)
	req_s = requests.Session() # 建連線
	r = req_s.get(profile_url)
	# print(r.text)
	web = pq(r.text)
	table = web(".col-md-9").find(".content")

	# print(table)
	# print(table("div").eq(1).attr("data-react-props"))
	#literal_eval->dictionary 
	dict_table = ast.literal_eval(table("div").eq(1).attr("data-react-props"))

	#print(dict_table)
	# print(dict_table["current_courses"])
	course_array = dict_table["current_courses"]
	data_dict={}
	for course in course_array:

		course_dict = ast.literal_eval(str(course))
		# print(course_dict)
		each_course_url = "https://www.crosslink.tw/courses/"+str(course_dict["id"]);
		# print(each_course_url)
		req_s = requests.Session() # 建連線
		r = req_s.get(each_course_url)
		# print(r.text)
		each_course_web = pq(r.text)
		# print(each_course_web.find("tr").eq(5).find("td").eq(1).text())
		course_time=each_course_web.find("tr").eq(5).find("td").eq(1).text()
		course_time_delet=str(course_time).replace(" ","")
		print(course_time_delet)
		print(course_time_delet[-1:])
		if(course_time_delet.isdigit()):
			course_time_delet=""
		if(str(course_time_delet[-1:])!=")"):
			course_time_delet=course_time_delet+"()"
		print(course_time_delet)
		course_time_replace_l=str(course_time_delet [:-1]).replace("(",",")
		course_time_replace_r=str(course_time_replace_l).replace(")",",")
		course_time_split=str(course_time_replace_r).split(",")
		# course_time_split = course_time_split [:-2] 
		data_dict.update({course_dict["name"]:course_time_split})
		
	# data = json.dumps(data_dict,ensure_ascii=False).encode('utf8')
	data = json.dumps(data_dict,ensure_ascii=False).encode('utf8')
	# print(data.decode('utf8'))
	return data.decode('utf8')
	# return data

@app.route('/summary', methods=['GET', 'POST'])
def summary():
	# return jsonify(d)
	data = request.data
	print("after make summary")
	print(data)
	# return data

	person_name = request.form.get('name', type=str)
	print('person_name')
	print(person_name)
	d = make_summary(person_name)

	# print("i got person name", person_name)
	return jsonify(d)



# @app.route('/')
# def hi():
#     print("welcome to dog pin's house!")



if __name__ == "__main__":
	# app.debug = True
	# handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    # handler.setLevel(logging.INFO)
    # app.logger.addHandler(handler)
	# app.run()
	app.run(host= '192.168.11.5', port=5000, debug=True)
