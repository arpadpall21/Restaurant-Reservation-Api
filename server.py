from ariadne import gql, make_executable_schema, QueryType, MutationType, SubscriptionType
from ariadne.asgi import GraphQL
from uvicorn import Config, Server

from utils.create_fake_table_map import generate_fake_table_map


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

table_map = generate_fake_table_map()

query = QueryType()
mutation = MutationType()
subscription = SubscriptionType()


@query.field("getAllTables")
def resolve_get_all_tables(*_, availableOnly=False, size=None):
    if availableOnly and size:
        return [table for table in table_map if table['status'] == 'free' and table['size'] == size]
    elif availableOnly:
        return [table for table in table_map if table['status'] == 'free']
    elif size:
        return [table for table in table_map if table['size'] == size]
    else:
        return table_map


schema = make_executable_schema(type_defs, query, mutation, subscription)
app = GraphQL(schema, debug=True)


if __name__ == '__main__':
    config = Config(app, port=3000)
    config.routes = [("/", app), ("/graphql", app)]

    server = Server(config)
    server.run()
