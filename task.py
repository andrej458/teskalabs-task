# výstupem by mělo být (pro každý kontejner): name, cpu a memory usage, created_at, status a všechny přiřazené IP adresy. Datumová pole převeďte na UTC timestamp.  

from functools import reduce
import json
import datetime

from tinydb import TinyDB


db = TinyDB('db.json')

def get_by_keys(dct, *keys):
    return reduce(lambda d, key: d.get(key) if d else None, keys, dct)


with open('sample-data.json') as f:
    data = json.load(f)

for i in data:
    name = get_by_keys(i, 'name')

    cpu_usage = get_by_keys(i, 'state', 'cpu', 'usage')

    memory_usage = get_by_keys(i, 'state', 'memory', 'usage')

    created_at = get_by_keys(i, 'created_at')
    if created_at:
        created_at = datetime.datetime.fromisoformat(created_at)
        created_at = int(created_at.timestamp())

    status = get_by_keys(i, 'status')

    addresses = []
    network = get_by_keys(i, 'state', 'network')
    if network:
        for x in network:
            x_addresses = get_by_keys(network[x], 'addresses')
            for y in x_addresses:
                addresses.append(get_by_keys(y, 'address'))

    db.insert({
                'name': name, 
                'cpu_usage': cpu_usage, 
                'memory_usage': memory_usage, 
                'created_at': created_at,
                'status': status,
                'addresses': addresses
                })

