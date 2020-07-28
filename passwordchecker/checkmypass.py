import requests
import hashlib
import sys


# query pwned passboard 
def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/'+ query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check API and call again')

	return res

def get_password_leaks_count(hashes, hashes_to_check):
	#print(hashes.text)
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, c in hashes:
		if h == hashes_to_check:
			return c	
	return 0



def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5, tail = sha1password[:5], sha1password[5:]
	res = request_api_data(first5)
	count = get_password_leaks_count(res, tail)
	return count



def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f"your password got pawned {count} times! Change your password")
		else:
			print(f"your password is solid, no hack history")
	return None

if __name__ == "__main__":
	main(sys.argv[1:])