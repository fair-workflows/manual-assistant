import cgi
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import List, Dict
import base64

from fairworkflows import FairStep
from jinja2 import Environment, PackageLoader, select_autoescape

logging.basicConfig(level=logging.DEBUG)
env = Environment(loader=PackageLoader('manualassistant', 'templates'), autoescape=select_autoescape('html'))

# TODO: Remove
USE_TEST_SERVER = True
EXAMPLE_STEP_URI = 'http://purl.org/np/RAFszXfE-J3sef_ZX_5LRMM6rHgBt7a1uQH-vZdxfy-RU'

HOST = 'localhost'
PORT = 8000
ENCODING = 'UTF-8'


def get_manual_step(uri: str) -> FairStep:
    step = FairStep.from_nanopub(uri, use_test_server=USE_TEST_SERVER)

    assert step.is_manual_task, 'Step is not a manual task!'
    return step


def render_manual_step(step: FairStep):
    template = env.get_template('manualstep.html')
    return template.render(step=step, outputs=outputs_to_html(step.outputs)).encode(ENCODING)


def outputs_to_html(outputs):
    """
    Extract the information necessary to render the outputs in an html form.
    :param outputs:
    :return:
    """

    for o in outputs:
        yield base64.b64encode(o.name.encode()).decode(), o.name, o.type


def _create_request_handler(uri):
    class ManualStepRequestHandler(BaseHTTPRequestHandler):
        def __init__(self, request, client_address, server):
            self.uri = uri
            self.step = get_manual_step(uri)
            super().__init__(request, client_address, server)

        def _set_response(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            self._set_response()
            self.wfile.write(render_manual_step(self.step))

        def do_POST(self):

            print('POST')
            # Assuming the form has been submitted
            form_data = cgi.parse(self.rfile)

            if _all_boxes_checked(form_data):
                self.server.confirm_output(form_data)
            else:
                # Just display the page again
                self.do_GET()

    return ManualStepRequestHandler


def _all_boxes_checked(form_data: Dict[str, List[str]]):
    return all(form_data.values())


def execute_manual_step(uri, **inputs):
    return run(uri)


class ManualTaskServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.done = False
        self.outputs = []

    def confirm_output(self, outputs):
        self.outputs = {base64.b64decode(k): v for k, v in outputs}
        self.done = True

    def is_done(self):
        return self.done


def run(uri: str):
    server_address = (HOST, PORT)
    server = ManualTaskServer(server_address, _create_request_handler(uri))

    logging.info('Starting Manual Step Assistant')
    logging.info(f'Please go to http://{HOST}:{PORT} to perform the manual step')

    try:
        while not server.is_done():
            server.handle_request()
        print(server.outputs)
        return server.outputs
    finally:
        server.server_close()


if __name__ == '__main__':
    run(EXAMPLE_STEP_URI)
