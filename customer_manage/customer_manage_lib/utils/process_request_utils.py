import jwt
from jwt.exceptions import DecodeError, InvalidSignatureError
from jsonschema import Draft4Validator
from functools import wraps
import json
from django.views import defaults

from customer_manage_lib.config import ACCESS_TOKEN_SECRET
from .utils import get_now_ts, api_response
from customer_manage_lib.constants import Result
from customer_manage_lib.logger import Logger
from customer_manage_lib.manager import customer_manager

log = Logger('main').logger


def verify_access_token():
	def _verify_access_token(func):
		def _func(request, data, *args, **kwargs):
			if "access_token" not in data:
				log.warn("access_token_not_found|data=%s", data)
				return api_response(Result.INVALID_ACCESS_TOKEN)
			try:
				session = jwt.decode(data['access_token'], ACCESS_TOKEN_SECRET, algorithms=['HS256'])
			except Exception in (DecodeError, InvalidSignatureError):
				log.warn('access_token_is_invalid|access_token=%s' % data['access_token'])
				return api_response(Result.INVALID_ACCESS_TOKEN)

			# verify session timestamp
			if session['expiry_time'] < get_now_ts():
				log.warn('access_token_expired|session=%s' % session)
				return api_response(Result.INVALID_ACCESS_TOKEN)

			data['session'] = session
			return func(request, data, *args, **kwargs)

		return _func

	return _verify_access_token


def parse_params(form, method='POST'):
	form = Draft4Validator(form)

	def _parse_params(func):
		@wraps(func)
		def _func(request, *args, **kwargs):
			if request.method != method:
				log.warning('wrong_method|url=%s,method=%s', request.get_full_path().encode('utf-8'), request.method)
				return api_response(Result.ERROR_PARAMS)

			if isinstance(form, (Draft4Validator)):
				try:
					formdata = json.loads(request.body)
				except:
					if request.body:
						log.warning('params_error|format=json,url=%s,body=%s', request.get_full_path().encode('utf-8'),
									request.body)
					return api_response(Result.ERROR_PARAMS)
				try:
					form.validate(formdata)
					data = formdata
				except Exception as ex:
					log.warning('params_error|format=form,url=%s,error=%s,body=%s',
								request.get_full_path().encode('utf-8'), ex, formdata)
					return api_response(Result.ERROR_PARAMS)
				return func(request, data, *args, **kwargs)
			return defaults.server_error(request)

		return _func

	return _parse_params


def pre_process_header():
	def _pre_process_header(func):
		def _func(request, *args, **kwargs):
			data = {}
			if len(args) > 0:
				data = args[0]

			headers = request.META
			try:
				data["api_version"] = headers["HTTP_X_API_VERSION"]
				data["access_token"] = headers.get("HTTP_X_ACCESS_TOKEN")
			except Exception as err:
				log.exception("header_invalid|headers=%s" % headers)
				return api_response(Result.ERROR_HEADER)

			# find ip country

			if len(args) > 0:
				return func(request, *args, **kwargs)
			else:
				return func(request, data, *args, **kwargs)

		return _func

	return _pre_process_header
