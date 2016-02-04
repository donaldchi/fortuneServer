#!/usr/bin/env python
#_*_coding: utf-8 _*_

import requests
import webbrowser
import cgi, cgitb

form = cgi.FieldStorage()
uname = form.getvalue('uname');
usex_m = form.getvalue('usex_m');
usex_f = form.getvalue('usex_f');
birth_y = form.getvalue('birth_y');
birth_m = form.getvalue('birth_m');
birth_d = form.getvalue('birth_d');
birth_h = form.getvalue('birth_h');
birth_s = form.getvalue('birth_s');
target_y = form.getvalue('target_y');

url = "http://www.unsin.co.kr/unse/free/today/result"

if usex_m=='true': sex = '남'
else: sex = '여'
payload = {'user_name': uname, 
'sex': sex, 
'birth_yyyy': birth_y, 
'birth_mm': birth_m, 
'birth_dd': birth_d, 
'birth_hh': birth_h, 
'birth_solunar': birth_s, 
'target_yyyy': target_y}

results = requests.post(url, payload)
contents = results.text

contents = contents[contents.find("<div class=\"cont\">"):contents.find("<!--// Contents -->")]
delStr = contents[contents.find("<div class=\"tab\">"):contents.find("<!--datetab-->")]
contents = contents.replace(delStr, "")
contents = contents.replace("src=\"", "src=\"http://www.unsin.co.kr")
contents = contents.replace("\"score_bg\"><em>", "\"score_bg\"><em>오늘의 일진점수: ");
# css= ["<link rel=\"stylesheet\" type=\"text/css\" href=\"/css/common.css\">\n",
#  	  "<link rel=\"stylesheet\" type=\"text/css\" href=\"/css/sub.css\">\n",
#  	  "<link rel=\"stylesheet\" type=\"text/css\" href=\"/css/free.css\">\n"]
# contents = "".join(css) + contents
# print(contents+uname+","+usex_m+","+usex_f+","+birth_y+","+birth_m+","+birth_d+","+birth_h+","+birth_s+","+target_y+ "sex="+sex)
print(contents)
