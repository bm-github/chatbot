import anthropic
import os
import sys

def generate_readme():
    try:
        # Initialize the Anthropic client
        client = anthropic.Anthropic(api_key=os.environ['AI_API_KEY'])
        
        # Generate content for README
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a README.md file for a GitHub repository. Include sections for Project Description, Installation, Usage, and Contributing."
                }
            ]
        )
        
        # Write the generated content to README.md
        with open('README.md', 'w') as f:
            f.write(message.content[0].text)
        
        print("README.md generated successfully.")
    except Exception as e:
        print(f"Error generating README: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()
