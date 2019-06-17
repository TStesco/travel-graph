# travel-graph

Uses googlemaps distance-matrix API to determine the location score of a specific location based on the weighted travel time to any number of locations with best guess travel time in traffic.


## install

Requires pipenv: https://docs.pipenv.org/en/latest
Requires google maps `Distance Matrix` API key: https://cloud.google.com/maps-platform/routes/?apis=routes


```bash
git clone https://github.com/TStesco/travel-graph.git
cd travel-graph
pipenv install
export GMAPS_API_KEY=$YOUR_API_KEY
```

## Run tests

Requires circleci local cli: https://circleci.com/docs/2.0/local-cli/#installation

```
cd travel-graph
circleci local execute --job build -e GMAPS_API_KEY=$GMAPS_API_KEY
```

## Getting Started

Take a look at `test_travel_times.py`, it demonstrates how this module should be used.

## API Pricing

### Google Maps - Distance Matrix Advanced

With free tier ($200 credit per month) thats up to 20,000 calls at 0.01 USD / call (see https://developers.google.com/maps/billing/understanding-cost-of-use#distance-matrix-advanced).