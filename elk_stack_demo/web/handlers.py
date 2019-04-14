import json

from tornado.web import RequestHandler

from elk_stack_demo.services import gk
from elk_stack_demo.services.evaluator import evaluate


class PingHandler(RequestHandler):
    _response = {
        'status': 'ok'
    }

    def get(self):
        self.write(self._response)
        self.set_status(200)
        self.finish()


class EvalHandler(RequestHandler):
    _GK = '__GK'

    def write_and_finish(self, result: str):
        self.write(result)
        self.set_status(200)
        self.finish()

    def initialize(self):
        self.expression = str(self.get_argument('expression'))

    def get(self, *args, **kwargs):
        result = evaluate(self.expression)
        response = f"""{{
            'result': {result}
        }}"""

        self.write_and_finish(response)
