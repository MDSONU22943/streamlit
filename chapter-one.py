import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")

chai=st.selectbox(
    "Select your favorite chai",
    ("Masala Chai", "Ginger Chai", "Lemon Chai", "Black Chai", "Green Chai")
)
st.write(f"You Choose {chai}. Excellent choice!")

st.success("Your chai has beem brewed!")
