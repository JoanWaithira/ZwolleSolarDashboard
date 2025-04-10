
import streamlit as st
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
from folium import Map, GeoJson
from shapely.geometry import mapping
import streamlit_folium
import streamlit.components.v1 as components
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="District Overview", layout="wide", initial_sidebar_state="collapsed")

district = st.session_state.get("selected_district", None)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("assets/solar.jpg")

# --- HEADER ---
st.markdown(f"""
    <style>
        .figma-header {{
            background-color: #c8bab2;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0;
            margin-bottom: 2rem;
        }}
        .figma-header-left {{
            display: flex;
            align-items: center;
        }}
        .figma-solar-image {{
            width: 210px;
            height: 100%;
            object-fit: cover;
        }}
        .figma-title-block {{
            padding: 20px 40px;
            text-align: center;
            flex-grow: 1;
        }}
        .figma-title {{
            font-size: 24px;
            font-weight: bold;
            color: black;
            margin-bottom: 6px;
            font-family: Georgia, serif;
        }}
        .figma-subtitle {{
            font-size: 15px;
            font-style: italic;
            color: black;
        }}
        .figma-zwolle {{
            background-color: #3a65a8;
            color: white;
            padding: 15px 30px;
            font-weight: bold;
            font-size: 20px;
            font-family: Georgia, serif;
        }}
    </style>

    <div class="figma-header">
        <div class="figma-header-left">
            <img class="figma-solar-image" src="data:image/jpeg;base64,{img_base64}" alt="Solar Panel">
        </div>
        <div class="figma-title-block">
            <div class="figma-title">WELCOME TO THE ZWOLLE SOLAR DASHBOARD</div>
            <div class="figma-subtitle">Track, Simulate & Optimize Solar Energy in Your District</div>
        </div>
        <div class="figma-zwolle">Zwolle</div>
    </div>
""", unsafe_allow_html=True)

if not district:
    st.warning("District not found. Please go back and choose a valid district.")
    st.stop()

col_back, col_title = st.columns([0.3, 2])
with col_back:
    if st.button("⬅ GO BACK", key="back_button", help="Return to dashboard"):
        st.switch_page("./Home.py")

# --- MAIN PANEL ---
left_col, right_col = st.columns([1.5, 1])

# --- LEFT PANEL ---
with left_col:
    st.markdown(f"## Solar Energy flow in {district}")
    st.markdown("### Current Energy Situation")

    # CHART GRID (2x2)
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        components.html(open("current_energy_profile.html").read(), height=350, scrolling=False)
    with r1c2:
        components.html(open("current_gas_distribution.html").read(), height=350, scrolling=False)

    r2c1, r2c2 = st.columns(2)
    with r2c1:
        components.html(open("current_solar_distribution.html").read(), height=350, scrolling=False)
    with r2c2:
        components.html(open("current_grid_capacity.html").read(), height=350, scrolling=False)

    st.markdown("<div style='text-align: center; margin-top: 1.5rem;'>", unsafe_allow_html=True)
    if st.button("➡ GO TO SIMULATION", key="go_sim"):
        st.switch_page("pages/simulation.py")
    st.markdown("</div>", unsafe_allow_html=True)

# --- RIGHT PANEL ---
with right_col:
    st.markdown("### Map View")

    @st.cache_data
    def load_districts():
        return gpd.read_file("assets/Wijkgrenzen_Zwolle.shp").to_crs(epsg=4326)

    districts = load_districts()
    sel_geom = districts[districts["OMSCHR"] == district]
    centroid = sel_geom.geometry.centroid.iloc[0]
    fmap = Map(location=[centroid.y, centroid.x], zoom_start=13)
    geojson = GeoJson(data=mapping(sel_geom.geometry.iloc[0]), name=district, tooltip=district)
    geojson.add_to(fmap)

    streamlit_folium.st_folium(fmap, width=500, height=500)
