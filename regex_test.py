import re

pattern = re.compile(r"^(?=.*[A-Za-z@#$%])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{7,}[0-9]$")


password = input('please enter your poassword:')

if pattern.search(password):
	print("pass")
else:
	print("password not correct")