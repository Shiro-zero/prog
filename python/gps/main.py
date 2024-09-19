from geopy.geocoders import Nominatim
import folium
from IPython.display import display, HTML

def get_location(address):
    # Initialize the geolocator
    geolocator = Nominatim(user_agent="gps_example")
    
    # Get location
    location = geolocator.geocode(address)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None

def create_map(latitude, longitude):
    # Create a map centered around the latitude and longitude
    map_ = folium.Map(location=[latitude, longitude], zoom_start=15)
    
    # Add a marker for the location
    folium.Marker(
        location=[latitude, longitude],
        popup="Your location",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(map_)
    
    return map_

def display_map(map_):
    # Convert the map to HTML and display it in the notebook
    map_html = map_._repr_html_()
    display(HTML(map_html))

# Example usage
address = input("Enter the address or place: ")
location = get_location(address)

if location:
    latitude, longitude = location
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    
    # Create and display the map
    map_ = create_map(latitude, longitude)
    display_map(map_)
else:
    print("Location not found!")
