import os
import io
import streamlit as st
from dotenv import load_dotenv

from prompts import (
    build_final_prompt,
    get_style_options,
    DEFAULT_NEGATIVE_PROMPT
)

from api_client import (
    generate_image,
    ImageGenerationError
)

load_dotenv()

try:
    if "HF_API_TOKEN" in st.secrets:
        os.environ["HF_API_TOKEN"] = st.secrets["HF_API_TOKEN"]
except Exception:
    pass

st.set_page_config(
    page_title="Clarity JPG",
    page_icon="💖",
    layout="centered"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');

:root{
    --bg-1:#15101f;
    --card:#1b1428;
    --card-2:#221a32;
    --border:#3a2c5a;
    --text-dim:#b3a6d9;
    --accent:#b794f6;
    --accent-2:#9333ea;
    --accent-3:#22d3ee;
    --accent-glow:rgba(183,148,246,.45);
}

.stApp{
    background:
        radial-gradient(circle at 10% -10%, rgba(147,51,234,.30), transparent 40%),
        radial-gradient(circle at 90% 10%, rgba(34,211,238,.15), transparent 35%),
        radial-gradient(circle at 50% 100%, rgba(183,148,246,.15), transparent 45%);
}

.block-container{
    max-width:880px;
    margin:auto;
    padding-top:3rem;
    padding-bottom:4rem;
}

h1, h2, h3, .hero-title, .gallery-title{
    font-family:'Space Grotesk', sans-serif;
}

.hero{
    text-align:center;
    margin-bottom:2.2rem;
}

.hero-title{
    font-weight:700;
    font-size:3.6rem;
    background:linear-gradient(120deg, #22d3ee, #b794f6 45%, #f472b6 90%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
    letter-spacing:-0.03em;
    filter:drop-shadow(0 0 30px rgba(183,148,246,.35));
}

.hero-sub{
    color:var(--text-dim);
    font-size:1.05rem;
    margin-top:.5rem;
    line-height:1.5;
}

.main-card{
    position:relative;
    background:linear-gradient(180deg, var(--card), var(--card-2));
    padding:2.2rem;
    border-radius:22px;
    border:1px solid var(--border);
    box-shadow:0 25px 60px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.05);
    overflow:hidden;
}

.main-card::before{
    content:"";
    position:absolute;
    top:0; left:0; right:0;
    height:3px;
    background:linear-gradient(90deg, var(--accent-3), var(--accent), var(--accent-2));
}

.result-card{
    position:relative;
    background:linear-gradient(180deg, var(--card), var(--card-2));
    padding:1.6rem;
    border-radius:22px;
    margin-top:2rem;
    border:1px solid var(--border);
    box-shadow:0 25px 60px rgba(0,0,0,.45);
    overflow:hidden;
}

.result-card::before{
    content:"";
    position:absolute;
    top:0; left:0; right:0;
    height:3px;
    background:linear-gradient(90deg, var(--accent-2), var(--accent), var(--accent-3));
}

.stTextArea textarea{
    min-height:220px !important;
    border-radius:14px !important;
}

.stTextArea textarea:focus{
    border-color:var(--accent) !important;
    box-shadow:0 0 0 3px var(--accent-glow) !important;
}

.stTextInput input:focus{
    border-color:var(--accent) !important;
    box-shadow:0 0 0 3px var(--accent-glow) !important;
}

/* Radio "chips" */
div[role="radiogroup"]{
    gap:.4rem;
}

div[role="radiogroup"] label{
    border:1.5px solid var(--border);
    border-radius:999px;
    padding:6px 16px;
    transition:border-color .15s ease;
}

div[role="radiogroup"] label:hover{
    border-color:var(--accent);
}

/* Buttons */
.stButton button{
    width:100%;
    height:56px;
    background:linear-gradient(135deg, var(--accent-3), var(--accent) 55%, var(--accent-2));
    color:#0a0614;
    border:none;
    border-radius:14px;
    font-weight:700;
    font-size:1.05rem;
    box-shadow:0 10px 28px var(--accent-glow);
    transition:transform .15s ease, box-shadow .15s ease, filter .15s ease;
}

.stButton button:hover{
    transform:translateY(-1px);
    box-shadow:0 12px 30px var(--accent-glow);
    filter:brightness(1.08);
}

.stDownloadButton button{
    width:100%;
    border-radius:12px !important;
}

.gallery-title{
    text-align:center;
    font-weight:600;
    font-size:1.4rem;
    margin-top:2.5rem;
    margin-bottom:1rem;
}

.small-caption{
    text-align:center;
    color:var(--accent);
    font-weight:600;
    margin-top:.6rem;
}

/* Images */
[data-testid="stImage"] img{
    border-radius:14px;
    border:1px solid var(--border);
}

/* Alerts */
[data-testid="stAlert"]{
    border-radius:12px;
}

hr{
    border-color:var(--border) !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="hero"><div class="hero-title">Clarity JPG</div>'
    '<div class="hero-sub">Describe what you\'re imagining, pick a vibe, and I\'ll generate it.</div></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

user_prompt = st.text_area(
    "Describe your image",
    placeholder="A better version of unemployment..."
)

style = st.radio(
    "Pick a vibe",
    options=get_style_options(),
    horizontal=True
)

with st.expander("Advanced Settings"):
    negative_prompt = st.text_input(
        "Negative Prompt",
        value=DEFAULT_NEGATIVE_PROMPT
    )

    img_size = st.select_slider(
        "Image Size",
        options=[512, 768, 1024],
        value=768
    )

generate_clicked = st.button("Generate")

st.markdown("</div>", unsafe_allow_html=True)

if generate_clicked:

    if not user_prompt.strip():
        st.warning("bro you gotta type something first da 😭")

    else:

        try:

            final_prompt = build_final_prompt(
                user_prompt,
                style
            )

            with st.spinner("creating magic..."):

                image = generate_image(
                    prompt=final_prompt,
                    negative_prompt=negative_prompt,
                    width=img_size,
                    height=img_size
                )

                buffer = io.BytesIO()
                image.save(buffer, format="PNG")

                st.session_state.history.insert(
                    0,
                    {
                        "prompt": user_prompt,
                        "style": style,
                        "image_bytes": buffer.getvalue()
                    }
                )

                st.rerun()

        except ImageGenerationError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Something went wrong: {e}")

if st.session_state.history:

    latest = st.session_state.history[0]

    st.markdown(
        '<div class="result-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        "###  your questionable masterpiece"
    )

    st.image(
        latest["image_bytes"],
        use_container_width=True
    )

    st.markdown(
        f"<div class='small-caption'>{latest['style']}</div>",
        unsafe_allow_html=True
    )

    st.download_button(
        "⬇ Download Image",
        latest["image_bytes"],
        "clarity_output.png",
        "image/png"
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

if len(st.session_state.history) > 1:

    st.markdown(
        "<div class='gallery-title'> your gallery</div>",
        unsafe_allow_html=True
    )

    gallery_items = st.session_state.history[1:]

    for row_start in range(0, len(gallery_items), 3):
        row_items = gallery_items[row_start:row_start + 3]
        cols = st.columns(3)

        for col, item in zip(cols, row_items):
            with col:
                st.image(
                    item["image_bytes"],
                    use_container_width=True
                )
                st.caption(item["style"])