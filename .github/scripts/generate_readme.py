import anthropic
import os
import sys

def generate_readme():
    try:
        # Initialize the Claude client
        client = anthropic.Client(api_key=os.environ['CLAUDE_API_KEY'])
        
        # Generate content for README
        response = client.completion(
            prompt="Generate a README.md file for a GitHub repository. Include sections for Project Description, Installation, Usage, and Contributing.",
            model="claude-3-opus-20240229",  # Use the latest available model
            max_tokens_to_sample=1000,
        )
        
        # Write the generated content to README.md
        with open('README.md', 'w') as f:
            f.write(response.completion)
        
        print("README.md generated successfully.")
    except Exception as e:
        print(f"Error generating README: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()