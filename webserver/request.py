import json


class Request:
    def __init__(self, chunk):
        self.__chunk = chunk
        self.__body = {}

        data = chunk.split("\n")
        if data[-1] != "":
            self.__body = json.loads(data[-1])


    def __str__(self):
        return self.__chunk


    def get_params(self, key):
        return self.__body[key]


    # def get_ip(self):
    #     return self.__params["ip"]


    # def get_host(self):
    #     return self.__params["host"]


    # def get_device(self):
    #     return self.__params["device"]


    # def get_method(self):
    #     return self.__params["method"]


    # def get_route(self):
    #     return self.__params["route"]


    # def __parse_chunk(self, chunk):
    #     pass
