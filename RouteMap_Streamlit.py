import streamlit as st
import time
import RouteMap
import streamlit as st
import login_page  # our login system
from safety_score import safety_score

# If user isn't logged in yet — show login/signup page first



# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="LuminaRoute", page_icon="🛡️", layout="wide")
st.markdown("""
<div style='text-align:center; padding:30px; background:linear-gradient(90deg,#0a192f,#122c56); border-radius:15px;'>
    <h1 style='color:#64ffda; font-size:45px;'>🌙 LuminaRoute</h1>
    <p style='color:#b3cde0; font-size:18px;'>
    Navigate confidently — find the <b>safest</b> path, not just the shortest.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 10% 20%, #0a192f 0%, #122c56 90%);
}
.stCard {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 10px rgba(100,255,218,0.2);
    margin: 10px;
}
h2 {
    color: #64ffda;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='stCard'><h2>Smart Safety Index</h2><p>Score each route based on real-time data.</p></div>", unsafe_allow_html=True)

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0a192f, #122c56);
    color: #f8f9fa;
}
h1, h2, h3 {
    color: #64ffda;
}
.stButton>button {
    background-color: #64ffda;
    color: #0a192f;
    font-weight: 600;
    border-radius: 10px;
}
div[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
# ---------- SIDEBAR ----------
st.sidebar.markdown("""
<style>
/* Sidebar Background */
div[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a192f 0%, #112d4e 100%);
    color: #ccd6f6;
    padding-top: 1rem;
}

/* Sidebar Title */
.sidebar-title {
    font-size: 22px;
    color: #5eead4;  /* soft teal */
    text-align: center;
    font-weight: 700;
    margin-bottom: 15px;
}

/* Labels */
.sidebar-label {
    color: #80ed99;  /* gentle mint green */
    font-weight: 600;
    font-size: 15px;
    margin-top: 20px;      /* added spacing ABOVE input box */
    margin-bottom: 6px;    /* added spacing BELOW label */
    display: block;
}

/* Input Boxes */
input[type="text"], select {
    margin-top: 4px;
    margin-bottom: 14px;
    border-radius: 8px;
}

/* Buttons */
.stButton>button {
    background-color: #5eead4 !important;
    color: #0a192f !important;
    font-weight: 600;
    border-radius: 10px;
    width: 100%;
    margin-top: 15px;
    margin-bottom: 15px;
    box-shadow: 0 0 10px rgba(94,234,212,0.4);
    transition: 0.2s ease;
}
.stButton>button:hover {
    background-color: #3ce3c0 !important;
    box-shadow: 0 0 20px rgba(94,234,212,0.6);
}

/* Metrics */
.metric-box {
    text-align: center;
    background-color: rgba(255,255,255,0.07);
    padding: 8px;
    border-radius: 8px;
    margin-top: 10px;
}
.metric-label {
    color: #a8b2d1;
    font-size: 13px;
}
.metric-value {
    color: #5eead4;
    font-size: 20px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Title
st.sidebar.markdown("<div class='sidebar-title'>🧭 LuminaRoute Panel</div>", unsafe_allow_html=True)

# Input Fields (with better spacing)
st.sidebar.markdown("<span class='sidebar-label'>Start Location</span>", unsafe_allow_html=True)
origin = st.sidebar.text_input("Start Location", "Malkajgiri, Hyderabad")

st.sidebar.markdown("<span class='sidebar-label'>Destination</span>", unsafe_allow_html=True)
destination = st.sidebar.text_input("Destination", "Tellapur, Hyderabad")

mode = st.sidebar.selectbox("Travel Mode", ["Driving", "Walking", "Transit"])

# Action Button
if st.sidebar.button("🚀 Find Safest Routes"):
    with st.spinner('🛰️ Calculating safest routes...'):
        if not origin or not destination:
            st.error("Please enter both origin and destination!")
        else:
            map_file, route_details = RouteMap.generate_route(origin, destination, open_map=False)
            st.success("Routes generated successfully!")
            with open(map_file, "r", encoding="utf-8") as f:
                map_html = f.read()
            st.components.v1.html(map_html, height=600)
            st.subheader("Route Details")
            import pandas as pd
            df = pd.DataFrame(route_details)
            st.dataframe(df, use_container_width=True)

# Sidebar Metrics
st.sidebar.markdown("---")
st.sidebar.markdown("### Safety Overview")
st.sidebar.markdown("<div class='metric-box'><div class='metric-label'>Average Safety</div><div class='metric-value'>82 / 100</div></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='metric-box'><div class='metric-label'>Risk Level</div><div class='metric-value'>🟢 Low</div></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='metric-box'><div class='metric-label'>Weather</div><div class='metric-value'>☀️ Clear</div></div>", unsafe_allow_html=True)

# Footer
st.sidebar.markdown("<hr style='border: 1px solid #233554;'>", unsafe_allow_html=True)
st.sidebar.markdown("<center style='font-size:13px; color:#8892b0;'>Made by <b>Team VidyutCoders</b></center>", unsafe_allow_html=True)

# ---------- MAIN SECTION ----------
with st.spinner('🛰️ Calculating safest routes...'):
    time.sleep(2)
    map_file, route_details = RouteMap.generate_route(origin, destination, open_map=False)

st.markdown("<hr style='border: 2px solid #64ffda; border-radius: 5px;'>", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #64ffda; font-size: 48px; margin-bottom: 0;'>LuminaRoute</h1>
        <p style='color: #b3cde0; font-size: 18px;'>Your AI-driven Nighttime Travel Companion for Safe Navigation ✨</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex; justify-content:center; margin-top:20px;">
    <div style="margin:0 20px; color:#00FF7F;">🟩 Green: Recommended route</div>
    <div style="margin:0 20px; color:#007BFF;">🟦 Blue: Possible but slower</div>
    <div style="margin:0 20px; color:#FF4B4B;">🟥 Red: Heavy or unsafe route</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## Route Safety Overview")
st.sidebar.metric("Average Safety", "82 / 100", "Good 👍")
st.sidebar.metric("Estimated Risk", "Low", "🟢")

# Tech Stack Section
st.markdown("<hr style='border: 1px solid #233554; margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("""
<div style="margin-top: 20px;">
    <h2 style="color:#64ffda;">Tech Stack</h2>
    <ul style="color:#dee3ea; font-size:17px;">
        <li><b>Languages:</b> Python, HTML, CSS</li>
        <li><b>APIs:</b> Google Maps Directions, Geocoding</li>
        <li><b>Libraries:</b> Streamlit, Folium, Pandas, Requests</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Future Enhancements
st.markdown("<hr style='border: 1px solid #233554; margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("""
<div style="margin-top: 20px;">
    <h2 style="color:#64ffda;">Future Enhancements</h2>
    <ul style="color:#dee3ea; font-size:17px;">
        <li>Integrate <b>real-time lighting, weather, and crime data</b> for safety analytics.</li>
        <li>Add <b>voice-based SOS alerts</b> and emergency contact triggers.</li>
        <li>Launch a <b>mobile-friendly version</b> powered by Streamlit Cloud.</li>
    </ul>
</div>
""", unsafe_allow_html=True)




# ---------- FEATURE CARDS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Smart Safety Index")
    st.write("Each route is scored (0–100) for real-time safety using accident and lighting data.")

with col2:
    st.markdown("### Multi-Route Comparison")
    st.write("Displays fastest, shortest, and safest routes simultaneously with color codes.")

with col3:
    st.markdown("### Realtime Alerts")
    st.write("Warns when approaching unsafe zones or dark roads during travel.")




# ---------- FOOTER ----------
st.divider()
st.markdown(
    "<center>Made with ❤️ by <b>Team VidyutCoders</b> | Hackathon 2025</center>",
    unsafe_allow_html=True,
)



