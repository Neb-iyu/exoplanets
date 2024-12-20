import csv
from flask import jsonify
def load_data(directory):
    """
    Load data from csv file
    """
    with open(f"{directory}/exoplanets.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = {}
        columns = reader.fieldnames
        for planet in reader:
            bf = {}
            for fieldname in columns:
                bf[fieldname] = planet[fieldname]
            id = int(planet[columns[0]])
            data[id] = bf
    return [data, columns]

def binary_search(data, query):
    i, j = 0, len(data)
    x = sorted(data, key=lambda d:data[type])

def look_up(data, query, id=False):
    x = []
    if id == True:
        query = int(query)
        return data[query]
    for id in data:
        planet = data[id]
        if query in planet['pl_name']: #or query in planet['hostname'] or query in planet['discoverymethod'] or query in planet['disc_year'] or query in planet['disc_facility']:
            x.append(planet)
    
    return x

def link(l):
    for i in range(len(l)):
        if l[i:i+5] == 'https':
            for j in range(i+4, len(l)):
                if l[j] == ' ':
                    return l[i:j-1]
    return 'h'
                

    