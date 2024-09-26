import anthropic
import os
import sys
import glob

def get_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def scan_repository():
    terraform_files = glob.glob('**/*.tf', recursive=True)
    shell_scripts = glob.glob('**/*.sh', recursive=True)
    py_file = glob.glob('**/*.py', recursive=True)
    
    repo_content = "Terraform Files:\n"
    for tf_file in terraform_files:
        repo_content += f"\n--- {tf_file} ---\n"
        repo_content += get_file_contents(tf_file)
    
    repo_content += "\n\nShell Scripts:\n"
    for sh_file in shell_scripts:
        repo_content += f"\n--- {sh_file} ---\n"
        repo_content += get_file_contents(sh_file)
    
    repo_content += "\n\nPython:\n"
    for py_file in python_files:
        repo_content += f"\n--- {py_file} ---\n"
        repo_content += get_file_contents(py_file)
    
    return repo_content

def generate_readme():
    try:
        # Initialize the Anthropic client
        client = anthropic.Anthropic(api_key=os.environ['AI_API_KEY'])
        
        # Scan repository and get content
        repo_content = scan_repository()
        
        # Generate content for README using the Messages API
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=3000,
            messages=[
                {
                    "role": "user",
                    "content": f"""Based on the following repository content, generate a comprehensive README.md file. 
                    Include sections for Project Description, Installation, Usage, and Contributing. 
                    Make sure to accurately reflect the purpose and functionality of the scripts and Terraform configurations.
                    If there are multiple related Terraform files or scripts, group their descriptions logically.
                    
                    Repository Content:
                    {repo_content}
                    
                    Please generate the README.md content now:"""
                }
            ]
        )
        
        # Write the generated content to README.md
        with open('README.md', 'w') as f:
            f.write(message.content[0].text)
        
        print("README.md generated successfully based on repository content.")
    except Exception as e:
        print(f"Error generating README: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()
