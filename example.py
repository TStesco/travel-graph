#!/bin/usr/python
import os
from datetime import datetime
import responses
import googlemaps
from private import *
from code import interact


if __name__ == "__main__":

    gmaps = googlemaps.Client(key=key)
    for m in modes:
        for d in destinations:
            interact(local=dict(globals(), **locals()))
            matrix = gmaps.distance_matrix(
                origins=origins[0],
                destinations=d.address,
                mode=m,
                avoid="tolls",
                units="metric",
                #traffic_model="best_guess"
                )
            d.distance_by[m] = matrix['rows'][0]['elements'][0]['distance']['value']
            d.duration_by[m] = matrix['rows'][0]['elements'][0]['duration']['value']
        print(matrix['rows'][0]['elements'][0]['distance']['value'])
        print(matrix['rows'][0]['elements'][0]['duration']['value'])
    for d in destinations:
        
    # interact(local=dict(globals(), **locals()))
