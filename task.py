# výstupem by mělo být (pro každý kontejner): name, cpu a memory usage, created_at, status a všechny přiřazené IP adresy. Datumová pole převeďte na UTC timestamp.  

import json
import datetime


with open('sample-data.json') as f:
    data = json.load(f)

for i in range(len(data)):
    print(i)

    informations = {
        'name' : None,
        'cpu_usage' : None,
        'memory_usage' : None,
        'created_at' : None,
        'status' : None,
        'addresses' : None,
    }

    # name 
    try:
        informations['name'] = data[i]['name']
    except TypeError:
        pass
    
    # cpu usage 
    try:
        informations['cpu_usage'] = data[i]['state']['cpu']['usage']
    except TypeError:
        pass

    # memory usage
    try:
        informations['memory_usage'] = data[i]['state']['memory']['usage']
    except TypeError:
        pass

    # created at
    try:
        dt = datetime.datetime.fromisoformat(data[i]['created_at'])
        timestamp = int(dt.timestamp())
        informations['created_at'] = timestamp
    except TypeError:
        pass

    # status
    try:
        informations['status'] = data[i]['status']
    except TypeError:
        pass

    # addresses
    try:
        addresses = []
        network = data[i]['state']['network']
        for i in network:
            for k in network[i]['addresses']:
                addresses.append(k['address'])
        informations['addresses'] = addresses
    except TypeError:
        pass

    print(informations)
    print('\n')
