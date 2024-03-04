import streamlit as st

st.title("Complete Inelastic Calculator")

massOne = st.number_input("Enter a Mass (kg): ")
massTwo = st.number_input("Enter another Mass(kg): ")
if(massOne == 0 or massTwo == 0):
    st.write("One or Both Masses equals to 0 :rage:")
else:
    velocityInital = st.number_input("Enter a velocity inital (m/s): ")

    initalMomentum = massOne * velocityInital
    finalVelocity = initalMomentum / (massOne + massTwo)

    st.write(f"The final Velocity of this collision is {finalVelocity:.2f}")
    st.write(f"The final Momentum of Mass One is {finalVelocity * massOne:.2f}  and the final Momentum of Mass Two is {finalVelocity * massTwo:.2f}")



