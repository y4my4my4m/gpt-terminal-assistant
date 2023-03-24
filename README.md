# GPT Terminal Prompt

A Python script that uses OpenAI's GPT models to generate text based on user input. Users can interact with the GPT engine and select code blocks returned by the model.

## Installation

1. Clone the repository or download the script files.
`git clone https://github.com/y4my4my4m/gpt-terminal-assistant.git`

2. Install the required Python packages using `requirements.txt`:
`pip install -r requirements.txt`

3. Set the environment variable for your OpenAI API key. You can find your API key in the OpenAI platform's dashboard.

   - For Linux or macOS:
     - `export OPENAI_API_KEY="your-api-key"`
   - For Windows:
     - `set OPENAI_API_KEY="your-api-key"`

## Usage

Run the script using Python:

`python main.py`

1. When prompted, select the chatbot engine you want to use (1 for chatGpt, 2 for GPT-4).
2. Type your prompt and press Enter **WHEN ON A NEW LINE**. The GPT model will generate a response.
3. If there are code blocks in the response, you can choose one to copy to the clipboard.
4. Type 'exit' to quit the program.

## Convenience

Personally, I've added the following to my `~/.zshrc` for ease of use:
`alias chatgpt='env OPENAI_API_KEY=MY-API-KEY python ~/gpt-terminal-assistant/main.py'`

## License

This project is licensed under the MIT License.
