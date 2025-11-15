import googlemaps
import folium
import webbrowser
from datetime import datetime
from googlemaps.convert import decode_polyline



API_KEY = "AIzaSyBJvLf7ELmjeX6KSmaGHHi2-Ks1QBkWWR0"
gmaps = googlemaps.Client(key=API_KEY)

def generate_route(origin, destination, open_map=True):
    import googlemaps, folium, webbrowser

    gmaps = googlemaps.Client(key=API_KEY)

    # Fetch multiple alternative routes
    directions = gmaps.directions(origin, destination, mode="driving", alternatives=True)

    # Create map
    origin_coords = gmaps.geocode(origin)[0]['geometry']['location']
    m = folium.Map(location=[origin_coords['lat'], origin_coords['lng']], zoom_start=12)
    # 🔹 Add start marker
    folium.Marker(
    location=[origin_coords['lat'], origin_coords['lng']],
    popup="Start: " + origin,
    icon=folium.Icon(color="green", icon="play")
                    ).add_to(m)

# 🔹 Add destination marker
    destination_coords = gmaps.geocode(destination)[0]['geometry']['location']
    folium.Marker(
    location=[destination_coords['lat'], destination_coords['lng']],
    popup="Destination: " + destination,
    icon=folium.Icon(color="red", icon="flag")
                    ).add_to(m)


    route_details = []  # store route info

    for i, route in enumerate(directions):
        leg = route["legs"][0]
        distance_text = leg["distance"]["text"]
        distance_value = leg["distance"]["value"]
        duration_text = leg["duration"]["text"]
        duration_value = leg["duration"]["value"]

    # 🧠 Determine color
        if duration_value > 3600 or distance_value > 25000:
            color = "#FF4B4B"
            color_name = "Red"
        elif duration_value > 1800:
            color = "#125297"
            color_name = "Blue"
        else:
            color = "#06A022"
            color_name = "Green"

    # Decode polyline
        points = []
        for step in leg["steps"]:
            decoded_points = decode_polyline(step["polyline"]["points"])
            points.extend([(p["lat"], p["lng"]) for p in decoded_points])

        folium.PolyLine(
            locations=points,
            color=color,
            weight=8 if color_name == "Green" else 6,
            opacity=0.8,
            tooltip=f"{color_name} Route → {distance_text}, {duration_text}"
                        ).add_to(m)

    # 🚫 Skip duplicate entries
        if any(r["Distance"] == distance_text and r["Time"] == duration_text for r in route_details):
                continue

        route_details.append({
        "Route": f"Route {i+1}",
        "Distance": distance_text,
        "Time": duration_text,
        "Color": color_name
    })



    map_file = "real_route_map.html"
    m.save(map_file)
    
    if open_map:
        webbrowser.open(map_file)
    # Avoid duplicate route entries

    return map_file, route_details



# --- Only run this if script is executed directly ---
if __name__ == "__main__":
    origin = input("Enter your start location: ")
    destination = input("Enter your destination: ")
    generate_route(origin, destination)
