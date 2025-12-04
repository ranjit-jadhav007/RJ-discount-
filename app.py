import streamlit as st
import numpy as np

st.title("RJ's Design")
st.image("cloth_logo.png",width=700)

user_input = st.text_input("Enter Cloths prices:  (space-separated):")

if user_input:
    try:
        arr = np.array([float(x) for x in user_input.split()])
        st.write("Cloth prices :", arr)
        st.write("Total number of clothes:", arr.shape)
        
        st.write("Total Price:",sum(arr))
        st.title("Discount Section")
        discount=st.number_input("Enter Discount:")
        
        new_price=arr-(arr*discount/100)
        st.write("After discount :",sum(new_price))

    except:
        st.error("Invalid input. Enter only numbers separated by spaces.")

