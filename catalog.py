
import streamlit
import snowflake.connector

# Header section
streamlit.title("Zena's Amazing Athleisure Catalog")

# Drop down box to select Color/Style
#streamlit.text("Pick a sweatsuit color or style:")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
style_list = my_cur.execute("Select distinct color_or_style from catalog_for_website")
streamlit.multiselect("Pick a sweatsuit color or style:", list(style_list.index))

# Image to view selected clothing


# Display caption/descriotion of clothing


# Display price


# Display available sizes


# Display upsell data
