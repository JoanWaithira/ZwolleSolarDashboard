# Solar Dashboard

## Overview
The **Solar Dashboard** is an interactive web-based tool designed to visualize and analyze the transition to solar energy in Zwolle. It provides insights into energy generation potential, adoption scenarios, and their impact on the local power grid.

## Features
- **Scenario Modeling**: Compare different solar adoption levels (all roofs, partial adoption, no adoption).
- **Geospatial Visualization**: Interactive map displaying solar panel distribution and energy output.
- **Real-time Data Integration**: Pulls live data on weather, solar radiation, and grid load.
- **Stakeholder Insights**: Identifies key players, including policymakers, businesses, and residents.
- **Energy Impact Analysis**: Calculates potential energy savings and CO₂ reductions.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js & npm
- PostgreSQL (for spatial data)

### Setup Instructions
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/solardashboard.git
   cd solardashboard
   ```

2. **Backend Setup**
   ```sh
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend Setup**
   ```sh
   cd ../frontend
   npm install
   npm start
   ```

## Usage
1. Open `http://localhost:3000` in your browser.
2. Select a scenario to visualize solar energy adoption.
3. Explore geospatial data and impact reports.

## Data Sources
- OpenStreetMap (for building footprints)
- KNMI (for weather and solar radiation data)
- Local government datasets (for energy policies and incentives)

## Roadmap
- [ ] Implement machine learning predictions for future solar adoption trends
- [ ] Add battery storage modeling
- [ ] Improve UI with more interactive features

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For questions or feedback, reach out via [email](mailto:joanwaithira.jw@gmail.com) or open an issue on GitHub.


