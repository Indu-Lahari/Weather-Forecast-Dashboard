import streamlit

streamlit.title("Weather Forecast for the Next Days")
place = streamlit.text_input("Place: ")
days = streamlit.slider("Forecast Days", min_value=1, max_value=5,
                        help="Select the number of forecasted days")
option = streamlit.selectbox("Select data to view",
                             ("Temperature", "Sky"))
streamlit.subheader(f"{option} for the next {days} days in {place}")