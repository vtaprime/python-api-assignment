import enum

LIMIT_ITEM_DEFAULT = 1000
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = DATE_FORMAT + " %H:%M"
HOUR_FORMAT = "%H:%M"
EXTRA_TIME_QUERY = 24*3600-1
VALID_AGE = 18


class TimeRangeQueryType():
	QUERY_BY_CREATE_TIME = 1
	QUERY_BY_UPDATE_TIME = 2


class Result():
	SUCCESS = 'success'
	INVALID_ACCESS_TOKEN = 'err_invalid_access_token'
	ERROR_SERVER = 'error_server'
	INVALID_USER = 'error_user_invalid'
	ERROR_HEADER = 'error_header'
	USER_NOT_FOUND = 'user_not_found'
	ERROR_MSG_DEFINE = 'error_define_message'
