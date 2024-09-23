import streamlit as st
import base64, os, requests
from PIL import Image

def encode_image(image_file):
    """Encode the image to base64."""
    try:
        return base64.b64encode(image_file.getvalue()).decode('utf-8')
    except Exception as e:
        st.error(f"Error encoding image: {e}")
        return None

def analyze_image(base64_image):
    """Make API request to analyze the image."""
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {os.environ.get('MISTRAL_API_KEY')}"}
    content = [
        {"type": "text", "text": "What's in this image?"},
        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
    ]
    data = {"messages": [{"role": "user", "content": content}], "model": "pixtral-12b-2409"}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error making API request: {e}")
    except KeyError:
        st.error("Invalid API response")
    return None

def main():
    st.title("Image Analysis App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.image(Image.open(uploaded_file), caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                base64_image = encode_image(uploaded_file)
                if base64_image:
                    result = analyze_image(base64_image)
                    if result:
                        st.subheader("Analysis Result:")
                        st.write(result)

if __name__ == '__main__':
    main()
