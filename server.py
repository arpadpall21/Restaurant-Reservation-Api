from ariadne import gql, make_executable_schema, QueryType, MutationType, SubscriptionType
from ariadne.asgi import GraphQL
from uvicorn import Config, Server


type_defs = gql("""
    type Query {
        getAllTables(availableOnly: Boolean, size: Int): [Table]!
        getTable(id: ID!): Table
    }

    type Mutation {
        reverveTable(id: ID!): Boolean!
        changeTableStatus(id: ID!, status: Status!): Boolean!
    }

    type Subscription {
        tableStatusChanged: [Table!]!
    }

    type Table {
        id: ID!
        size: Int!
        vip: Boolean!
        status: Status!
    }

    enum Status {
        free
        reserved
        onPreparation
        unavailable
    }
""")

query = QueryType()
mutation = MutationType()
subscription = SubscriptionType()


schema = make_executable_schema(type_defs, query, mutation, subscription)
app = GraphQL(schema, debug=True)

if __name__ == '__main__':
    config = Config(app, port=3000)
    config.routes = [("/", app), ("/graphql", app)]

    server = Server(config)
    server.run()


# {'id': '1', 'size': 4, 'vip': False, 'status': 'free'}