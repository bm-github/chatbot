# OpenAI ChatBot with Coding Assistance

This Python project provides a user-friendly graphical interface for interacting with OpenAI's GPT-3.5 language model. It allows you to engage in natural conversations, as well as receive assistance with code breakdown and commenting tasks.

## Project Description

The project consists of two Python scripts: `chat_Profile.py` and `chat_buttons.py`. Both scripts utilize the `tkinter` library to create a graphical user interface (GUI) and the `openai` library to interact with the OpenAI API.

### `chat_Profile.py`

This script allows you to have general conversations with the ChatGPT model, as well as perform specific tasks like code breakdown and professional profile generation.

### `chat_buttons.py`

Similar to `chat_Profile.py`, this script provides a chat interface with the OpenAI model. Additionally, it includes buttons for code breakdown and adding comments to code snippets.

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python packages by running the following command:

```
pip install openai tkinter
```

3. Obtain an API key from OpenAI by creating an account on their website (https://openai.com/).

## Usage

1. Run either `chat_Profile.py` or `chat_buttons.py` script using Python.
2. Upon the first run, you will be prompted to enter your OpenAI API key. Provide the key and click "Set API Key".
3. The main chat window will open, allowing you to interact with the ChatGPT model.
4. Type your message in the input text area and press "Send" or "Ctrl+Enter" to submit it.
5. The AI response will be displayed in the chat log.

### Additional Features

- **Save Conversation**: Saves the current conversation to a JSON file in the "history" subfolder.
- **Load Conversation**: Loads a previously saved conversation from the "history" subfolder.
- **Delete File**: Deletes a selected conversation file from the "history" subfolder.
- **Regenerate**: Generates a new response for the last user message.
- **Code Breakdown** (chat_Profile.py and chat_buttons.py): Instructs the model to break down and explain the provided code.
- **Create Profile** (chat_Profile.py): Generates a professional profile based on the provided input.
- **Add comments** (chat_buttons.py): Instructs the model to add comments to the provided code.
- **New Chat**: Starts a new conversation, clearing the chat log and conversation history.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.