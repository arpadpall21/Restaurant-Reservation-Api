# Restaurant-Table-Reservation-Service
## Description
- This is a restaurant table reservation service that uses GraphQL API that allows users to make reservations and also allows the restaurant to manage their table status.
- We are simulating a restaurant with 30 tables (table stats are randomly generated at each server start)
- Customers can:
  - request all the tables' status
  - make reservations
- Restaurant Manager can:
  - change the status of any table
  - monitor table status changes through a separate connection (GraphQL subscription -> websocket connection)
- This is a fully working tool but not a production code, the goal is to demonstrate a GraphQL implementation through a real world-like example
## Setup
- Run `pip install -r requirements.txt` to install required packages (I recommend using a Python virtual environment)
- Run `python server.py` to start the GraphQL server
- In a separate terminal run `python spy.py` to start the spy client (this will monitor table status changes)

## Usage
- You will need a GraphQL client to interact with the API (like `GraphiQL`)
- Request the `http://localhost:3000/graphql` endpoint with the below examples
- In the spy terminal, you will see the table status changes (like when a table becomes `reserved`, `free`, `onPreparation`, `unavailable`)

### Client Query Examples:
- Request all tables:
```
query AllTables{
  getAllTables {
    id
    status
    size
  }
}
```
- Request available tables only:
```
query AllTables{
  getAllTables(availableOnly: true) {
    id
    status
    size
  }
}
```
- Request tables with 6 seats only:
```
query AllTables{
  getAllTables(size: 6) {
    id
    status
    size
  }
}
```
- Request the status of Table 21:
```
query GetTable{
  getTable(id: 21) {
    id
    size
    status
  }
}
```
- Reserve table 21 (returns `true` on successful reservation (if the table is free), `false` otherwise)
```
mutation ReserveTable {
  reserveTable(id: 21)
}
```

### Restaurant Manager Query Examples:
- Changes table 21 status to `onPreparation` (possible status: `free`, `reserved`, `onPreparation`, `unavailable`)

```
mutation ChangeTableStatus {
  changeTableStatus(id: 21, status: onPreparation)
}
```
