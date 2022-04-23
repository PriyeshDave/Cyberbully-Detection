import streamlit as st
import joblib
from prediction_pipeline import *
from PIL import Image


st.set_page_config(page_title="Cyberbully Detection 🚨",
                   page_icon="🚨", layout="wide")

# creating a side bar 
image_word_cloud = Image.open('Sidebar Image.jpg')
st.sidebar.info("Created By : Priyesh Dave")
# Adding an image to the side bar 
st.sidebar.image(image_word_cloud, width=None)
st.sidebar.subheader("Contact Information : ")
col1, mid, col2 = st.columns([1,1,20])
with col1:
	st.sidebar.subheader("LinkedIn : ")
with col2:
	st.sidebar.markdown("[![Linkedin](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLsu_X_ZxDhuVzjTHvk4eZOmUDklreUExhlw&usqp=CAU)](https://www.linkedin.com/in/priyeshdave21/)")

col3, mid, col4 = st.columns([1,1,20])
with col3:
	st.sidebar.subheader("Github : ")
with col4:
	st.sidebar.markdown("[![Github](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJGtP-Pq0P67Ptyv3tB7Zn2ZYPIT-lPGI7AA&usqp=CAU)](https://github.com/PriyeshDave)")

#creating option list for dropdown menu
st.markdown("<h1 style='text-align: center;'>Cyberbully Detection Application🚨</h1>", unsafe_allow_html=True)
image_cyber_bully = Image.open('Cyber Bullying.jpg')
st.image(image_cyber_bully)
def main():
    with st.form('prediction_form'):

        st.subheader("Enter your comment below.")
        comment = st.text_input(label='Enter text here...')
        submit = st.form_submit_button("Predict")


    if submit:
       pred = get_predictions(comment)
    
       if pred[0] == 'Toxic':
              st.write('Ughhh!!! It seems like a Toxic comment.😒 with probability of {}'.format(round(pred[1], 2)))
       else:
              st.write('Not toxic.🙂 with a predicted probability of {}'.format(round(pred[1], 2)))

if __name__ == '__main__':
    main()