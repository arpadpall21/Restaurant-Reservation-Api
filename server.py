from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from uvicorn import Config, Server

from handlers.type_def import type_defs
from handlers.query import query, mutation, subscription


schema = make_executable_schema(type_defs, query, mutation, subscription)
app = GraphQL(schema, debug=True)                       # change debug aftet DEV


if __name__ == '__main__':
    config = Config(app, port=3000)
    config.routes = [("/", app), ("/graphql", app)]

    server = Server(config)
    server.run()


# nail test concepts!!!!!!!