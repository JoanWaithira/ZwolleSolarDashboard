# Solar Dashboard: Tracking, Simulating, and Optimizing Solar Energy in Zwolle

## Overview

The **Zwolle Solar Dashboard** is an interactive, district-level decision-support tool designed to guide Zwolle’s transition to solar energy. Developed as part of a climate transition intervention, it allows policymakers, planners, and cooperatives to monitor current energy trends and explore rooftop solar adoption scenarios. The dashboard supports Zwolle’s target of generating 201 GWh of solar electricity annually by 2030.

## Key Features

- **District-Level Visualization**  
  View current energy consumption (electricity and gas), existing solar generation, and grid load capacity for specific districts, starting with Stadshagen.

- **Scenario-Based Simulation**  
  Simulate solar adoption scenarios based on:
  - Building type (residential, industrial, other, large roofs)
  - Roof suitability (Level 1–3)
  - Adoption rate (25%–100%)

- **Energy Generation & ROI Estimates**  
  Calculate potential solar output, number of panels, storage needs, and investment costs.

- **Economic Feasibility Analysis**  
  Estimate payback periods for solar panels and battery storage systems using Dutch-specific financial tools:
  - [BerekenHet.nl](https://www.berekenhet.nl)
  - [Jeroen.nl](https://jeroen.nl/over/thuisbatterijen)

- **Governance and Policy Integration**  
  Designed in consultation with local stakeholders, including the Municipality of Zwolle and energy cooperative Blauwvinger Energie.

## Repository Contents

- `/Solar Dashboard_Streamlit/`: Main Streamlit application files
- `/All Data/`: Processed geospatial and statistical datasets
- `simulation.html`: Energy and storage modeling outputs (visual)
- `README.md`: This file


## In order to get started, follow the steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/JoanWaithira/ZwolleSolarDashboard.git
   cd ZwolleSolarDashboard
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   streamlit run Solar\ Dashboard_Streamlit/app.py
   ```

## Data Sources

- **Geospatial Data**: Zwolle building footprints and roof suitability (ITC Disc Lab)
- **Energy Data**: Enexis (grid and solar generation), CBS (consumption)
- **Solar Simulation**: [PVGIS](https://ec.europa.eu/jrc/en/pvgis) by the European Commission
- **Grid Capacity**: Netbeheer Nederland’s Capacity Map

## Current Focus Area: Stadshagen

The prototype implementation focuses on the Stadshagen district, analyzing:
- Energy consumption and solar potential
- Grid capacity limitations
- Residential adoption patterns and payback scenarios

## Roadmap

- [ ] Expand to neighborhood (buurt) level analysis using CBS buurt data
- [ ] Enable district stacking to simulate municipality-wide solar impact
- [ ] Integrate simulation of large-scale solar/wind farm projects
- [ ] Allow energy cooperatives to upload and test their own data

## Governance & Stakeholder Alignment

The dashboard is envisioned as a **planning and communication tool** embedded in Zwolle's annual climate strategy cycle. It facilitates participatory governance, evidence-based policy development, and transparent monitoring of energy transition progress.

## Prototype from Streamlit --> Still under development
https://solardashboard-si69kaz8mv5oypzjbxabny.streamlit.app/


## Contact

For questions or collaboration:  
📧 [joanwaithira.jw@gmail.com](mailto:joanwaithira.jw@gmail.com)  
🔗 [GitHub Repository](https://github.com/JoanWaithira/ZwolleSolarDashboard)