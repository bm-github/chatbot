import tkinter as tk
from tkinter import scrolledtext, Menu, Listbox, Button
import tkinter.font as tkfont
import openai
import json
import os
import re

# Initialize global variables
api_key_window = None
api_key_entry = None

# Define the system message
system_message = "You are a friendly chatbot called BrendenBot."

# Initialize the conversation history
conversation = []

# Counter for conversation file names
file_counter = 1

# Define file_listbox and chat_log as global variables
file_listbox = None
chat_log = None

# Define a variable to store the current loaded file name
current_loaded_file = None

# Store filenames (including extensions) in a list
file_list = []

def code_system_message():
    global system_message
    system_message = "Breakdown the submitted code"
    send_message(entry)  # Send the prompt with the updated system message

def profile_system_message():
    global system_message
    system_message = "You will create a professional profile up to 150 words in British English. Write in the third person. Avoid using is a highly skilled or highly experienced in the opening sentence and avoid repitition."
    send_message(entry)  # Send the prompt with the updated system message


# Function to send a message when Ctrl-Enter is pressed and without a new line
def send_message_on_ctrl_enter(event):
    if event.state == 4:  # Check if the Ctrl key is held down (Ctrl modifier has state 4)
        send_message(entry)
        return 'break'  # This prevents the default newline behavior

def set_api_key():
    api_key = api_key_entry.get()
    openai.api_key = api_key
    api_key_window.destroy()
    initialize_chat_window()

def send_message(entry):
    global chat_log, conversation

    user_message = entry.get("1.0", tk.END).strip()
    entry.delete("1.0", tk.END)

# Initialize the conversation history with the system message
    conversation.append({"role": "system", "content": system_message})
    conversation.append({"role": "user", "content": user_message})

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_message}\n", "user")
    chat_log.config(state=tk.DISABLED)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=conversation
    )

    ai_response = completion['choices'][0]['message']['content']

    conversation.append({"role": "assistant", "content": ai_response})

    update_chat_log()


def regenerate_response():
    global chat_log, conversation

    if conversation:
        conversation.pop()

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        ai_response = completion['choices'][0]['message']['content']

        conversation.append({"role": "assistant", "content": ai_response})

        update_chat_log()

# Function to sanitize a string for use as a filename
def sanitize_filename(filename):
    # Remove non-alphanumeric characters, spaces, and newlines
    sanitized_filename = re.sub(r'[^\w\s-]', '', filename)
    sanitized_filename = sanitized_filename.replace(' ', '_')
    sanitized_filename = sanitized_filename.replace('\n', '')

    # Truncate to the first 20 characters
    return sanitized_filename[:20]

# Function to save a conversation
def save_conversation():
    global conversation

    if not conversation:
        return  # Do nothing if the conversation is empty

    user_message = conversation[1]["content"]

    # Specify the subfolder "history" as part of the file path
    history_subfolder = "history"
    if not os.path.exists(history_subfolder):
        os.makedirs(history_subfolder)

    # Sanitize the user_message for use as a filename
    sanitized_user_message = sanitize_filename(user_message)

    # Use the sanitized user_message as the filename without an extension
    filename = sanitized_user_message

    # Specify the file path within the "history" subfolder
    file_path = os.path.join(history_subfolder, filename)

    # Check if the file already exists; if yes, increment the filename
    counter = 1
    while os.path.exists(file_path):
        filename = f"{sanitized_user_message}_{counter}"
        file_path = os.path.join(history_subfolder, filename)
        counter += 1

    with open(file_path, 'w') as file:
        json.dump(conversation[1:], file)
    update_file_listbox()  # Update the listbox after saving


def load_conversation(file_path):
    global conversation

    with open(file_path, 'r') as file:
        conversation = json.load(file)

def load_conversation_from_file(filename):
    global conversation

    if filename:
        # Specify the subfolder "history" as part of the file path
        file_path = os.path.join("history", filename)
        conversation = []  # Clear existing conversation
        load_conversation(file_path)
        update_chat_log()

def delete_json_file(filename):
    global file_list

    # Specify the subfolder "history" as part of the file path
    file_path = os.path.join("history", filename)
    
    try:
        os.remove(file_path)
        # Remove the deleted filename from the file_list
        if filename in file_list:
            file_list.remove(filename)
        update_file_listbox()
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"File '{filename}' not found.")
    except Exception as e:
        # Handle other exceptions that might occur during file deletion
        print(f"An error occurred while deleting '{filename}': {str(e)}")

def update_chat_log():
    global chat_log, conversation

    chat_log.config(state=tk.NORMAL)
    chat_log.delete("1.0", tk.END)
    for message in conversation:
        if message["role"] == "user":
            chat_log.insert(tk.END, f"{message['content']}\n", "user")
        elif message["role"] == "assistant":  # Only display assistant's messages
            chat_log.insert(tk.END, f"{message['content']}\n", "assistant")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)

