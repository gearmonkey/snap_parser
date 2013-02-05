"""
parse the Stanford beer data (from http://snap.stanford.edu/data/web-BeerAdvocate.html)
and shove it in an sqlitedb
"""

import sys, os
import sqlite3

infile = sys.argv[1]
outfile = sys.argv[2]

rh = open(infile)

beers = {}
current_id = None
this_beer = {}
for line in rh:
    if line == '\n':
        if current_id != None:
            if current_id in beers.keys():
                beers[current_id][ratings].append(this_beer[ratings])
                beers[current_id][mean_rating] = sum(beers[current_id][ratings])/ \
                                                  float(len(beers[current_id][ratings]))
                print 'new rating for', this_beer['name']
            else:
                beers[current_id] = this_beer
                beers[current_id][mean_rating] = beers[current_id][ratings]
                print 'added', this_beer['name']
                
        current_id = None
        this_beer = {}
        continue
    key, value = line.strip().split(': ')
    toplabel, sublabel = key.split('/')
    if toplabel == 'beer'
        if sublabel == 'name':
            this_beer['name'] = value
        elif sublabel == 'beerID':
            this_beer['beerID'] = int(value)
        elif sublabel == 'brewerId':
            this_beer['brewerID'] = int(value)
        elif sublabel == 'ABV':
            this_beer['ABV'] = float(value)
        elif sublabel == 'style':
            this_beer['style'] = value
    elif toplabel == 'review':
        if sublabel == 'overall':
            this_beer['ratings'] = [float(value)]

#now doing some with the beers dict

