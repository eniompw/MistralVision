# Mistral Vision

This is a Flask web application that allows users to upload images by pasting them into a designated area on the webpage. The uploaded images are then sent to an external API for analysis, and the results are displayed back to the user.

## Features

- **Image Upload**: Users can paste an image directly into the webpage.
- **Image Encoding**: The pasted image is encoded to base64 format.
- **API Integration**: The encoded image is sent to the Mistral API for analysis.
- **Result Display**: The API response is displayed on the webpage along with the uploaded image.

## Requirements

- Python 3.x
- Flask
- Requests

## Usage

1. Open the application in your web browser.
2. Paste an image into the designated area on the webpage.
3. Click the "Upload Image" button.
4. The uploaded image and the API response will be displayed on the page.

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The main template for the image upload page.
- `static/uploads/`: Directory where uploaded images are saved.

## License

This project is licensed under the MIT License.
