from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from prompt_enhancer import PromptEnhancer
from fastapi.staticfiles import StaticFiles

# Load environment variables
load_dotenv()
api_token = os.getenv("HUGGINGFACE_API_TOKEN")

app = FastAPI()

# Initialize Prompt Enhancer
enhancer = PromptEnhancer()

# Static file serving for frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as f:
        return f.read()

@app.post("/enhance_prompt")
async def enhance_prompt(prompt: str = Form(...)):
    """Enhance the prompt."""
    if not prompt.strip():
        return JSONResponse(content={"error": "Please provide a valid prompt."}, status_code=400)

    try:
        enhanced_prompt = enhancer.enhance(prompt)
        return JSONResponse(content={"enhanced_prompt": enhanced_prompt})
    except Exception as e:
        return JSONResponse(content={"error": f"Error enhancing prompt: {str(e)}"}, status_code=500)

@app.post("/generate_image")
async def generate_image(prompt: str = Form(...), model_name: str = Form(...)):
    """Generate an image using the Hugging Face Inference API."""
    if not api_token:
        return JSONResponse(content={"error": "API token not found."}, status_code=400)
    if not prompt.strip():
        return JSONResponse(content={"error": "Please provide a valid prompt."}, status_code=400)

    client = InferenceClient(model_name, token=api_token)
    try:
        image = client.text_to_image(prompt)
        image_path = "generated_image.png"
        image.save(image_path)
        return JSONResponse(content={"image_url": image_path})
    except Exception as e:
        return JSONResponse(content={"error": f"Error generating image: {str(e)}"}, status_code=500)
