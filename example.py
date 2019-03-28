#!/bin/usr/python
import os
from datetime import datetime
import responses
import googlemaps
from private import *
from code import interact


if __name__ == "__main__":
    for d in destinations:
        if (d.arrival_datetime != 0) & (d.arrival_frequency != 0):
            for m in modes:
                matrix = gmaps.distance_matrix(
                    origins=origins[0],
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
                    origins=origins[0],
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
    
    # total with car
    tot_with_car = (distances_df.arrival_frequency.values.transpose().dot(
        distances_df.arrival_min_duration.values) + \
        distances_df.return_frequency.values.transpose().dot(
            distances_df.return_min_duration.values)) / 3600.
    print("total travel duration with a car: %d".format(tot_with_car))
    tot_no_car = (distances_df.arrival_frequency.values.transpose().dot(
        distances_df.arrival_min_duration_no_car.values) + \
        distances_df.return_frequency.values.transpose().dot(
            distances_df.return_min_duration_no_car.values)) / 3600.
    print("total travel duration without a car: %d".format(tot_no_car))