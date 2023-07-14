from time import sleep
from graphql_client import GraphQLClient


UPTIME = 7 * 24 * 60 * 60       # 7 days

query = """
    subscription GetTableStatusChange{
        monitorTableStatus
    }
"""


def callback(_, data):
    if data['type'] == 'error':
        print(f'Error: {data["payload"]["message"]}')
        return

    payload = data['payload']['data']['monitorTableStatus']
    print(f': {payload}')


with GraphQLClient('ws://localhost:3000/graphql') as client:
    client.subscribe(query, callback=callback)
    print('websocket client connected!')
    sleep(UPTIME)
