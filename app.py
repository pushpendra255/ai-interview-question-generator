import streamlit as st
from prompts import generate_questions
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

st.set_page_config(page_title="TalentScout – AI Hiring Assistant", layout="centered")
st.title("🤖 TalentScout – AI Hiring Assistant")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.stage = "form"

# Candidate form
if st.session_state.stage == "form":
    st.markdown("Welcome to TalentScout! Please enter your details to get started.")
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (comma-separated)")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not all([full_name, email, phone, experience, position, location, tech_stack]):
            st.error("⚠️ Please fill in all the fields before submitting.")
        else:
            st.session_state.candidate_data = {
                "Name": full_name,
                "Email": email,
                "Phone": phone,
                "Experience": experience,
                "Position": position,
                "Location": location,
                "Tech Stack": tech_stack
            }
            tech_list = [t.strip() for t in tech_stack.split(",") if t.strip()]
            st.session_state.questions = generate_questions(tech_list)
            st.session_state.tech_list = tech_list
            st.session_state.stage = "questions"
            st.rerun()

# Display questions and chatbot
if st.session_state.stage == "questions":
    st.subheader("📋 Here are your technical questions:")
    for tech, qs in st.session_state.questions.items():
        st.markdown(f"### 🔧 {tech}")
        for i, q in enumerate(qs, 1):
            st.markdown(f"**Q{i}.** {q}")

    st.markdown("---")
    st.markdown("### 💬 Ask anything below (or type 'exit' to quit):")

    user_input = st.text_input("Your message", key="chat_input")
    if user_input:
        st.chat_message("user").write(user_input)

        if user_input.lower().strip() in ["exit", "quit"]:
            st.chat_message("assistant").write("Thank you for using TalentScout. Goodbye! 👋")

        elif "answer" in user_input.lower() or "ready to answer" in user_input.lower():
            for tech, qs in st.session_state.questions.items():
                st.chat_message("assistant").markdown(f"### ✅ Answers for {tech}")
                for i, q in enumerate(qs, 1):
                    response = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": "Answer this technical interview question briefly and professionally."},
                            {"role": "user", "content": q},
                        ]
                    )
                    answer = response.choices[0].message.content.strip()
                    st.chat_message("assistant").markdown(f"**Q{i}.** {q}\n\n✅ **Answer:**\n{answer}")

        else:
            chat = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a helpful recruiter assistant."},
                    {"role": "user", "content": user_input},
                ]
            )
            answer = chat.choices[0].message.content.strip()
            st.chat_message("assistant").write(answer)