def update_file_listbox():
    global file_listbox, file_list

    # Clear the current listbox items
    file_listbox.delete(0, tk.END)

    # Specify the subfolder "history" as part of the file path
    history_subfolder = os.path.join(os.getcwd(), "history")

    # List all files in the "history" subfolder
    file_list = [filename for filename in os.listdir(history_subfolder)]

    # Add filenames (including extensions) to the Listbox
    for filename in file_list:
        file_listbox.insert(tk.END, filename)

def start_new_check():
    global conversation, current_loaded_file

    if conversation:
        save_conversation()

    conversation.clear()
    current_loaded_file = None  # Clear the current loaded file name
    chat_log.config(state=tk.NORMAL)
    chat_log.delete("1.0", tk.END)
    chat_log.config(state=tk.DISABLED)

def initialize_chat_window():
    global chat_log, entry, file_listbox, conversation

    root = tk.Tk()
    root.title("OpenAI Brendenbot")

    file_frame = tk.Frame(root, width=200)
    file_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create the Listbox with grey background, white text, and Arial font
    listbox_font = tkfont.Font(family="Arial", size=12)
    global file_listbox
    file_listbox = Listbox(file_frame, bg="gray", fg="white", font=listbox_font)
    file_listbox.pack(fill=tk.BOTH, expand=True)
    update_file_listbox()

    def load_selected_conversation():
        selected_index = file_listbox.curselection()
        if selected_index:
            selected_filename = file_listbox.get(selected_index[0])  # Get the selected filename
            load_conversation_from_file(selected_filename)

    save_button = Button(file_frame, text="Save Conversation", command=save_conversation)
    save_button.pack(fill=tk.BOTH)

    load_button = Button(file_frame, text="Load Conversation", command=load_selected_conversation)
    load_button.pack(fill=tk.BOTH)

    def delete_selected_file():
        selected_index = file_listbox.curselection()
        if selected_index:
            selected_filename = file_listbox.get(selected_index[0])  # Get the selected filename
            delete_json_file(selected_filename)

    # Create a "Delete File" button
    delete_button = Button(file_frame, text="Delete File", command=delete_selected_file)
    delete_button.pack(fill=tk.BOTH)

    menu = Menu(root)
    root.config(menu=menu)
    conversation_menu = Menu(menu)
    menu.add_cascade(label="Conversation", menu=conversation_menu)
    conversation_menu.add_command(label="Load File", command=load_selected_conversation)
    conversation_menu.add_command(label="Delete Selected File", command=delete_selected_file)
    conversation_menu.add_separator()
    conversation_menu.add_command(label="Exit", command=root.destroy)

    chat_log = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, bg="light green", fg="black")
    chat_log.pack(expand=True, fill="both")

    user_font = tkfont.Font(family="Arial", size=12, weight="bold")
    assistant_font = tkfont.Font(family="Arial", size=12, slant="italic")

    chat_log.tag_configure("user", justify='left', foreground='white', font=user_font)
    chat_log.tag_configure("assistant", justify='left', foreground='black', font=assistant_font)

    entry = tk.Text(root, height=5)
    entry.pack(expand=True, fill="both", padx=10, pady=10)
    entry.focus_set()

    h_scrollbar = tk.Scrollbar(entry, orient=tk.HORIZONTAL)
    v_scrollbar = tk.Scrollbar(entry, orient=tk.VERTICAL)
    entry.config(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
    h_scrollbar.config(command=entry.xview)
    v_scrollbar.config(command=entry.yview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    regenerate_button = Button(root, text="Regenerate", font=user_font, command=regenerate_response)
    regenerate_button.pack(side=tk.LEFT)

    code_system_button = Button(root, text="Code Breakdown", font=user_font, command=code_system_message)
    code_system_button.pack(side=tk.LEFT)

    profile_system_button = Button(root, text="Create Profile", font=user_font, command=profile_system_message)
    profile_system_button.pack(side=tk.LEFT)

    new_check_button = Button(root, text="New Chat", font=user_font, command=start_new_check)
    new_check_button.pack(side=tk.RIGHT)

    send_button = Button(root, text="   Send   ", font=user_font, command=lambda: send_message(entry))
    send_button.pack(side=tk.BOTTOM, fill=tk.X)

    # Bind Ctrl-Enter to send_message_on_ctrl_enter
    entry.bind('<Control-Return>', send_message_on_ctrl_enter)

    # Set the system message to "You are a friendly chatbot"
    #conversation.append({"role": "system", "content": "You are a friendly chatbo"})

    root.mainloop()

# Function to handle Enter key in the API key entry
def handle_api_key_entry(event):
    set_api_key()

# Initialize the API key input window
def initialize_api_key_window():
    global api_key_window, api_key_entry

    api_key_window = tk.Tk()
    api_key_window.title("API Key Input")

    api_key_label = tk.Label(api_key_window, text="Enter your OpenAI API key:")
    api_key_label.pack()

    api_key_entry = tk.Entry(api_key_window)
    api_key_entry.pack()
    api_key_entry.focus_set()

    api_key_button = tk.Button(api_key_window, text="Set API Key", command=set_api_key)
    api_key_button.pack()

    # Bind Enter key to handle_api_key_entry
    api_key_entry.bind('<Return>', handle_api_key_entry)

    api_key_window.mainloop()

# Initialize the API key input window
initialize_api_key_window()
