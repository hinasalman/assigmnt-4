import streamlit as st # type: ignore

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    if height > 0:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    return None

# Streamlit app
st.title("BMI Calculator")

st.sidebar.header("Input your details:")
weight = st.sidebar.number_input("Weight (kg):", min_value=0.0, step=0.1, value=70.0)
height = st.sidebar.number_input("Height (m):", min_value=0.0, step=0.01, value=1.75)

if st.sidebar.button("Calculate BMI"):
    if height <= 0 or weight <= 0:
        st.error("Please enter valid positive numbers for weight and height.")
    else:
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is: {bmi}")

        # Categorize BMI
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")