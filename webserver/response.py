import json

from .types import HTTPStatusCode, ContentType


class Response:
    def __init__(self, status_code, content_type, reason, headers = None, body = None):
        self.status_code = status_code
        self.content_type = content_type
        self.reason = reason
        self.headers = headers
        self.body = body


    def send(self):
        headers = self.__get_headers()
        data = self.__data_preparation(self.content_type, self.reason)
        return headers + data


    def __data_preparation(self, content_type, data):
        if content_type == ContentType.JSON:
            return json.dumps(data)
        return data


    def __get_headers(self):
        return "".join([
            f"HTTP/1.1 {self.status_code.value} OK\r\n",
            f"Accept: {self.content_type.value};\r\n",
            f"Access-Control-Allow-Origin: *\r\n",
            f"Content-Type: {self.content_type.value}; charset=utf-8;\r\n\r\n"
        ])

    @staticmethod
    def success(message = "All success"):
        return Response(HTTPStatusCode.OK, ContentType.JSON, {
            "code": 0,
            "status": "success",
            "message": message
        })


    @staticmethod
    def failure(message = "Incorrect path"):
        return Response(HTTPStatusCode.BAD_REQUEST, ContentType.JSON, {
            "code": 1,
            "status": "failure",
            "message": message
        })


    @staticmethod
    def json(data):
        return Response(HTTPStatusCode.OK, ContentType.JSON, {
            "code": 1,
            "status": "failure",
            "data": json.dump(data)
        })


    @staticmethod
    def file(filename):
        with open(filename) as f:
            return Response(HTTPStatusCode.OK, ContentType.JSON, {
                "code": 1,
                "status": "failure",
                "data": f.read()
            })
