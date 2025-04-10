import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Run Simulation", layout="wide", initial_sidebar_state="collapsed")

# --- Get Scenario and District ---
scenario = st.session_state.get("scenario", "Unknown Scenario")
district = st.session_state.get("selected_district", "Unknown District")

# --- Load header image ---
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

        /* Panel Styling */
        .panel {{
            background-color: #ececec;
            padding: 30px;
            border-radius: 25px;
            font-family: Georgia, serif;
        }}

        /* Yellow buttons */
        .yellow-btn > button {{
            background-color: #ffdd57;
            color: black;
            font-weight: bold;
            border-radius: 30px;
            padding: 12px 24px;
            font-size: 16px;
            font-family: Georgia, serif;
            border: none;
        }}

        .yellow-btn > button:hover {{
            background-color: #f7cd45;
            transform: scale(1.01);
        }}

        .stRadio > div, .stMultiSelect > div {{
            background-color: transparent;
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

# --- LAYOUT ---
col_left, col_right = st.columns(2)

# --- LEFT PANEL ---
with col_left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(f"### Scenario Two: {scenario} L.U")
    st.write(
        f"""
        This scenario analyzes solar energy integration in residential areas.  
        It evaluates factors like rooftop solar feasibility, energy savings  
        for homeowners, and potential grid contributions from small-scale  
        solar panel systems on houses and apartment buildings.
        """
    )

    with st.container():
        if st.button("CHOOSE ANOTHER SCENARIO", key="back", type="primary"):
            st.switch_page("pages/simulation.py")
        st.markdown("""
            <style>
                .stButton > button {{
                    background-color: #ffdd57;
                    color: black;
                    font-weight: bold;
                    border-radius: 30px;
                    padding: 12px 24px;
                    font-size: 16px;
                    border: none;
                    font-family: Georgia, serif;
                    margin-top: 20px;
                }}
                .stButton > button:hover {{
                    background-color: #f7cd45;
                    transform: scale(1.01);
                }}
            </style>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT PANEL ---
with col_right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("### Roof Suitability Level")
    roof_levels = st.multiselect(
        label="",
        options=["Level 1", "Level 2", "Level 3"],
        default=["Level 1"]
    )

    st.markdown("### Percentage of Roofs")
    roof_percentage = st.radio(
        label="",
        options=["25%", "50%", "75%", "100%"],
        index=1,
        horizontal=False
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Run button
    run_btn = st.button("RUN SIMULATION")
    st.markdown("""
        <style>
            .stButton > button {{
                background-color: #ffdd57;
                color: black;
                font-weight: bold;
                border-radius: 30px;
                padding: 12px 24px;
                font-size: 16px;
                border: none;
                font-family: Georgia, serif;
            }}
            .stButton > button:hover {{
                background-color: #f7cd45;
                transform: scale(1.01);
            }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if run_btn:
        st.session_state["roof_percentage"] = roof_percentage
        st.session_state["roof_levels"] = roof_levels
        st.success(f"Running simulation for **{scenario}** in **{district}** with {roof_percentage} roof coverage...")
        st.switch_page("pages/runit.py")
