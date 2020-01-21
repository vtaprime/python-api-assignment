import datetime
from datetime import date
import time
import json
from customer_manage_lib.constants import DATE_FORMAT


def convert_string_to_date(str_date):
	return datetime.datetime.strptime(str_date, DATE_FORMAT).date()


def convert_date_to_string(date_type):
	return date_type.strftime(DATE_FORMAT)


def convert_string_to_unix_timestamp(str_date):
	return int(time.mktime(datetime.datetime.strptime(str_date, DATE_FORMAT).timetuple()))


def get_now_ts():
	return int(time.time())


def api_response(result_code, reply=None):
	from django import http
	response = http.HttpResponse(json.dumps({"result": result_code, "reply": reply}))
	response['content-type'] = 'application/json; charset=utf-8'
	
	return response


def calculate_age(dob):
	born = convert_string_to_date(dob)
	today = date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
