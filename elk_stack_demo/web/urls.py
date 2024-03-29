from tornado.web import RequestHandler
from typing import List, Tuple

from elk_stack_demo.web.handlers import PingHandler, EvalHandler

ping_url = (r'/ping/', PingHandler)

custom_urls = [
    (r'/eval', EvalHandler)
]


def get_all_urls() -> List[Tuple[str, RequestHandler]]:
    return custom_urls + [ping_url]
