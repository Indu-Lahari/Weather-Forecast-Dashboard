import streamlit
import plotly.express as px
from backend import get_data

# Add title, text input, slider, select box, and sub header
streamlit.title("Weather Forecast for the Next Days")
place = streamlit.text_input("Place: ")
days = streamlit.slider("Forecast Days:", min_value=1, max_value=5,
                        help="Select the number of forecasted days")
option = streamlit.selectbox("Select data to view:",
                             ("Temperature", "Sky"))
streamlit.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        # Get the Temperature/Sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create Temperature Plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            streamlit.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            streamlit.image(image_paths, width=110)

except KeyError:
    streamlit.info("Hey! You entered a non-existing place. Please enter again")
