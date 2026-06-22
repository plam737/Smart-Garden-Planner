# Create hardiness zone
import requests

ARCGIS_URL_CANADA = 'https://services3.arcgis.com/vq5vGR4r1YX7ueLg/arcgis/rest/services/ZonesDeRusticite_SHP_FR/FeatureServer'
ARCGIS_URL_USA = 'https://services1.arcgis.com/rKbpcgHXWYYaP4pQ/arcgis/rest/services/phzm_us_zones_shp_2023_view/FeatureServer'

canadian_provinces = {"alberta", "british columbia", "manitoba", "new brunswick", 
                      "newfoundland and labrador", "northwest territories", "nova scotia", "nunavut", 
                      "ontario", "prince edward island", "quebec", "saskatchewan", "yukon"}

def is_canada(state):
    return state.lower() in canadian_provinces

if is_canada(input_state):
    layer_url = ARCGIS_URL_CANADA
else:
    layer_url = ARCGIS_URL_USA

def get_coordinates(city):
    """Convert city name to lat/lon using ArcGIS geocoder."""
    params = {
        "singleLine": city,
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
    """Query your AGOL feature layer with a spatial filter."""
    params = {
        "geometry": f"{lon},{lat}",
        "geometryType": "esriGeometryPoint",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "zone",        # match your layer's field name
        "returnGeometry": "false",
        "f": "json"
    }
    response = requests.get(YOUR_FEATURE_LAYER_URL, params=params)
    data = response.json()

    if data.get("features"):
        return data["features"][0]["attributes"]["zone"]
    return "Zone not found"