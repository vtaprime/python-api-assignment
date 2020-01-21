from django.core.cache import caches

CACHE_DEFAULT_EXPIRY_TIME = 5*60

CONFIG_GET_CUSTOMER_DETAIL = {
	'prefix': 'customer.detail.%s',
	'expiry_time': 5 * 60,
}

CONFIG_GET_CUSTOMER_INFOS = {
	'prefix': 'customer.info.%s',
	'expiry_time': 5 * 60,
}


def del_cache_by_one_key(prefix, expiry_time=60, cache_name="default"):
	def _cache_data(func):
		def _func(*args, **kwargs):
			cache_key = prefix % args[0]

			data = caches[cache_name].get(cache_key)
			if data is None:
				return func(*args)

			caches[cache_name].delete(cache_key)
			return func(*args)
		return _func
	return _cache_data


def cache_data_by_one_key(prefix, expiry_time=60, cache_name="default"):
	def _cache_data(func):
		def _func(*args, **kwargs):
			cache_key = prefix % args[0]

			data = caches[cache_name].get(cache_key)
			if data is None:
				data = func(*args)
				caches[cache_name].set(cache_key, data, expiry_time)
			else:
				if data:
					pass
					# log.info("cache_hit|cache_key=%s", cache_key)
			return data
		return _func
	return _cache_data


def cache_data_by_keys(prefix, expiry_time=CACHE_DEFAULT_EXPIRY_TIME, cache_name="default"):
	"""
	When use this decorator for cache a list of value, function has to:
		- input must be a list of key
		- output must be a dict
	"""
	def _cache_data(func):
		def _func(keys, **kwargs):
			if not keys:
				return {}
			keys = list(set(keys))
			result = {}
			key_map = {prefix % key: key for key in keys}
			cached_data_dict = caches[cache_name].get_many(key_map.keys())
			for cached_key, cached_data in cached_data_dict.items():
				key = key_map[cached_key]
				result[key] = cached_data
				keys.remove(key)
			if keys:
				response_data = func(keys)
				if response_data:
					data_to_cache = {prefix % key: data for key, data in response_data.items() if data}
					caches[cache_name].set_many(data_to_cache, expiry_time)
				return {**result, **response_data}
			else:
				return result

		return _func

	return _cache_data
