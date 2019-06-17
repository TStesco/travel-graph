#!/bin/usr/python
import numpy as np

class Destination:
    """
    :param distance_by: dict with keys of transportation modes of distances from origin in meters (m)
    :type: dict

    :param: duration_by: dict with keys of transportation modes of durations from origin in seconds (s)
    :type: dict
    """
    def __init__(self, address, arrival_datetime, arrival_frequency, return_datetime, return_frequency, modes):
        self.address = address
        self.arrival_datetime = arrival_datetime
        self.arrival_frequency = arrival_frequency
        self.arrival_distance_by = {m: 0 for m in modes}
        self.arrival_duration_by = {m: 0 for m in modes}
        self.return_datetime = return_datetime
        self.return_frequency = return_frequency
        self.return_distance_by = {m: 0 for m in modes}
        self.return_duration_by = {m: 0 for m in modes}

    @property
    def pref_mode(self):
        return self._pref_mode

    def distance_score(d):
        return (2 / (1 + np.exp(-d/(dist_10_mins_walk/10)+10)))*(np.exp(-d/dist_10_mins_walk)) + (1 - 1 / (1 + np.exp(-d/(dist_10_mins_walk/10)+10)))

    def haversine_np(lon1, lat1, lon2, lat2):
        """
        Calculate the distance between two points on the earth surface.
        All args must be of equal length.
        """
        
        lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

        c = 2 * np.arcsin(np.sqrt(a))
        # See https://www.maps.ie/coordinates.html and https://www.toronto.ca/311/knowledgebase/kb/docs/articles/information-and-technology/solutions-development/geospatial-competency-centre/torontos-elevationaltitude-above-sea-level.html
        # https://rechneronline.de/earth-radius/
        km = 6368.095 * c
        meters = km*1000.
        return meters
    

