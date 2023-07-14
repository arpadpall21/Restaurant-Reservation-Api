import asyncio

from ariadne import QueryType, MutationType, SubscriptionType

from utils.create_fake_table_map import generate_fake_table_map


table_map = generate_fake_table_map()

##################################################################
# query ##########################################################
query = QueryType()


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


@query.field("getTable")
def resolve_get_table(*_, id):
    return next((table for table in table_map if table['id'] == id), None)


##################################################################
# mutation #######################################################
mutation = MutationType()


@mutation.field("reserveTable")
def resolve_reserve_table(*_, id):
    table = next((table for table in table_map if table['id'] == id), None)
    if table and table['status'] == 'free':
        table['status'] = 'reserved'
        return True
    return False


@mutation.field("changeTableStatus")
def resolve_change_table_status(*_, id, status):
    table = next((table for table in table_map if table['id'] == id), None)
    if table:
        table['status'] = status
        return True
    return False


##################################################################
# subscription ###################################################
subscription = SubscriptionType()


@subscription.field('monitorTableStatus')
def resolve_monitor_table_status(monitorTableStatus, *_,):
    return monitorTableStatus


@subscription.source('monitorTableStatus')
async def notify_table_status_change(*_):
    while True:
        # yield table_map
        yield True
        await asyncio.sleep(1)
