from typing import Dict, Any

from tornado.web import RequestHandler

_REQUIRED_COOKIE_KEYS = ['_ga', '_ym_uid', 'flocktory-uuid']


def _get_user_identificators(request_handler: RequestHandler) -> Dict[str, Any]:
    return {
        key: request_handler.get_cookie(key) for key in _REQUIRED_COOKIE_KEYS
    }


def _get_ua(request_handler: RequestHandler) -> Dict[str, Any]:
    return {
        'User-Agent': request_handler.request.headers['User-Agent'],
    }


def get(request_handler: RequestHandler) -> Dict[str, Any]:
    d1 = _get_user_identificators(request_handler)
    d2 = _get_ua(request_handler)
    d1.update(d2)
    return d1
