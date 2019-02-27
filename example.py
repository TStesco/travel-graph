#!/bin/usr/python
import os
from datetime import datetime
import responses
import googlemaps
from private import *
from code import interact

if __name__ == "__main__":

	gmaps = googlemaps.Client(key=key)

	matrix = gmaps.distance_matrix(
		origins=origins,
		destinations=destinations,
		mode="transit",
		avoid="tolls",
		units="metric",
		traffic_model="best_guess"
		)

	interact(local=dict(globals(), **locals()))