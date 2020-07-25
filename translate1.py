from translate import Translator

translator= Translator(to_lang="zh-TW")
try:
	with open('./word.txt', mode = 'r+') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
		my_file.write(translation)
except FileNotFoundError as err:
	print("file not exist!")

