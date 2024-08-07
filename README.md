# Weather Forecast Data Dashboard

## Project Description

This project provides a web-based dashboard for visualizing weather forecast data. Built using Streamlit and Plotly, the application allows users to input a location and view weather forecasts for the next few days. Users can choose between viewing temperature trends or sky conditions, with visualizations to enhance data understanding.

## Process

1. **User Interface Development:**
   - Created a Streamlit application to build an interactive dashboard.
   - Implemented user input options including text input for location, a slider for the number of forecast days, and a select box to choose the type of data to view (Temperature or Sky).

2. **Data Retrieval:**
   - Used the OpenWeatherMap API to fetch weather forecast data based on user input.
   - Implemented a function to process API responses and filter data according to the selected number of days.

3. **Data Visualization:**
   - Utilized Plotly to create interactive line charts for temperature trends.
   - Displayed sky conditions using image representations to provide a visual understanding of weather conditions.

4. **Error Handling:**
   - Added error handling for non-existent locations to provide user-friendly feedback.

## Technology Used

- **Streamlit:** For building the interactive web dashboard.
- **Plotly:** For creating dynamic and interactive visualizations.
- **OpenWeatherMap API:** For retrieving weather forecast data.
- **Requests:** For making HTTP requests to the OpenWeatherMap API.

## What I Learned

- **Streamlit Development:**
  - Gained experience in using Streamlit for developing interactive web applications.
  - Learned how to integrate various Streamlit components like text input, sliders, and select boxes.

- **Data Visualization:**
  - Enhanced skills in using Plotly for creating line charts and managing image-based data visualizations.
  - Understood the importance of visual representation in data analysis and user experience.

- **API Integration:**
  - Learned how to interact with external APIs and process JSON responses.
  - Developed skills in filtering and manipulating data from API responses.

## Future Insights

- **Enhancements:**
  - Integrate additional weather parameters such as humidity, wind speed, and precipitation for a more comprehensive forecast.
  - Add features for comparing forecasts between multiple locations.

- **User Experience Improvements:**
  - Implement a more sophisticated error handling mechanism to handle various types of user input errors.
  - Provide options for customizing visualizations (e.g., different chart types, color schemes).

- **Performance Optimization:**
  - Optimize data retrieval and processing to handle larger datasets more efficiently.
  - Implement caching to reduce API calls and improve response times.

Feel free to explore the code and run the application locally:
- `main.py` for the Streamlit application and visualization logic.
- `backend.py` for fetching and processing weather data from the API.