import streamlit as st
import base64, os, requests
from PIL import Image

def encode_image(image_file):
    """Encode the image to base64."""
    return base64.b64encode(image_file.getvalue()).decode('utf-8')

def analyze_image(base64_image, user_text):
    """Make API request to analyze the image."""
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {os.environ.get('MISTRAL_API_KEY')}"}
    content = [
        {"type": "text", "text": user_text},
        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
    ]
    data = {"messages": [{"role": "user", "content": content}], "model": "pixtral-12b-2409"}

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def main():
    st.title("Pixtral Demo App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.image(Image.open(uploaded_file), caption="Uploaded Image", use_column_width=True)

        # Add a text input for the user to set their own text
        user_text = st.text_input("Enter your text prompt:", "What's in this image?")

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                base64_image = encode_image(uploaded_file)
                result = analyze_image(base64_image, user_text)
                st.subheader("Analysis Result:")
                st.write(result)

if __name__ == '__main__':
    main()
