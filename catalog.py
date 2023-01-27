
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

#streamlit.stop()

# Requery Snowflake to return supporting data for the selection
my_cur.execute("Select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + choice + "' ;")
df2 = my_cur.fetchone()
# Image to view selected clothing

streamlit.image(df2[0], width = 400, caption = "Our warm, comfortable, " + choice + " sweatsuit!" )

# Display price
streamlit.write('Price: ', df2[1])

# Display available sizes
streamlit.write('Sizes Available: ', df2[2])

# Display upsell data
streamlit.write(df2[3])
