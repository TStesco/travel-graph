#!/bin/usr/python

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
        self.return_datetime = return_datetime
        self.return_frequency = return_frequency
        self.distance_by = {m: 0 for m in modes}
        self.duration_by = {m: 0 for m in modes}

    @property
    def pref_mode(self):
        return self._pref_mode
    

