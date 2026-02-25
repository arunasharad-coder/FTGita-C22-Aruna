import streamlit as st
from langchain_openai import ChatOpenAI
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GitaSummary-GPT", 
    page_icon="📖", 
    layout="wide"
)

# --- 2. SECRETS & API KEY SETUP ---
# This looks for the key in your .streamlit/secrets.toml (local) 
# or the Secrets tab (Streamlit Cloud).
if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
else:
    st.error("Missing OpenAI API Key. Please add it to your Streamlit Secrets.")
    st.stop()

# --- 3. CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .output-text {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        color: #1e1e1e;
        line-height: 1.6;
        min-height: 200px;
    }
    stSubheader {
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER SECTION ---
st.title("📖 GitaSummary-GPT")
st.markdown("📋 **Summary:** Get a concise breakdown of any verse or chapter.") 
st.markdown("❤️ Powered by **Aruna-GPT** (Fine-tuned GPT-4o).")

# --- 5. INPUT SECTION ---
topic = st.text_input("Enter the Chapter or Verse:", placeholder="e.g., Chapter 2, Verse 47")

st.info("💡 **Try:** 'Explain the summary of Chapter 2'", icon="💡")

# --- 6. MODEL INITIALIZATION (CACHED) ---
@st.cache_resource
def load_models():
    # Base model for comparison
    base = ChatOpenAI(model="gpt-4o") 
    # Your specific fine-tuned model ID
    ft = ChatOpenAI(model="ft:gpt-4o-2024-08-06:personal::DCvHUpdR") 
    return base, ft

base_model, ft_model = load_models()

# --- 7. LOGIC & OUTPUT ---
if st.button("Summarize"):
    if topic:
        with st.spinner("Meditating on the verses..."):
            try:
                # Generate responses
                prompt = f"Provide a spiritual summary and key takeaway for: {topic}"
                base_response = base_model.invoke(prompt)
                ft_response = ft_model.invoke(prompt)
                
                # Create two columns for comparison
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Standard GPT-4o 🔗")
                    st.markdown(f'<div class="output-text">{base_response.content}</div>', unsafe_allow_html=True)
                
                with col2:
                    st.subheader("Aruna-GPT (Fine-tuned) ✨")
                    st.markdown(f'<div class="output-text">{ft_response.content}</div>', unsafe_allow_html=True)
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic before clicking Summarize.")

# --- 8. FOOTER ---
st.divider()
st.caption("Deepen your understanding of the Bhagavad Gita with AI-powered insights.")
