import streamlit
import plotly.express as px
from backend import get_data

streamlit.title("Weather Forecast for the Next Days")
place = streamlit.text_input("Place: ")
days = streamlit.slider("Forecast Days:", min_value=1, max_value=5,
                        help="Select the number of forecasted days")
option = streamlit.selectbox("Select data to view:",
                             ("Temperature", "Sky"))
streamlit.subheader(f"{option} for the next {days} days in {place}")



d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
streamlit.plotly_chart(figure)