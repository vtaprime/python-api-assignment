from models import *
from cache_manager import cache_data_by_one_key, del_cache_by_one_key, cache_data_by_keys, CONFIG_GET_CUSTOMER_INFOS, \
	CONFIG_GET_CUSTOMER_DETAIL
from constants import LIMIT_ITEM_DEFAULT
from utils.utils import get_now_ts, convert_string_to_date


def get_ids(name=None, dob=None, start_time=None, end_time=None, query_ts_type=1, limit=LIMIT_ITEM_DEFAULT):
	items = CustomerTab.objects
	if name:
		items = CustomerTab.objects.filter(name=name)
	if dob:
		items = items.filter(dob__date=dob)
	
	if start_time and end_time:
		if query_ts_type==1:
			items = items.filter(created_ts__lte=end_time).filter(created_ts__gte=start_time)
		elif query_ts_type==2:
			items = items.filter(updated_ts__lte=end_time).filter(updated_ts__gte=start_time)
	
	items = items.values_list('id', flat=True)[:limit]
	
	return list(items)


@cache_data_by_keys(CONFIG_GET_CUSTOMER_INFOS['prefix'])
def get_infos(ids):
	event_ids = CustomerTab.objects.filter(id__in=ids)
	
	return {item.id: item for item in event_ids}


def create(customer_info):
	now_ts = get_now_ts()
	customer_info['created_ts'] = now_ts
	customer_info['updated_ts'] = now_ts
	customer_info['dob'] = convert_string_to_date(customer_info['dob'])
	
	customer = CustomerTab.objects.create(
		**customer_info,
		is_deleted=False
	)
	
	return customer


@cache_data_by_one_key(**CONFIG_GET_CUSTOMER_DETAIL)
def get_detail(customer_id, is_deleted=None):
	item = CustomerTab.objects.filter(id=customer_id)
	if is_deleted:
		item = item.filter(is_deleted=is_deleted)
	else:
		item = item.filter(is_deleted=0)
	item = item.first()
	
	return item


@del_cache_by_one_key(**CONFIG_GET_CUSTOMER_DETAIL)
def update(customer_id, name=None, dob=None):
	item = CustomerTab.objects.get(id=customer_id)
	if item:
		now_ts = get_now_ts()
		item.updated_ts = now_ts
		if name:
			item.name = name
		if dob:
			item.dob = convert_string_to_date(dob)
		item.save()
		return item
	return None


@del_cache_by_one_key(**CONFIG_GET_CUSTOMER_DETAIL)
def delete(event_id):
	item = CustomerTab.objects.filter(id=event_id).update(is_deleted=1)
	
	return item
