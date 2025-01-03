# Carbon Emission Calculator

The **Carbon Emission Calculator** is a web application designed to assess the carbon footprint of laptops within an organization. The project involves a comprehensive software solution that integrates backend APIs, a user-friendly interface, and efficient data storage. Built using **Django**, **Docker**, **Postgres**, and **Python**, this application streamlines the process of calculating CO2 emissions based on battery report data.

## Features
- **Backend Development with REST APIs:** Developed robust APIs in Django for data processing, calculation, and integration.
- **Automated Battery Report Collection:** Automated the gathering of battery report data from laptops using Python scripts.
- **Carbon Emission Analysis:** Calculates the power consumed and the corresponding carbon emissions from laptops based on battery report data.
- **User-Friendly Interface:** A web interface where users can:
  - Upload battery reports.
  - View power consumption and carbon emission statistics.
  - Store data in a **Postgres** database for future reference, eliminating the need to re-upload reports.
- **Dockerized Application:** Ensures seamless deployment and environment consistency using Docker.

## Workflow
1. **Battery Report Upload:** Users upload battery reports through the web interface.
2. **Data Processing:** Backend APIs process the uploaded reports to calculate power consumption and carbon emissions.
3. **Results Display:** The web interface displays the calculated metrics to the user.
4. **Data Storage:** The processed data is stored in a Postgres database, ensuring it is accessible for future reference without needing to re-upload the reports.

## Technologies Used
- **Python:** Core programming language for automation and backend logic.
- **Django:** Framework for building the REST APIs and backend architecture.
- **Postgres:** Database for securely storing battery report and emission data.
- **Docker:** For containerization and consistent environment setup.
- **REST API:** To handle data transfer between the backend and frontend.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/carbon-emission-calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd carbon-emission-calculator
   ```

3. Start the application using Docker:
   ```bash
   docker-compose up --build
   ```

4. Access the application at:
   ```
   http://localhost:8000
   ```

## Purpose
This project was developed to help organizations monitor and reduce their carbon footprint by providing insights into the emissions generated by their laptops. By automating data collection and providing an easy-to-use interface, it empowers users to make informed decisions toward sustainability.
