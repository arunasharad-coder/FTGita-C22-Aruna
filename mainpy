import streamlit as st
from langchain_openai import ChatOpenAI

# Main Title
st.title("📖 GitaSummary-GPT")

# Updated description with the clipboard icon
st.markdown("📋 **Summary:** Get a concise breakdown of any verse or chapter.") 
st.markdown("❤️ Powered by GPT-4.1 fine-tuned model.")

# Text input for topic
topic = st.text_input("Please enter the topic")

st.code("""
            Try:
            Explain the summary of Chapter 2?
            """, language= None)

# Initialize the models
base_model = ChatOpenAI(model="gpt-4.1-2025-04-14")
ft_model = ChatOpenAI(model="ft:gpt-4.1-2025-04-14:personal::DCvHUpdR")

def generate_linkedin_post(prompt, base_model=base_model, ft_model=ft_model):
    response1 = base_model.invoke(prompt)
    response2 = ft_model.invoke(prompt)
    return response1.content, response2.content

if st.button("Summarize"):
    if topic:
        with st.spinner("Summarizing..."):
            base_response, ft_response = generate_linkedin_post(f"Generate a summary of {topic}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Base Model (gpt-4o-mini) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)
        
        with col2:
            st.subheader("Satvik-GPT (Fine-tuned Model)")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic before generating posts.")