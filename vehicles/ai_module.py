import base64
import requests
from django.conf import settings


def analyze_phone_image(image_path):
    try:
        with open(image_path, "rb") as f:
            image_data = base64.standard_b64encode(f.read()).decode("utf-8")

        ext = image_path.lower().split(".")[-1]
        media_type_map = {
            "jpg": "image/jpeg",
            "jpeg": "image/jpeg",
            "png": "image/png",
            "webp": "image/webp",
            "gif": "image/gif",
        }
        media_type = media_type_map.get(ext, "image/jpeg")

        prompt = """You are an expert smartphone price estimation system.

Carefully examine the image and provide a detailed analysis:
- Identify if there is a smartphone in the image
- If yes — what brand and model (or closest match), color if visible
- Assess the physical condition: screen, body, any visible scratches/cracks/damage
- Estimate the approximate market price in USD based on condition and model
- Explain the key factors affecting the price

At the end, provide a confidence score from 0 to 100 in this exact format:
CONFIDENCE: <number>

Also provide estimated price range in this exact format:
PRICE_MIN: <number>
PRICE_MAX: <number>

Respond in English, 5-7 sentences."""

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "anthropic/claude-haiku-4-5",
                "max_tokens": 1024,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{media_type};base64,{image_data}",
                                },
                            },
                            {
                                "type": "text",
                                "text": prompt,
                            },
                        ],
                    }
                ],
            },
        )

        data = response.json()
        full_text = data["choices"][0]["message"]["content"]

        confidence = 0.0
        price_min = 0
        price_max = 0
        lines = full_text.splitlines()

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("CONFIDENCE:"):
                try:
                    confidence = float(stripped.split(":")[1].strip())
                except ValueError:
                    pass
            elif stripped.startswith("PRICE_MIN:"):
                try:
                    price_min = int(float(stripped.split(":")[1].strip()))
                except ValueError:
                    pass
            elif stripped.startswith("PRICE_MAX:"):
                try:
                    price_max = int(float(stripped.split(":")[1].strip()))
                except ValueError:
                    pass

        # Remove metadata lines from display
        display_lines = []
        for line in lines:
            s = line.strip()
            if (s.startswith("CONFIDENCE:") or
                s.startswith("PRICE_MIN:") or
                s.startswith("PRICE_MAX:")):
                continue
            display_lines.append(line)

        display_text = "\n".join(display_lines).strip()

        return {
            "text": display_text,
            "confidence": round(confidence, 1),
            "price_min": price_min,
            "price_max": price_max,
        }

    except Exception as e:
        return {
            "text": f"AI Error: {str(e)}",
            "confidence": 0,
            "price_min": 0,
            "price_max": 0,
        }
