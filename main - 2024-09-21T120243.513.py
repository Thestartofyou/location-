import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt

# Function to get latitude and longitude of a location
def get_lat_lon(location_name):
    geolocator = Nominatim(user_agent="route_finder")
    location = geolocator.geocode(location_name)
    return (location.latitude, location.longitude)

# Function to plot the fastest route between two locations
def plot_fastest_route(start_loc, end_loc, travel_mode='drive'):
    # Get latitude and longitude for start and end locations
    start_point = get_lat_lon(start_loc)
    end_point = get_lat_lon(end_loc)
    
    # Download the graph for the area
    G = ox.graph_from_point(start_point, dist=5000, network_type=travel_mode)

    # Find the nearest nodes to the start and end points
    start_node = ox.distance.nearest_nodes(G, start_point[1], start_point[0])
    end_node = ox.distance.nearest_nodes(G, end_point[1], end_point[0])

    # Find the shortest path based on travel time or distance
    route = nx.shortest_path(G, start_node, end_node, weight='length')

    # Plot the route on the map
    fig, ax = ox.plot_graph_route(G, route, route_linewidth=3, node_size=0, bgcolor='k')
    plt.show()

# Example Usage:
start_location = "Boston, MA"
end_location = "New York, NY"

plot_fastest_route(start_location, end_location, travel_mode='drive')
