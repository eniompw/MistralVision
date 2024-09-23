import streamlit as st
import base64
import os
from datetime import datetime
import requests
from PIL import Image
import io

def encode_image(image_file):
    """Encode the image to base64."""
    try:
        return base64.b64encode(image_file.getvalue()).decode('utf-8')
    except Exception as e:
        st.error(f"Error encoding image: {e}")
        return None

def main():
    st.title("Image Analysis App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                # Encode the image
                base64_image = encode_image(uploaded_file)
                if not base64_image:
                    st.error("Failed to encode image")
                    return

                # Make the API request
                url = "https://api.mistral.ai/v1/chat/completions"
                headers = {"Authorization": "Bearer " + str(os.environ.get("MISTRAL_API_KEY"))}
                text = {"type": "text", "text": "What's in this image?"}
                content = [text, {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}]
                data = {"messages": [{"role": "user", "content": content}], "model": "pixtral-12b-2409"}

                try:
                    response = requests.post(url, headers=headers, json=data)
                    response.raise_for_status()  # Raise an exception for bad status codes
                    response_json = response.json()

                    if 'choices' not in response_json:
                        st.error("Invalid API response")
                        return

                    response_content = response_json["choices"][0]["message"]["content"]
                    st.subheader("Analysis Result:")
                    st.write(response_content)

                except requests.exceptions.RequestException as e:
                    st.error(f"Error making API request: {e}")

if __name__ == '__main__':
    main()
