from ariadne import gql


type_defs = gql("""
    type Query {
        getAllTables(availableOnly: Boolean, size: Int): [Table]!
        getTable(id: ID!): Table
    }

    type Mutation {
        reserveTable(id: ID!): Boolean!
        changeTableStatus(id: ID!, status: Status!): Boolean!
    }

    type Subscription {
        # monitorTableStatus: [Table]!
        monitorTableStatus: Boolean!
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
