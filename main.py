import os
import re
import openai
import json
import getpass
from colorama import Fore, Back, Style, init
import pyperclip
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

# Get the current user's username for the command prompt
username = getpass.getuser()

# Initialize colorama for colored terminal output
init(autoreset=True)

# Load your API key from the environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to select the chatbot model
def select_model():
    print(Fore.YELLOW + "Select the gpt model:")
    print(Back.GREEN + "1. ChatGpt")
    print(Back.BLACK + "2. GPT-4  ")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            return "gpt-3.5-turbo"
        elif choice == '2':
            return "gpt-4"
        else:
            print(Fore.RED + "Invalid input. Please enter 1 or 2.")

# Function to send the user's prompt to the selected model
def send_prompt(prompt, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )
    return response

# Function to print the response received from the chatbot model
def print_response(response, selected_model):
    if 'choices' in response:
        print(Style.NORMAL + Fore.BLUE + selected_model +": ")
        content = response["choices"][0]["message"]["content"]
        print(Style.BRIGHT + Fore.BLUE + content + "\n")
        return content
    else:
        print(Fore.RED + "Unexpected API response:")
        print(json.dumps(response, indent=2))
        return None

# Function to detect code blocks in the chatbot's response
def detect_code_blocks(text):
    triple_backticks = re.findall(r'```', text)
    if len(triple_backticks) % 2 != 0:
        print(Fore.YELLOW + "Warning: Code blocks may not be properly wrapped.")
    
    code_blocks = re.findall(r'```(?:[a-zA-Z]+\n)?([\s\S]*?)```', text)
    return code_blocks

# Function to display highlighted code blocks
def display_highlighted_code_block(code_block):
    highlighted_code = highlight(code_block, PythonLexer(), TerminalFormatter())
    print(highlighted_code)

# Function to allow the user to select a code block and copy it to the clipboard
def select_and_copy_code_block(code_blocks):
    if not code_blocks:
        return

    print(Fore.GREEN + "Detected code blocks:")
    for index, code_block in enumerate(code_blocks, 1):
        print(Fore.YELLOW + f"[{index}]")
        display_highlighted_code_block(code_block)
        print()

    while True:
        selected = input(Fore.WHITE + "Enter the number of the code block you want to copy, or type 'cancel': ")
        if selected.lower() == "cancel":
            break

        try:
            index = int(selected) - 1
            if 0 <= index < len(code_blocks):
                pyperclip.copy(code_blocks[index])
                print(Fore.GREEN + "Code block copied to clipboard.")
                break
            else:
                print(Fore.RED + "Invalid selection. Try again.")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.")

# Main function to run the GPT Terminal Prompt
def main():
    # print(Fore.YELLOW + "Welcome to the GPT Terminal Prompt!")
    selected_model = select_model()

    while True:
        prompt = input(Style.DIM + Fore.GREEN + username + ": " + Style.NORMAL)
        if prompt.lower() == "exit":
            break

        try:
            response = send_prompt(prompt, selected_model)
            content = print_response(response, selected_model)
            if content:
                code_blocks = detect_code_blocks(content)
                select_and_copy_code_block(code_blocks)
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()