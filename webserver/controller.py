from .types import HTTPMethod


class Controller():
    def __init__(self, root_route = "/", state = {}):
        self.__root_route = root_route
        self.__state = state
        self.__routes = {}


    def route_get(self, path):
        return self.__make_decorator(HTTPMethod.GET, path)


    def route_post(self, path):
        return self.__make_decorator(HTTPMethod.POST, path)


    def route_put(self, path):
        return self.__make_decorator(HTTPMethod.PUT, path)


    def route_delete(self, path):
        return self.__make_decorator(HTTPMethod.DELETE, path)


    def is_route(self, method, path):
        return method in self.__routes.keys() and path in self.__routes[method].keys()


    def get_route(self, method, path):
        func = self.__routes[method][path]
        if func:
            return func
        else:
            raise ValueError(f"Route '{path}' has not been registered")


    def get_state(self):
        return self.__state


    def __make_decorator(self, method, path):
        def decorator(func):
            if method not in self.__routes.keys():
                self.__routes[method] = {}
            self.__routes[method][self.__root_route + path] = func
            return func
        return decorator
