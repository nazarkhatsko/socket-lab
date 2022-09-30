import socket

from .request import Request
from .response import Response
from .types import HTTPMethod, HTTPStatusCode, ContentType
from .logging import log_info, log_warn


class WebServer:
    def __init__(self, host = "127.0.0.1", port = 3000, listen = 100):
        self.__host = host
        self.__port = port
        self.__listen = listen
        self.__controllers = []
        self.__middlewares = []
        self.__chunks = []
        self.__state = {}


    def set_listen(self, listen):
        self.__listen = listen


    def add_controllers(self, controllers):
        self.__controllers.extend(controllers)


    def add_middlewares(self, middlewares):
        self.__middlewares.extend(middlewares)


    def run(self):
        try:
            serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            serv_sock.bind((self.__host, self.__port))
            serv_sock.listen(self.__listen)
            log_info(f"Server started {self.__host}:{self.__port}")

            while True:
                client_sock, client_addr = serv_sock.accept()
                chunk = client_sock.recv(8192).decode("utf-8")
                client_sock.send(self.__call_route(chunk).encode("utf-8"))
                client_sock.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            log_warn("Server is shutting down")
        finally:
            serv_sock.close()


    def __parse_chunk(self, chunk):
        params = chunk.split("\n")[0].split(" ")
        return [HTTPMethod(params[0]), params[1]]


    def __call_route(self, chunk):
        method, path = self.__parse_chunk(chunk)
        for controller in self.__controllers:
            if controller.is_route(method, path):
                route = controller.get_route(method, path)
                return route(Request(chunk), controller.get_state()).send()
        return Response.failure().send()
