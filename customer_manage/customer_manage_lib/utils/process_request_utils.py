import jwt
from jwt.exceptions import DecodeError, InvalidSignatureError
from customer_manage_lib.config import ACCESS_TOKEN_SECRET
from utils.utils import get_now_ts, api_response
from customer_manage_lib.constants import Result


def verify_access_token():
	def _verify_access_token(func):
		def _func(request, data, *args, **kwargs):
			if "access_token" not in data:
				log.warn("access_token_not_found|data=%s", data)
				return api_response(Result.INVALID_ACCESS_TOKEN)
			session = None
			try:
				session = jwt.decode(data['access_token'], ACCESS_TOKEN_SECRET, algorithms=['HS256'])
			except Exception in (DecodeError, InvalidSignatureError):
				return api_response(Result.INVALID_ACCESS_TOKEN)
			
			if session is None:
				log.warn('access_token_is_invalid|access_token=%s' % data['access_token'])
				return api_response(Result.INVALID_ACCESS_TOKEN)
			# verify session timestamp
			if session['expirytime'] < get_now_ts():
				log.warn('access_token_expired|session=%s' % session)
				return api_response(Result.INVALID_ACCESS_TOKEN)

			data['session'] = session
			return func(request, data, *args, **kwargs)

		return _func

	return _verify_access_token
