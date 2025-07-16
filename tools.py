import base64
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

vision_llm = ChatOpenAI(model="gpt-4o")

def extract_text(img_path: str) -> str:
    """
    Extract text from an image file using a multimodal model.

    Args:
        img_path: A local image file path (string).

    Returns:
        Extracted text as a string.
    """
    try:
        with open(img_path, "rb") as image_file:
            image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        message = [
            HumanMessage(
                content=[
                    {"type": "text", "text": "Extract all text from this image. Return only the text."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
                ]
            )
        ]
        response = vision_llm.invoke(message)
        return response.content.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def divide(a: int, b: int) -> float:
    """
    Divide two numbers and return the result.

    Args:
        a: numerator
        b: denominator

    Returns:
        The division result as a float.
    """
    return a / b

tools = [divide, extract_text]
