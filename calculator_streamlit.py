import streamlit as st

st.title("Simple Calculator")
st.write("-------------")

# Operation choice
choice = st.radio(
    "Select an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Number inputs
num1 = st.number_input("Enter your first number:", value=0)
num2 = st.number_input("Enter your second number:", value=0)

# Perform calculation
result = None
if choice == "Addition":
    result = num1 + num2
elif choice == "Subtraction":
    result = num1 - num2
elif choice == "Multiplication":
    result = num1 * num2
elif choice == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Error: Division by zero is not allowed.")

# Show result with colorful background and full border
if result is not None:
    st.markdown(
        f"""
        <div style="
            border:4px solid #FF5722;
            padding:15px;
            border-radius:12px;
            background-color:#FFE0B2;
            text-align:center;
        ">
            <h3 style="color:#BF360C;">Result: {result}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )



