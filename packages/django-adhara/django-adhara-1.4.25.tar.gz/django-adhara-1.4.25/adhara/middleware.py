import datetime
import json
import logging
from urllib.parse import unquote

from django.middleware.csrf import CsrfViewMiddleware

from .exceptions import AdharaException
from .meta import Meta, Page
from .request import AdharaRequest, APIMethods
from .response_utils import ApiResponse
from .thread_local import ThreadLocal

logger = logging.getLogger(__name__)


class ThreadLocalMiddleware:
    """
     Simple middleware that adds the request object in thread local storage.
     Usage not recommended!
    """

    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_request(self, request):
        ThreadLocal.set_request(request)

    def process_response(self, request, response):
        ThreadLocal._del_request()

    def process_exception(self, request, exception):
        ThreadLocal._del_request()


class DebugMiddleware:

    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response

    def process_request(self, request):
        request.ADHARA_DEBUG = {
            "start_time": datetime.datetime.now()
        }

    def process_response(self, request, response):
        print(
            "request {0} took {1} ms".format(
                request.path,
                datetime.datetime.now()-request.ADHARA_DEBUG["start_time"]
            )
        )
        return response


class AdharaMiddleware:

    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):

        path = request.path
        app = path.strip('/').split('/')[0]

        try:
            self.process_request(request)
        except ValueError as ve:
            print(ve)
            return ApiResponse.error("invalid json received")
        except TypeError as te:
            print(te)
            return ApiResponse.error("input format not supported")
        except StopIteration as se:
            print(request.method, "not allowed")
            return ApiResponse.error("Method not allowed")
        except AdharaException as ae:
            return ApiResponse.error(ae.get_message())
        return self.get_response(request)

    @staticmethod
    def process_request(request):
        try:
            ct = request.META['CONTENT_TYPE']
            cts = [cti.strip() for cti in ct.split(";")]
        except KeyError:
            ct = None
            cts = [""]

        input_json = {}
        if request.method == 'GET':
            qs = unquote(request.META['QUERY_STRING'])
            query_params = {}
            qs = qs.split('&')
            if not ((len(qs) == 1) and (qs[0].strip() == '')):
                for q in qs:
                    q = q.split('=')
                    try:
                        query_params[q[0]] = json.loads(q[1])
                    except ValueError:
                        query_params[q[0]] = q[1]
                    except IndexError:
                        ApiResponse.error("Invalid input")
                input_json = query_params
        if request.method == 'POST':
            if cts[0] == "application/json":
                # rb = request.body.decode(cts[1] if len(cts) > 1 else 'utf-8')
                rb = request.body.decode('utf-8')
                if rb.strip():
                    input_json = json.loads(rb)
            elif cts[0] == "application/x-www-form-urlencoded":
                input_json = json.loads(json.dumps(request.POST))
            elif cts[0].startswith("multipart/form-data"):
                pass
            else:
                raise TypeError
        if request.method == 'PUT':
            if cts[0] == "application/json":
                # rb = request.body.decode(cts[1] if len(cts) > 1 else 'utf-8')
                rb = request.body.decode('utf-8')
                if rb.strip():
                    input_json = json.loads(rb)
            elif cts[0] == "application/x-www-form-urlencoded":
                input_json = json.loads(json.dumps(request.POST))
            elif cts[0].startswith("multipart/form-data"):
                input_json = json.loads(json.dumps(request.POST))
            else:
                raise TypeError
        if request.method == 'DELETE':
            if ct == "application/json":
                rb = request.body.decode('utf-8')
                if rb.strip():
                    input_json = json.loads(rb)
            else:
                pass

        if input_json and 'csrfmiddlewaretoken' in input_json:
            del input_json['csrfmiddlewaretoken']
        method = getattr(APIMethods, APIMethods(request.method).name)
        meta = None
        if "_meta" in input_json:
            meta = Meta(current_page=Page(page=input_json["_meta"]["page"]))
        request.adhara_request = AdharaRequest(request, method=method, input_json=input_json, meta=meta)
        return None


class AdharaTokenMiddleware(CsrfViewMiddleware):

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.META.get('HTTP_APIKEY'):
            return
        else:
            return super(AdharaTokenMiddleware, self).process_view(request, callback, callback_args, callback_kwargs)
