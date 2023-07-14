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
        monitorTableStatus: [TableStatusChange]!
    }

    type Table {
        id: ID!
        size: Int!
        status: Status!
    }

    type TableStatusChange {
        id: ID!
        oldStatus: Status!
        newStatus: Status!
    }

    enum Status {
        free
        reserved
        onPreparation
        unavailable
    }
""")
