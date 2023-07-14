from time import sleep
from graphql_client import GraphQLClient


UPTIME = 7 * 24 * 60 * 60       # 7 days

query = """
    subscription GetTableStatusChange{
        monitorTableStatus {
            id
            oldStatus
            newStatus
        }
    }
"""


def callback(_, data):
    if data['type'] == 'error':
        print(f'Error: {data["payload"]["message"]}')
        return

    payload = data['payload']['data']['monitorTableStatus']
    print(f'Tables with changed status: {payload}')


with GraphQLClient('ws://localhost:3000/graphql') as client:
    sub_id = client.subscribe(query, callback=callback)
    print('spy connected!')

    sleep(UPTIME)
    client.stop_subscribe(sub_id)
