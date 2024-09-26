# Project Description

This repository contains Python scripts for building a simple chatbot application using the OpenAI GPT-3.5-turbo language model. The application allows users to interact with the chatbot through a graphical user interface (GUI) built with the Tkinter library.

# Installation

1. Ensure you have Python installed on your system. This project was built using Python 3.7 or higher.

2. Install the required Python packages:

```
pip install openai tkinter
```

3. Obtain an API key from OpenAI by creating an account at https://beta.openai.com/signup/.

# Usage

1. Run either the `chat_Profile.py` or `chat_buttons.py` script to launch the chatbot application.

2. Upon launching, the application will prompt you to enter your OpenAI API key. Enter the API key you obtained from OpenAI, and the main chat window will open.

3. The chat window consists of the following components:
   - **Chat Log**: Displays the conversation history between you and the chatbot.
   - **Entry Text Box**: Enter your message or prompt for the chatbot here.
   - **Send Button**: Click this button or press Ctrl+Enter to send your message to the chatbot.
   - **Regenerate Button**: Click this button to regenerate the chatbot's response based on the conversation history.
   - **Function Buttons**: Buttons that change the chatbot's behavior or purpose. The available buttons may vary between the scripts.
   - **New Chat Button**: Click this button to start a new conversation, clearing the chat log.
   - **File List Box**: Displays a list of saved conversation files. You can load or delete a conversation file from here.
   - **Save Conversation Button**: Click this button to save the current conversation to a file.
   - **Load Conversation Button**: Click this button to load a previously saved conversation from the selected file.
   - **Delete File Button**: Click this button to delete the selected conversation file.

4. The `chat_Profile.py` script includes the following function buttons:
   - **Code Breakdown**: Prompts the chatbot to provide an explanation or breakdown of the submitted code.
   - **Create Profile**: Prompts the chatbot to generate a professional profile in British English, adhering to specific guidelines.

5. The `chat_buttons.py` script includes the following function buttons:
   - **Code Breakdown**: Prompts the chatbot to provide an explanation or breakdown of the submitted code.
   - **Add comments**: Prompts the chatbot to add comments to the submitted code, with each comment on a single line above the corresponding line of code.

6. Saved conversation files are stored in the `history` subfolder within the same directory as the script. These files can be loaded, deleted, or overwritten as needed.

# Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the repository.