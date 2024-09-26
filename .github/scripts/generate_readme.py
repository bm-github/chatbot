import anthropic
import os
import sys

def generate_readme():
    try:
        # Initialize the Anthropic client with the correct API key name
        client = anthropic.Anthropic(api_key=os.environ['AI_API_KEY'])
        
        # Generate content for README
        completion = client.completions.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens_to_sample=1000,
            prompt=f"{anthropic.HUMAN_PROMPT} Generate a README.md file for a GitHub repository. Include sections for Project Description, Installation, Usage, and Contributing.{anthropic.AI_PROMPT}",
        )
        
        # Write the generated content to README.md
        with open('README.md', 'w') as f:
            f.write(completion.completion)
        
        print("README.md generated successfully.")
    except Exception as e:
        print(f"Error generating README: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()
