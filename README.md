#  Clarity JPG

**Clarity JPG** is an AI-powered image generation application built with **Streamlit** and the **Hugging Face Inference API**. It serves as an extension to the clarity AI model which only worked for text based queries.

This AI enables you to choose an artistic style, and generate unique AI artwork in seconds.

---

## Depolyed link 

**Deployed App:** https://clarity-jpg-ai.streamlit.app/

---

## Project Overview

Clarity JPG transforms natural language prompts into AI-generated images using the **FLUX.1-schnell** diffusion model.

Users can:

* Enter a custom image prompt
* Select a visual style
* Generate AI images in real time
* Download generated images
* View previous creations during the session

The application uses prompt engineering techniques to modify user prompts based on the selected style before sending them to the image generation API.
---

## Features in Clarity JPG


### 1. Multiple Art Styles

Users can choose from:

* Realistic
* Anime
* Cyberpunk
* Watercolor
* 3D Render
* Sketch

Each style automatically enhances the prompt with style-specific descriptors.

---

### 2. AI Image Generation

Generate images directly from text descriptions using the Hugging Face Inference API and FLUX.1-schnell.

Examples:

**Prompt:**

> A futuristic Indian city at night

**Style:**

> Cyberpunk

**Result:**

An AI-generated futuristic city with neon lighting, holograms, and cyberpunk aesthetics.

---

### 3. Prompt History

Generated images are stored during the current session, allowing users to revisit previous creations.

---

### 4. Download Images

Every generated image can be downloaded directly from the application.

---

### 5. Advanced Controls

Users can optionally:

* Enter a negative prompt
* Select image resolution
* Experiment with different styles and prompt combinations

---

## Technologies used 

| Technology                 | Purpose                         |
| -------------------------- | ------------------------------- |
| Python                     | Core application logic          |
| Streamlit                  | Frontend and deployment         |
| Hugging Face Inference API | AI image generation             |
| FLUX.1-schnell             | Diffusion image model           |
| Pillow                     | Image processing                |
| Python-dotenv              | Environment variable management |

---

##  Project Structure

```text
clarity-jpg/
│
├── app.py
├── api_client.py
├── prompts.py
├── requirements.txt
├── .env.example
└── README.md
```

### File Responsibilities

**app.py**

* Streamlit user interface
* Session state management
* User interaction handling

**api_client.py**

* Hugging Face API integration
* Request handling
* Error management

**prompts.py**

* Style modifiers
* Prompt engineering logic
* Prompt construction

---


##  Running Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

Create a `.env` file:

```env
HF_API_TOKEN=your_token_here
```
---

## Known Limitation

Image quality is highly dependent on prompt specificity.

Simple prompts such as:

> cat

may produce generic results.

More descriptive prompts typically generate significantly better outputs.

Example:

> cute orange cat wearing sunglasses, sitting on a rooftop at sunset, cinematic lighting, highly detailed

produces much stronger results.

---

##  Screenshot

<img width="1917" height="871" alt="image" src="https://github.com/user-attachments/assets/d671ab95-06f0-48d5-a14a-1d7188965165" />
<img width="1917" height="871" alt="image" src="https://github.com/user-attachments/assets/4a17915d-6264-41fa-9dd6-0e7e1ad08b24" />
<img width="1917" height="870" alt="image" src="https://github.com/user-attachments/assets/ff44fe12-5490-4736-b2b5-61ce53026b03" />
<img width="1917" height="870" alt="image" src="https://github.com/user-attachments/assets/29c342ff-aef7-4fa2-80d6-c8ce03ba3228" />

---

##  Author

Developed as part of the Generative AI Project Series using Streamlit and Hugging Face.
