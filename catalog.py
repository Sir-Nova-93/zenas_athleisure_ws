
import streamlit
import snowflake.connector
import pandas

# Header section
streamlit.title("Zena's Amazing Athleisure Catalog")

# Drop down box to select Color/Style
#streamlit.text("Pick a sweatsuit color or style:")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select distinct color_or_style from catalog_for_website")
catalog = my_cur.fetchall()

df = pandas.DataFrame(catalog)

style_list = df[0].values.tolist()
#streamlit.dataframe(style_list)
choice = streamlit.selectbox("Pick a sweatsuit color or style:", list(style_list))

# Image to view selected clothing
my_cur.execute("Select direct_url from catalog_for_website where color_or_style = '" + choice + "'")
image_url = my_cur.fetchone()
streamlit.text(image_url)
#streamlit.image(image_url, caption='Our warm, comfortable, ' + choice + ' sweatsuit!')

# Display caption/descriotion of clothing


# Display price


# Display available sizes


# Display upsell data
