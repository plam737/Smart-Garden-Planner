# Create hardiness zone
import requests

ARCGIS_GEOCODE_URL = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates'
ARCGIS_URL_USA = 'https://services1.arcgis.com/rKbpcgHXWYYaP4pQ/arcgis/rest/services/phzm_us_zones_shp_2023_view/FeatureServer'

def get_coordinates(city):
    """Convert city name to lat/lon using ArcGIS geocoder."""
    passing_string = city + ", California"
    params = {
        "singleLine": passing_string,
        "outFields": "location",
        "f": "json"
    }
    response = requests.get(ARCGIS_GEOCODE_URL, params=params)
    data = response.json()

    if data["candidates"]:
        location = data["candidates"][0]["location"]
        return location["x"], location["y"]  # lon, lat
    return None, None

def get_hardiness_zone(lon, lat):
    country_field_name = "zone" 
    params = {
        "geometry": f"{lon},{lat}",
        "geometryType": "esriGeometryPoint",
        "spatialRel": "esriSpatialRelIntersects",
        "inSR": "4326",
        "outFields": country_field_name,
        "returnGeometry": "false",
        "f": "json"
    }   
    layer_url = ARCGIS_URL_USA
    response = requests.get(layer_url + "/0/query", params=params)
    data = response.json()
    if data.get("features"):
        return data["features"][0]["attributes"][country_field_name]
    return "not found"

def hardiness_zone(city):
    lon, lat = get_coordinates(city)
    if lat is None or lon is None:
        return "NO"
    else: 
        zone = get_hardiness_zone(lon, lat)
        return zone