from .form_schema import CustomerSchema, CustomerInfoSchema, CustomerDeleteSchema
from customer_manage_lib.utils.utils import api_response
from customer_manage_lib.utils.process_request_utils import verify_access_token, parse_params, pre_process_header
from customer_manage_lib.manager import customer_manager
from customer_manage_lib.constants import Result


@parse_params(CustomerSchema)
@pre_process_header()
@verify_access_token()
def create_customer(request, data):
	customer = customer_manager.create({'name': data['name'], 'dob': data['dob']})

	if not customer:
		return api_response(Result.ERROR_SERVER)

	return api_response(Result.SUCCESS, customer)


@pre_process_header()
@verify_access_token()
def get_customer_ids(request):
	data = request.GET
	name = data.get('name')
	dob = data.get('dob')
	start_time = data.get('start_time')
	end_time = data.get('end_time')
	query_ts_type = data.get('type')
	limit = data.get('limit')
	ids = customer_manager.get_ids(name, dob, start_time, end_time, query_ts_type, limit)

	return api_response(Result.SUCCESS, {'ids': ids})


@pre_process_header()
@parse_params(CustomerInfoSchema)
@verify_access_token()
def get_customer_infos(request, data):
	customer_infos = customer_manager.get_infos(data['ids'])

	return api_response(Result.SUCCESS, {'customer_infos': customer_infos})


@pre_process_header()
@verify_access_token()
def get_customer_details(request):
	customer_id = request.GET.get('customer_id')
	customer = customer_manager.get_detail(customer_id)

	return api_response(Result.SUCCESS, customer)


@pre_process_header()
@parse_params(CustomerSchema)
@verify_access_token()
def update_customer(request, data):
	customer = customer_manager.update(data['id'], data.get('dob'), data.get('name'))

	if not customer:
		return api_response(Result.INVALID_USER)

	return api_response(Result.SUCCESS, customer)


@pre_process_header()
@parse_params(CustomerDeleteSchema)
@verify_access_token()
def delete_customer(request, data):
	customer = customer_manager.delete(data['id'])

	if not customer:
		return api_response(Result.INVALID_USER)

	return api_response(Result.SUCCESS, customer)
