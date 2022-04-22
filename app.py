import streamlit as st
import joblib
from prediction_pipeline import *
from PIL import Image


st.set_page_config(page_title="Cyberbully Detection 🚨",
                   page_icon="🚨", layout="wide")


#creating option list for dropdown menu


st.markdown("<h1 style='text-align: center;'>Cyberbully Detection Application🚨</h1>", unsafe_allow_html=True)
image = Image.open('Cyber Bullying.jpg')
st.image(image)
def main():
    with st.form('prediction_form'):

        st.subheader("Enter your comment below.")
        comment = st.text_input(label='Enter text here...')
        submit = st.form_submit_button("Predict")


    if submit:
       pred = get_predictions(comment)
       st.write(pred)
       # if pred == 'Toxic':
       #        st.write('Ughhh!!! It seems like a Toxic comment.😒')
       # else:
       #        st.write('Not toxic.🙂')
       #st.write(f"The predicted severity is:  {pred}")

if __name__ == '__main__':
    main()