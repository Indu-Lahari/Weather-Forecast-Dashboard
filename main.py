import streamlit
import plotly.express as px

streamlit.title("Weather Forecast for the Next Days")
place = streamlit.text_input("Place: ")
days = streamlit.slider("Forecast Days:", min_value=1, max_value=5,
                        help="Select the number of forecasted days")
option = streamlit.selectbox("Select data to view:",
                             ("Temperature", "Sky"))
streamlit.subheader(f"{option} for the next {days} days in {place}")


# Data Visualization
dates = ["28-10-2023", "29-10-2023", "30-10-2023"]
temperatures = [37, 36, 43]


figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
streamlit.plotly_chart(figure)