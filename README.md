# Project Description

This repository contains a collection of Terraform configurations, shell scripts, Python scripts, and Terraform variable files. The main purpose of these files is to interact with and support various automation and deployment tasks.

## Terraform Files

The Terraform files in this repository are responsible for provisioning and managing infrastructure resources across different cloud providers or on-premises environments. These files define the desired state of the infrastructure using Hashicorp Configuration Language (HCL).

## Terraform Variable Files

The Terraform variable files (`.tfvars`) contain values for input variables used by the Terraform configurations. These files allow you to customize the deployment by providing specific values for variables such as resource names, sizes, and other configuration options.

## Shell Scripts

The shell scripts in this repository are designed to automate various tasks related to the Terraform deployments. These scripts can perform actions like initializing Terraform working directories, applying or destroying infrastructure, and executing other necessary operations.

## Python Scripts

There are two Python scripts included in this repository:

### chat_Profile.py

This script provides a graphical user interface (GUI) for interacting with the OpenAI GPT-3.5 language model. The main features include:

- **Conversation Management**: Save, load, and delete conversation histories as JSON files in the `history` subfolder.
- **System Message Presets**: Buttons to set specific system messages for code breakdown and professional profile generation.
- **Chat Interface**: A scrollable text area to display the conversation between the user and the AI assistant.
- **Regenerate Response**: A button to regenerate the AI assistant's response for the current conversation.

### chat_buttons.py

This script is similar to `chat_Profile.py` but with additional features:

- **Add Comments**: A button to set the system message to "Add comments above each line of code."
- **Code Breakdown**: A button to set the system message for breaking down submitted code.

Both Python scripts require an OpenAI API key to be entered upon initial execution. The scripts save and load conversation histories as JSON files in the `history` subfolder, which can be managed through the GUI.

## Usage

1. Set up the required dependencies and configurations for Terraform and the cloud provider(s) you plan to use.
2. Review and customize the Terraform configuration files and variable files according to your infrastructure requirements.
3. Execute the shell scripts or use the Terraform CLI to apply the desired configurations and provision the infrastructure resources.
4. For the Python scripts, make sure you have the required dependencies (e.g., `tkinter`, `openai`) installed. Run the scripts and enter your OpenAI API key when prompted. You can then interact with the GUI to have conversations with the AI assistant, save and load conversation histories, and utilize the various features provided by the scripts.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b my-new-feature`
3. Make the necessary changes and commit them: `git commit -am 'Add some feature'`
4. Push your changes to the branch: `git push origin my-new-feature`
5. Submit a pull request detailing your changes.

Please ensure that your contributions align with the project's coding standards and guidelines.