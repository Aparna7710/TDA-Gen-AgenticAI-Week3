STYLE_MODIFIERS = {

    "Realistic": """
    photorealistic,
    realistic lighting,
    DSLR photography,
    natural skin textures,
    cinematic lighting,
    depth of field,
    ultra realistic
    """,

    "Anime": """
    anime illustration,
    studio quality,
    expressive characters,
    vibrant colors,
    clean linework,
    detailed anime background,
    high quality anime artwork
    """,

    "Cyberpunk": """
    cyberpunk city,
    neon lighting,
    futuristic atmosphere,
    holograms,
    synthwave colors,
    cinematic environment,
    concept art
    """,

    "Watercolor": """
    watercolor painting,
    soft brush strokes,
    artistic illustration,
    storybook art,
    textured paper,
    elegant color palette
    """,

    "3D Render": """
    unreal engine 5,
    octane render,
    ray tracing,
    realistic materials,
    cinematic lighting,
    high quality 3D render
    """,

    "Sketch": """
    pencil sketch,
    hand drawn illustration,
    detailed line art,
    cross hatching,
    concept art sketch,
    artist notebook style
    """
}

DEFAULT_NEGATIVE_PROMPT = """
worst quality,
low quality,
blurry,
out of focus,
deformed,
mutated,
bad anatomy,
poorly drawn face,
poorly drawn hands,
extra fingers,
missing fingers,
extra limbs,
missing limbs,
duplicate,
cropped,
watermark,
signature,
logo,
text,
jpeg artifacts,
oversaturated,
ugly
"""


def build_final_prompt(user_prompt: str, style: str) -> str:

    user_prompt = user_prompt.strip()

    if not user_prompt:
        return ""

    modifier = STYLE_MODIFIERS.get(style, "")

    if style == "Realistic":

        quality_boost = """
        masterpiece,
        best quality,
        ultra detailed,
        professional photography,
        cinematic lighting,
        depth of field,
        sharp focus,
        highly detailed
        """

    else:

        quality_boost = """
        masterpiece,
        best quality,
        highly detailed,
        professional artwork,
        beautiful composition,
        vibrant colors,
        detailed background,
        trending artwork
        """

    return f"""
{user_prompt}

{modifier}

{quality_boost}
"""

def get_style_options() -> list:
    return list(STYLE_MODIFIERS.keys())