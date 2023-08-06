#!/usr/bin/env python

from enum import Enum


class RouteMode(Enum):
    """Modes which is used in routing api functions."""

    fastest = 'fastest'
    shortest = 'shortest'
    balanced = 'balanced'
    bicycle = 'bicycle'
    car = 'car'
    car_hov = 'carHOV'
    traffic_enabled = 'traffic:enabled'
    traffic_disabled = 'traffic:disabled'
    traffic_default = 'traffic:default'
    enabled = 'enabled'
    pedestrian = 'pedestrian'
    publicTransport = 'publicTransport'
    publicTransportTimeTable = 'publicTransportTimeTable'
    truck = 'truck'

    def __str__(self):
        return '%s' % self._value_

class MatrixSummaryAttribute(Enum):
    """Defines an attribute to be included in the route matrix entries"""

    travel_time = 'traveltime'
    cost_factor = 'costfactor'
    distance = 'distance'
    route_id = 'routeid'

    def __str__(self):
        return '%s' % self._value_

class PlacesCategory(Enum):
    """Categories which are used in places api functions."""

    accomodation = 'accomodation'
    administrative_areas_buildings = 'administrative-areas-buildings'
    airport = 'airport'
    atm_bank_exchange = 'atm-bank-exchange'
    coffee_tea = 'coffee-tea'
    eat_drink = 'eat-drink'
    going_out = 'going-out'
    hospital_health_care_facility = 'hospital-health-care-facility'
    leisure_outdoor = 'leisure-outdoor'
    natural_geographical = 'natural-geographical'
    petrol_station = 'petrol-station'
    restaurant = 'restaurant'
    snacks_fast_food = 'snacks-fast-food'
    sights_museums = 'sights-museums'
    shopping = 'shopping'
    toilet_rest_area = 'toilet-rest-area'
    transport = 'transport'

    def __str__(self):
        return '%s' % self._value_

class PublicTransitSearchMethod(Enum):
    """Search methods used in public transit search function"""

    fuzzy = 'fuzzy'
    strict = 'strict'

    def __str__(self):
        return '%s' % self._value_

class PublicTransitRoutingType(Enum):
    """Routing types used in public transit api"""

    time_tabled = 'tt'
    simple = 'sr'
    all = 'all'

    def __str__(self):
        return '%s' % self._value_
    
class WeatherProductType(Enum):
    """Identifis the type of report to obtain."""

    observation = 'observation'
    forecast_7days = 'forecast_7days'
    forecast_7days_simple = 'forecast_7days_simple'
    forecast_hourly = 'forecast_hourly'
    forecast_astronomy = 'forecast_astronomy'
    alerts = 'alerts'
    nws_alerts = 'nws_alerts'

    def __str__(self):
        return '%s' % self._value_
