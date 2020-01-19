import datetime
import time
import json
from constants import DATE_FORMAT


def convert_string_to_date(str_date):
	return datetime.datetime.strptime(str_date, DATE_FORMAT).date()


def get_now_ts():
	return int(time.time())


def api_response(result_code, reply=None):
	from django import http
	response = http.HttpResponse(json.dumps({"result": result_code, "reply": reply}))
	response['content-type'] = 'application/json; charset=utf-8'
	
	return response
