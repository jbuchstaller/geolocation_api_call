#get weather data

import os
import sys
from datetime import datetime as dt
import requests
import json
import argparse

geocoding_api_url = "https://geocoding-api.open-meteo.com/v1/search"

#city = "Berlin"

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("city")
	parser.add_argument("base_file_path")
	return parser.parse_args()

def get_current_weather(city):
	return(requests.get(url=geocoding_api_url, params=dict(name=city, format="json")))

def response_to_json(response):
	response_json = json.loads(response.text)
	return(response_json)

def main():

	args = parse_args()

	try:
		coordinates = get_current_weather(args.city)
		response_json = response_to_json(coordinates)
		print(response_json)
	except Exception as err:
		print("Some API error")

	now = dt.now()
	current_time = now.strftime("%H-%M-%S")
	print("Current Time=", str(current_time))
	coordinates_file = "coordinates_" + args.city + "_" + current_time + ".json"

	if response_json:
		with open(args.base_file_path + coordinates_file, 'w+', encoding = "utf8") as fp:
			json.dump(response_json, fp)