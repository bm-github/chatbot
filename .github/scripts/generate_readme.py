import anthropic
import os
import sys
import glob

def get_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def scan_repository():
    file_types = {
        'Terraform Files': '**/*.tf',
        'Terraform Variables Files': '**/*.tfvars',
        'Shell Scripts': '**/*.sh',
        'Python Scripts': '**/*.py'
    }
    
    repo_content = ""
    
    for file_type, glob_pattern in file_types.items():
        files = glob.glob(glob_pattern, recursive=True)
        if files:
            repo_content += f"\n{file_type}:\n"
            for file in files:
                repo_content += f"\n--- {file} ---\n"
                repo_content += get_file_contents(file)
    
    return repo_content.strip()

def generate_readme():
    try:
        # Initialize the Anthropic client
        client = anthropic.Anthropic(api_key=os.environ['AI_API_KEY'])
        
        # Scan repository and get content
        repo_content = scan_repository()
        
        # Only proceed if there's content to process
        if not repo_content:
            print("No .tf, .tfvars, .sh, or .py files found in the repository.")
            return
        
        # Generate content for README using the Messages API
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": f"""Based on the following repository content, generate a comprehensive README.md file. 
                    Include sections for Project Description, Installation, Usage, and Contributing. 
                    Only include information about file types that are present in the repository content provided.
                    Make sure to accurately reflect the purpose and functionality of the files present.
                    Group related files and their descriptions logically.
                    If Terraform files are present, explain the infrastructure being provisioned.
                    If shell scripts are present, explain their purpose and how to use them.
                    If Python scripts are present, explain their functionality and how they relate to the project.
                    
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
