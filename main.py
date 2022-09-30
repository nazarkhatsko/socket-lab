from argparse import ArgumentParser
from webserver import (
    WebServer, Controller, Request, Response, HTTPStatusCode, ContentType
)


blog = Controller("/api/", {
    "posts": []
})

@blog.route_get("get/posts/")
def get_posts(req, state):
    try:
        return Response(HTTPStatusCode.OK, ContentType.JSON, state["posts"])
    except:
        return Response.failure()


@blog.route_post("new/post/")
def new_post(req, state):
    try:
        post_data = req.get_params("post_data")
        state["posts"].append({
            "id": len(state["posts"]),
            "data": post_data
        })
        return Response(HTTPStatusCode.OK, ContentType.JSON, state["posts"])
    except:
        return Response.failure()


@blog.route_post("remove/post/")
def remove_post(req, state):
    try:
        post_id = req.get_params("post_id")
        state["posts"] = list(filter(lambda post: post["id"] != post_id, state["posts"]))
        return Response(HTTPStatusCode.OK, ContentType.JSON, state["posts"])
    except:
        return Response.failure()


def main():
    parser = ArgumentParser(description="Process some integers.")
    parser.add_argument("--host", type=str, default="localhost", help="fdf")
    parser.add_argument("--port", type=int, default=3000, help="fdf")
    parser.add_argument("--listen", type=int, default=100, help="fdf")
    args = parser.parse_args()

    ws = WebServer(args.host, args.port, args.listen)
    ws.add_controllers([blog])
    ws.run()


if __name__ == "__main__":
    main()
