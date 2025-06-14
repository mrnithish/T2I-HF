# T2I-HF: Text-to-Image with Multiple Models (Hugging Face and Prompt Enhancer)

## Overview
T2I-HF is a streamlined application for generating images from text prompts using Hugging Face's powerful models. The application includes a prompt enhancer and supports multiple image generation models such as Stable Diffusion. The user-friendly interface is powered by Streamlit, allowing seamless interaction.

## Features
1. **Prompt Enhancer:** Automatically refines your text prompts to produce higher-quality images.
2. **Image Generator:** Leverages Hugging Face community models like Stable Diffusion and FLUX for generating images from text.


## Requirements
- Python 3.8+
- Streamlit
- Hugging Face Transformers
- Stable Diffusion-related libraries

## Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/mrnithish/T2I-HF.git
cd T2I-HF
```

### Step 2: Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```


### Step 3: Create an `.env` File
Store your API keys and configuration in a `.env` file. Example:
```env
HUGGINGFACE_TOKEN=your_huggingface_token
```

### Step 4: Run the Application
```bash
streamlit run main.py
```

## Usage
1. Enter your text prompt in the input box.
2. (Optional) Use the prompt enhancer to refine your text.
3. Generate an image using your selected model.
4. Download or share the generated image.

## Models Supported
- Hugging Face Community Models
- Stable Diffusion
- FLUX

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your updates or enhancements.


## License
This project is licensed under the MIT License. See the LICENSE file for details.


## Acknowledgments
- [Hugging Face](https://huggingface.co/)
- [Stable Diffusion](https://stability.ai/)
- [Streamlit](https://streamlit.io/)

