import streamlit as st
import datetime

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Chai is ready!")

add_masala=st.checkbox("Add Masala")

if add_masala:
    st.write("Masala Added to Your Chai")


tea_type=st.radio("Select Tea Type", ("Black Tea", "Green Tea", "Herbal Tea"))
st.write(f"You selected {tea_type}")

flavour=st.selectbox("Select Flavour", ("Cardamom", "Ginger", "Mint"))
st.write(f"You selected {flavour}")

sugar=st.slider("Select Sugar Level", 0, 10, 5)
st.write(f"You selected {sugar} level of sugar")

cups=st.number_input("Number of Cups", 1, 10, 1)
st.write(f"You selected {cups} cups")

name=st.text_input("Enter Your Name")
# st.write(f"Hello {name}, your chai is being prepared!")

if name:
    st.write(f"Hello {name}, your chai is being prepared!")

dob=st.date_input("Enter Your Date of Birth")
st.write(f"Your date of birth is {dob}")

dob2 = st.date_input(
    "Enter Your Date of Birth",
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today()
)
st.write(f"Your date of birth is {dob2}")