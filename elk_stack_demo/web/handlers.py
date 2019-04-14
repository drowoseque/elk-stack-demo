import json
import logging
from tornado.web import RequestHandler

from elk_stack_demo.repositories import exceptions
from elk_stack_demo.services import context


class PingHandler(RequestHandler):
    _response = {
        'status': 'ok'
    }

    def get(self):
        self.write(self._response)
        self.set_status(200)
        self.finish()


class EvalHandler(RequestHandler):

    def get(self, *args, **kwargs):
        expression = str(self.get_argument('expression'))
        kontext = context.get(self)
        kontext.update({'expression': expression})
        try:
            result = str(eval(expression))
            self.write(result)
            self.set_status(200)
            self.finish()
        except Exception as e:
            exceptions.log(e, kontext)
            raise e
