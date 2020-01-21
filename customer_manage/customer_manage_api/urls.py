"""customer_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import customer_api

urlpatterns = [
    url(r'^api/v1/customer/get-ids$', customer_api.get_customer_ids, name='get_customer_ids'),
    url(r'^api/v1/customer/get-infos$', customer_api.get_customer_infos, name='get_customer_list'),
    url(r'^api/v1/customer/get-detail$', customer_api.get_customer_details, name='get_customer_detail'),
    url(r'^api/v1/customer/create$', customer_api.create_customer, name='create_customer'),
    url(r'^api/v1/customer/update$', customer_api.update_customer, name='update_customer'),
    url(r'^api/v1/customer/delete$', customer_api.delete_customer, name='delete_customer'),
]
