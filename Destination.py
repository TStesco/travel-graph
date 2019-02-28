#!/bin/usr/python

class Destination:
	"""
	:param distance_by: dict with keys of transportation modes of distances from origin in meters (m)
	:type: dict

	:param: duration_by: dict with keys of transportation modes of durations from origin in seconds (s)
	:type: dict
	"""
	def __init__(self, address, arrival_datetimes, frequency, modes):
		self.address = address
		self.arrival_datetimes = arrival_datetimes
		self.frequency = frequency
		self.distance_by = {m: 0 for m in modes}
		self.duration_by = {m: 0 for m in modes}

	@property
	def pref_mode(self):
		return self._pref_mode
	

