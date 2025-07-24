import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io
from dotenv import load_dotenv
import os
from prompt_enhancer import PromptEnhancer


# Load environment variables
load_dotenv()
api_token = os.getenv("HUGGINGFACE_API_TOKEN")

# Streamlit app layout
st.title("Text-to-Image Generator")
st.sidebar.header("Settings")

# Sidebar - Prompt Customization
st.sidebar.subheader("Prompt Customization")
prompt = st.sidebar.text_input("Enter a text prompt:", "Astronaut riding a horse", key="sidebar_prompt")

# Sidebar - Image Customization
st.sidebar.subheader("Image Generation Settings")
model_name = st.sidebar.selectbox(
    "Select a Model",
    [
        "stabilityai/stable-diffusion-3.5-large-turbo",
        "stabilityai/stable-diffusion-xl-base-1.0",
        "black-forest-labs/FLUX.1-dev",
        "strangerzonehf/Flux-Super-Realism-LoRA",
        "strangerzonehf/Flux-Midjourney-Mix2-LoRA",
    ]
)
max_length = st.sidebar.slider("Max Length", min_value=50, max_value=500, value=256, step=10)
repetition_penalty = st.sidebar.slider("Repetition Penalty", min_value=1.0, max_value=2.0, value=1.2, step=0.1)

# Initialize Prompt Enhancer
enhancer = PromptEnhancer()

# Button to enhance the prompt
enhanced_prompt = prompt # Default to the original prompt
if st.sidebar.button("Enhance Prompt"):
    if not prompt.strip():
        st.toast("Please provide a valid prompt to enhance.", icon="⚠️")
    else:
        try:
            enhanced_prompt = enhancer.enhance(prompt)
            st.toast("Prompt enhanced successfully!", icon="✅")
        except Exception as e:
            st.toast(f"Error enhancing prompt: {e}", icon="❌")

# Update the text input field to show the enhanced prompt if available
prompt = st.text_input("Enter a text prompt:", enhanced_prompt, key="main_prompt")
print(prompt)
x=enhanced_prompt
print(x)
def generate_image(prompt, model_name, token):
    """Generate an image using the Hugging Face Inference API."""
    client = InferenceClient(model_name, token=token)
    try:
        image = client.text_to_image(prompt)
        return image
    except Exception as e:
        st.toast(f"Error generating image: {e}", icon="❌")
        return None
    
# Button to generate the image
if st.button("Generate Image"):
    if not api_token:
        st.toast("API token not found. Please check your .env file.", icon="⚠️")
    elif not prompt.strip():
        st.toast("Please provide a valid prompt.", icon="⚠️")
    else:
        st.toast("Generating image. Please wait...")
        image = generate_image(x, model_name, api_token)
        if image:
            st.image(image, caption="Generated Image", use_container_width=True)
