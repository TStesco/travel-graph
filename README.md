# travel-graph

Uses googlemaps distance-matrix API to determine the location score of a specific location based on the weighted travel time to any number of locations with best guess travel time in traffic.

## API Pricing

### SKU: Distance Matrix Advanced

With free tier ($200 credit per month) thats up to 20,000 calls at 0.01 USD / call (see https://developers.google.com/maps/billing/understanding-cost-of-use#distance-matrix-advanced).

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