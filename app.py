import streamlit as st


st.title("🎓 Student Registration App")

with st.form("student_form"):

    name = st.text_input(
        "👤 Name",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "📧 Email",
        placeholder="Enter your email"
    )

    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=100,
        step=1
    )

    gender = st.selectbox(
        "⚧ Gender",
        ["", "Male", "Female", "Other"]
    )

    course = st.selectbox(
        "📚 Course",
        ["", "Python", "Java", "C", "Data Science", "AI"]
    )

    skills = st.text_input(
        "💻 Skills",
        placeholder="Example: Python, SQL, Excel"
    )

    submitted = st.form_submit_button("🚀 Register")


if submitted:

    if name == "" or email == "" or course == "":
        st.error("❌ Please fill all required fields.")

    else:
        st.success("🎉 Registration Successful!")

        st.write("### 📋 Student Details")
        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Age:**", age)
        st.write("**Gender:**", gender)
        st.write("**Course:**", course)
        st.write("**Skills:**", skills)
