# Create hardiness zone
import requests

ARCGIS_GEOCODE_URL = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates'
ARCGIS_URL_CANADA = 'https://services3.arcgis.com/vq5vGR4r1YX7ueLg/arcgis/rest/services/ZonesDeRusticite_SHP_FR/FeatureServer'
ARCGIS_URL_USA = 'https://services1.arcgis.com/rKbpcgHXWYYaP4pQ/arcgis/rest/services/phzm_us_zones_shp_2023_view/FeatureServer'

canadian_provinces = {"alberta", "british columbia", "manitoba", "new brunswick", 
                      "newfoundland and labrador", "northwest territories", "nova scotia", "nunavut", 
                      "ontario", "prince edward island", "quebec", "saskatchewan", "yukon"}

def is_canada(state):
    return state.lower() in canadian_provinces

def get_country(input_state):
    layer_url = ""
    if is_canada(input_state):
        layer_url = ARCGIS_URL_CANADA
    else:
        layer_url = ARCGIS_URL_USA
    return layer_url    

def get_coordinates(city, state):
    """Convert city name to lat/lon using ArcGIS geocoder."""
    passing_string = city + ", " + state
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

def get_hardiness_zone(lon, lat, state):
    country_field_name = ""
    if is_canada(state):
        country_field_name = "ph_zone"
    else:
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
    layer_url = get_country(state)
    response = requests.get(layer_url + "/0/query", params=params)
    data = response.json()
    if data.get("features"):
        return data["features"][0]["attributes"][country_field_name]
    return "not found"

def hardiness_zone(city, state):
    lon, lat = get_coordinates(city, state)
    if lat is None or lon is None:
        return "NO"
    else: 
        zone = get_hardiness_zone(lon, lat, state)
        return zone