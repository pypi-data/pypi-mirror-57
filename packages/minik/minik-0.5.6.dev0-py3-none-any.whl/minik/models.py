import json
from minik.status_codes import codes, get_description


class MinikRequest:
    """
    Simple wrapper of the data object received from API Gateway. This object will
    parse a given API gateway event and it will transform it into a more user
    friendly object to operate on. The idea is that a view does not need to be
    concerned with the inner representation of the APIGateway's event as long as
    it has access to the underlaying data values in the event.
    """
    __slots__ = ['request_type', 'path', 'resource', 'query_params', 'headers', 'uri_params',
                 'method', 'body', '_json_body', 'aws_context', 'aws_event']

    def __init__(self, request_type, path, resource, query_params, headers, uri_params, method, body, context, event):

        self.request_type = request_type
        self.path = path
        self.resource = resource
        self.query_params = query_params
        self.headers = headers
        self.uri_params = uri_params
        self.method = method
        self.body = body
        self.aws_context = context
        self.aws_event = event
        # The parsed JSON from the body. This value should
        # only be set if the Content-Type header is application/json,
        # which is the default content type.
        self._json_body = None

    @property
    def json_body(self):
        """
        Lazy loading/parsing of the json payload.
        """
        if self.headers.get('content-type', '').startswith('application/json'):
            if self._json_body is None:
                self._json_body = json.loads(self.body)
            return self._json_body


class Response:
    __slots__ = ['request_type', 'body', 'headers', 'status_code', 'is_base_64', 'multi_value_headers']

    def __init__(self, request_type=None, body='', headers=None, status_code=codes.ok):
        self.body = body
        self.headers = headers or {}
        self.status_code = status_code
        self.is_base_64 = False
        self.multi_value_headers = {}
        self.request_type = request_type

    @property
    def content_type(self):
        return {
            key.lower(): value
            for key, value in self.headers.items()
        }.get('content-type')

    def to_dict(self, binary_types=None):

        additional_fields = self.get_additional_response_fields()

        return {
            'headers': self.headers,
            'multiValueHeaders': self.multi_value_headers,
            'statusCode': self.status_code,
            'isBase64Encoded': self.is_base_64,
            'body': self.body,
            **additional_fields
        }

    def get_additional_response_fields(self):

        if self.request_type == 'alb_request':
            return {
                'statusDescription': get_description(self.status_code),
                'multiValueHeaders': self.get_alb_multivalue()
            }

        return {}

    def get_alb_multivalue(self):
        return {
            key: [value]
            for key, value in self.headers.items()
        }
