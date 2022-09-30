from enum import Enum


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    def __int__(self):
        return self.value


class HTTPStatusCode(Enum):
    OK = 200
    BAD_REQUEST = 400

    def __int__(self):
        return self.value


class ContentType(Enum):
    JSON = "application/json"
    HTML = "text/html"

    def __int__(self):
        return self.value

