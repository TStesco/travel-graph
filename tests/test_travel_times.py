#!/bin/usr/python
import os
import googlemaps
import numpy as np
import pandas as pd
from Destination.Destination import Destination as dest
from datetime import datetime
from datetime import timedelta
import pytest

origins = [
    ("884 Kingston Rd, Toronto, ON", (43.6788473,-79.3048691)),
]

n = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
WEEK_START = n - timedelta(days=n.weekday()) + timedelta(weeks=1)

modes = ["driving", "walking", "transit", "bicycling"]
destinations = [
    dest(
        address="207 Queens Quay W, Toronto, ON M5J 1A7",
        arrival_datetime= WEEK_START + timedelta(days=1, hours=9),
        arrival_frequency=5*4+3,
        return_datetime= WEEK_START + timedelta(days=1, hours=19),
        return_frequency=5*4+3,
        modes=modes),
    dest(address="25 Dockside Dr, Toronto, ON M5A 1B6",
        arrival_datetime= WEEK_START + timedelta(days=1, hours=9),
        arrival_frequency=5*4+3,
        return_datetime= WEEK_START + timedelta(days=1, hours=19),
        return_frequency=5*4+3,
        modes=modes)
    ]

gmaps = googlemaps.Client(key=os.environ['GMAPS_API_KEY'])

def test_gmaps():
    '''
    Test demonstrating usage of Destination class and pandas.
    '''
    for d in destinations:
        if (d.arrival_datetime != 0) & (d.arrival_frequency != 0):
            for m in modes:
                matrix = gmaps.distance_matrix(
                    origins=origins[0][0],
                    destinations=d.address,
                    mode=m,
                    avoid="tolls",
                    units="metric",
                    arrival_time=d.arrival_datetime,
                    #traffic_model="best_guess"
                )
                d.arrival_distance_by[m] = matrix['rows'][0]['elements'][0]['distance']['value']
                d.arrival_duration_by[m] = matrix['rows'][0]['elements'][0]['duration']['value']
        if (d.return_datetime != 0) & (d.return_frequency != 0):
            for m in modes:
                matrix = gmaps.distance_matrix(
                    origins=origins[0][0],
                    destinations=d.address,
                    mode=m,
                    avoid="tolls",
                    units="metric",
                    arrival_time=d.arrival_datetime,
                    #traffic_model="best_guess"
                )
                d.return_distance_by[m] = matrix['rows'][0]['elements'][0]['distance']['value']
                d.return_duration_by[m] = matrix['rows'][0]['elements'][0]['duration']['value']
    d_list = []
    for d in destinations:
        dist_dict = {
            'origin': origins[0],
            'destination': d.address,
            'arrival_datetime': d.arrival_datetime,
            'arrival_frequency': d.arrival_frequency,
            'arrival_min_duration': min([d.arrival_duration_by[m] for m in modes]),
            'arrival_min_duration_no_car': min([d.arrival_duration_by[m] for m in modes if m != 'driving']),
            'return_datetime': d.return_datetime,
            'return_frequency': d.return_frequency,
            'return_min_duration': min([d.return_duration_by[m] for m in modes]),
            'return_min_duration_no_car': min([d.return_duration_by[m] for m in modes if m != 'driving']),
        }
        dist_dict.update({"arrival_distance_by_"+m: d.arrival_distance_by[m] for m in modes})
        dist_dict.update({"arrival_duration_by_"+m: d.arrival_duration_by[m] for m in modes})
        dist_dict.update({"return_distance_by_"+m: d.return_distance_by[m] for m in modes})
        dist_dict.update({"return_duration_by_"+m: d.return_duration_by[m] for m in modes})
        d_list.append(dist_dict)

    distances_df = pd.DataFrame(columns=d_list[0].keys())
    for d in d_list:
        distances_df = distances_df.append(d, ignore_index=True)
    
    # total with car
    # add extra time on each arrival on average for parking
    parking_factor = 60*5
    tot_with_car = (distances_df.arrival_frequency.values.transpose().dot(
        (distances_df.arrival_min_duration.values + parking_factor)) + \
    distances_df.return_frequency.values.transpose().dot(
        distances_df.return_min_duration.values)) / 3600.
    print("total travel duration with a car: %d".format(tot_with_car))
    # total without car
    tot_no_car = (distances_df.arrival_frequency.values.transpose().dot(
        distances_df.arrival_min_duration_no_car.values) + \
    distances_df.return_frequency.values.transpose().dot(
        distances_df.return_min_duration_no_car.values)) / 3600.
    print("total travel duration without a car: %d".format(tot_no_car))
