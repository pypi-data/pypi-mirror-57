# -*- coding: utf-8 -*-

import requests
import logging
from django.conf import settings
from requests.exceptions import ConnectTimeout, ConnectionError
from sparrow_cloud.registry.service_discovery import consul_service
from .exception import HTTPException

logger = logging.getLogger(__name__)


def get_settings_service_name():
    """获取settings中的配置"""
    value = getattr(settings, 'SERVICE_CONF', '')
    if value == '':
        return ''
    service_name = value.get('NAME', '')
    return service_name


def get(service_conf, api_path, timeout=10, retry_times=3, *args, **kwargs):
    """
    :param service_conf: 服务配置
    :param api_path: 请求url
    :param timeout: 超时时间， 默认5秒
    :param args:
    :param kwargs:
    :return:
    """
    error_message = None
    service_name = get_settings_service_name()
    for _ in range(int(retry_times)):
        try:
            url = _build_url(service_conf, api_path)
            res = requests.get(url, timeout=timeout, *args, **kwargs)
            return _handle_response(res)
        except (ConnectionError, ConnectTimeout)as ex:
            error_message = ex.__str__()
            logger.error("rest_client error,service_name:{}, api_path:{}, message:{}, retry:{}".format(service_name,
                                                                                                       api_path,
                                                                                                       error_message,
                                                                                                       int(_)+1))
    raise Exception("rest_client error, service_name: {}, api_path:{}, message: {}".format(service_name, api_path,
                                                                                           error_message))


def post(service_conf, api_path, timeout=10, retry_times=3, *args, **kwargs):
    """
    :param service_conf: settings 里面配置的服务注册 key 值
    :param api_path:
    :param timeout:
    :param args:
    :param kwargs:
    :return:
    """
    error_message = None
    service_name = get_settings_service_name()
    for _ in range(int(retry_times)):
        try:
            url = _build_url(service_conf, api_path)
            res = requests.post(url, timeout=timeout, *args, **kwargs)
            return _handle_response(res)
        except (ConnectionError, ConnectTimeout)as ex:
            error_message = ex.__str__()
            logger.error("rest_client error,service_name:{}, api_path:{}, message:{}, retry:{}".format(service_name,
                                                                                                       api_path,
                                                                                                       error_message,
                                                                                                       int(_)+1))
    raise Exception("rest_client error, service_name: {}, api_path:{}, message: {}".format(service_name, api_path,
                                                                                           error_message))


def put(service_conf, api_path, timeout=10, retry_times=3, *args, **kwargs):
    """
    :param service_conf: settings 里面配置的服务注册 key 值
    :param api_path:
    :param timeout:
    :param args:
    :param kwargs:
    :return:
    """
    error_message = None
    service_name = get_settings_service_name()
    for _ in range(int(retry_times)):
        try:
            url = _build_url(service_conf, api_path)
            res = requests.put(url, timeout=timeout, *args, **kwargs)
            return _handle_response(res)
        except (ConnectionError, ConnectTimeout)as ex:
            error_message = ex.__str__()
            logger.error("rest_client error,service_name:{}, api_path:{}, message:{}, retry:{}".format(service_name,
                                                                                                       api_path,
                                                                                                       error_message,
                                                                                                       int(_)+1))
    raise Exception("rest_client error, service_name: {}, api_path:{}, message: {}".format(service_name, api_path,
                                                                                           error_message))


def delete(service_conf, api_path, timeout=10, retry_times=3, *args, **kwargs):
    """
    :param service_conf: settings 里面配置的服务注册 key 值
    :param api_path:
    :param timeout:
    :param args:
    :param kwargs:
    :return:
    """
    error_message = None
    service_name = get_settings_service_name()
    for _ in range(int(retry_times)):
        try:
            url = _build_url(service_conf, api_path)
            res = requests.delete(url, timeout=timeout, *args, **kwargs)
            return _handle_response(res)
        except (ConnectionError, ConnectTimeout)as ex:
            error_message = ex.__str__()
            logger.error("rest_client error,service_name:{}, api_path:{}, message:{}, retry:{}".format(service_name,
                                                                                                       api_path,
                                                                                                       error_message,
                                                                                                       int(_)+1))
    raise Exception("rest_client error, service_name: {}, api_path:{}, message: {}".format(service_name, api_path,
                                                                                           error_message))


def _build_url(service_conf, api_path):
    servicer_addr = consul_service(service_conf)
    return "http://{}{}".format(servicer_addr, api_path)


def _handle_response(response):
    if 200 <= response.status_code < 300:
        if response.content:
            try:
                res_result = response.json()
            except Exception as ex:
                res_result = {
                    "data": response.content,
                    "message": str(ex),
                }
        else:
            res_result = {}
        return res_result
    else:
        xx = HTTPException(
            code="http_exception",
            detail=response.content,
        )
        xx.status_code = response.status_code
        raise xx