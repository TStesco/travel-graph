# travel-graph

Uses googlemaps distance-matrix API to determine the location score of a specific location based on the weighted travel time to any number of locations.

## install

```bash
git clone https://github.com/TStesco/travel-graph.git
cd travel-graph
conda create -f environment.yml
```

## weighting

TODO

## origins and destinations

These are not commited and kept in private.py, which can be imported.
The contents of private.py are similar to as follows:

```python
key="1234"
origins=["200 University Ave W, Waterloo, ON N2L 3G1"]
destinations=[
	"Union Station, Front Street West, Toronto, ON",
	"27 King's College Cir, Toronto, ON M5S"]
```