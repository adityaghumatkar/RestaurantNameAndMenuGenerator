import streamlit as st
from data.cuisine import cuisine
import json
from langchain_helper import generate_name_and_items

st.title('Restaurant Name Generator')
st.write('This is a simple web app to generate restaurant names.')

selected_cusine = st.sidebar.selectbox('Select a cuisine', cuisine)


if st.sidebar.button('Generate'):
    response = generate_name_and_items(selected_cusine)
    restaurant_name = response["restaurant_name"]
    menuitem = response["menu_items"]

    st.header(restaurant_name)
    st.subheader('Menu Items')

    menu_json_array =json.loads(menuitem)
    for item in menu_json_array:
        st.markdown(f"<h3 style='font-size:24px;'>{item["name"]}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:16px;'>{item["description"]}</p>", unsafe_allow_html=True)
