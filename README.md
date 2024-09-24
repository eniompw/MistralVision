# Pixtral

This is a Streamlit-based web application that allows users to upload images and analyze them using the Mistral AI API.

## Features

- Upload images (JPG, JPEG, PNG)
- Display uploaded images
- Analyze images using Mistral AI's image recognition capabilities
- Show analysis results

## Requirements

- Python 3.7+
- Streamlit
- Pillow
- Requests

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/eniompw/MistralVision.git
   cd image-analysis-app
   ```

2. Install the required packages:
   ```bash
   pip install streamlit pillow requests
   ```

3. Set up your Mistral AI API key:
   - Sign up for an account at [Mistral AI](https://mistral.ai/)
   - Obtain your API key
   - Set the API key as an environment variable:
     ```bash
     export MISTRAL_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`)

3. Use the file uploader to select an image

4. Click the "Analyze Image" button to process the image and view the results

## How it works

1. The app uses Streamlit's file uploader to allow users to select an image file.
2. The uploaded image is displayed on the page.
3. When the user clicks "Analyze Image", the app encodes the image to base64.
4. The encoded image is sent to the Mistral AI API along with a prompt asking "What's in this image?".
5. The API response is processed and displayed on the page.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
