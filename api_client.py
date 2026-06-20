import os
import io
import requests
from PIL import Image

HF_MODEL_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"


class ImageGenerationError(Exception):
    pass


def get_api_token() -> str:
    token = os.environ.get("HF_API_TOKEN")
    if not token:
        raise ImageGenerationError(
            "No API token found. Please set HF_API_TOKEN in your .env "
            "file locally, or in Streamlit Secrets when deployed."
        )
    return token


def generate_image(prompt: str, negative_prompt: str = "", width: int = 512, height: int = 512) -> Image.Image:
    token = get_api_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "width": width,
            "height": height,
        },
    }

    if negative_prompt and negative_prompt.strip():
        payload["parameters"]["negative_prompt"] = negative_prompt.strip()

    try:
        response = requests.post(HF_MODEL_URL, headers=headers, json=payload, timeout=60)
    except requests.exceptions.RequestException as e:
        raise ImageGenerationError(f"Network error while contacting Hugging Face API: {e}")

    if response.status_code == 503:
        raise ImageGenerationError(
            "The model is still loading. "
            "Please wait ~20 seconds and try again."
        )

    if response.status_code == 401:
        raise ImageGenerationError("Invalid API token. Check your HF_API_TOKEN.")

    if response.status_code == 429:
        raise ImageGenerationError("Rate limit reached. Wait a bit before generating again.")

    if response.status_code != 200:
        try:
            err_json = response.json()
            err_msg = err_json.get("error", response.text[:200])
        except Exception:
            err_msg = response.text[:200]
        raise ImageGenerationError(
            f"API request failed (status {response.status_code}): {err_msg}"
        )

    content_type = response.headers.get("content-type", "")
    if "image" not in content_type:
        try:
            err_json = response.json()
            err_msg = err_json.get("error") or str(err_json)
        except Exception:
            err_msg = response.text[:200] or "Unknown error"
        raise ImageGenerationError(f"API returned a non-image response: {err_msg}")

    try:
        image = Image.open(io.BytesIO(response.content))
        image.load()
        return image
    except Exception:
        raise ImageGenerationError("Received a response but couldn't decode it as an image.")