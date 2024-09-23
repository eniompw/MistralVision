from flask import Flask, request, render_template, redirect, url_for
import base64, os
from datetime import datetime
import requests  # Import the requests library for API calls

app = Flask(__name__)

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if not (image_data := request.form.get('image')):
            return "No image data received", 400
        
        try:
            # Ensure the static/uploads directory exists
            os.makedirs(os.path.join('static', 'uploads'), exist_ok=True)
            
            filename = f"image_{datetime.now():%Y%m%d_%H%M%S}.png"
            file_path = os.path.join('static', 'uploads', filename)  # Save to static/uploads
            with open(file_path, 'wb') as f:
                f.write(base64.b64decode(image_data.split(',')[1]))
            
            # Encode the image and make the API request
            base64_image = encode_image(file_path)
            if not base64_image:
                return "Failed to encode image", 500

            url = "https://api.mistral.ai/v1/chat/completions"
            headers = {"Authorization": "Bearer " + str(os.environ.get("MISTRAL_API_KEY"))}
            text = {"type": "text", "text": "What's in this image?"}
            content = [text, {"type": "image_url", "image_url":  f"data:image/jpeg;base64,{base64_image}"}]
            data = {"messages": [{"role": "user", "content": content}], "model": "pixtral-12b-2409"}

            response = requests.post(url, headers=headers, json=data)
            response_json = response.json()
            
            # Log the entire response for debugging
            app.logger.debug(f"API Response Content: {response.content}")

            if 'choices' not in response_json:
                app.logger.error("API response does not contain 'choices'")
                return "Invalid API response", 500

            response_content = response_json["choices"][0]["message"]["content"]
            
            return render_template('index.html', filename=filename, response_content=response_content)
        except Exception as e:
            app.logger.error(f"Error uploading image: {e}")
            return "An error occurred while uploading the image", 500
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)  # Ensure the static/uploads directory exists
    app.run(debug=True)
