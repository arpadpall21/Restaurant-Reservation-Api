""" Generates a fake table map with random table stats
ex:
[
    {'id': '1', 'size': 4, 'vip': False, 'status': 'free'},
    ...
]
"""

import random


TOTAL_TABLES = 30
FREE_TABLE_CHANCE = .5
VIP_CHANCE = .15
SIZE_RANGE = (4, 12)
POSSIBLE_NON_FREE_STATUS = ['reserved', 'onPreparation', 'unavailable']


def generate_fake_table_map(total_tables=TOTAL_TABLES,
                            free_table_chance=FREE_TABLE_CHANCE,
                            vip_chance=VIP_CHANCE,
                            size_range=SIZE_RANGE,
                            possible_non_free_status=POSSIBLE_NON_FREE_STATUS):
    return [
        {
            'id': str(table_id),
            'size': random.choice(range(*size_range, 2)),
            'vip': random.random() < vip_chance,
            'status': 'free' if random.random() < free_table_chance else random.choice(possible_non_free_status),
        }
        for table_id in range(1, total_tables+1)
    ]
