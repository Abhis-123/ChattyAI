# Chatbot with Microsoft's DialoGPT Model
This project implements a Chatbot using Microsoft's DialoGPT model and top_k sampling method. The model has been trained on a large corpus of conversational data to generate human-like responses to user input.

## Requirements
  . To run the Chatbot, you need to have the following:
  . Python 3.6 or later
  . PyTorch 1.6 or later
  . Transformers 4.0 or later
  . Flask
You can install the required Python packages using pip:
`pip install torch transformers flask`
# Usage
To start the Chatbot, run the app.py file: `python app.py`
This will start a Flask web application on http://localhost:5000/. You can open this URL in your browser to chat with the Chatbot.

The Chatbot will respond to your messages using the DialoGPT model and top_k sampling method. You can configure the top_k value in the config.py file. By default, the top_k value is set to 40.

# Acknowledgments
This project is based on the DialoGPT model developed by Microsoft Research. The model has been pre-trained on a large corpus of conversational data to generate human-like responses to user input. We thank Microsoft for making this model publicly available.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
