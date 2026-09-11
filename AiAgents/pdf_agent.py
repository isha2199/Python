import ollama
from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    """Read the text from a PDF file."""

    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


tools = [read_pdf]

available_functions = {
    "read_pdf": read_pdf
}

user_input = input("You: ")

messages = [
    {
        "role": "user",
        "content": user_input
    }
]

while True:

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=messages,
        tools=tools
    )

    messages.append(response.message)

    if response.message.tool_calls:

        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print("\nAI wants to use:", function_name)
            print("Arguments:", arguments)

            function = available_functions[function_name]

            result = function(**arguments)

            print("Tool result:")
            print(result[:500])

            messages.append({
                "role": "tool",
                "tool_name": function_name,
                "content": result
            })
        continue

    else:
        print("\nAI:", response.message.content)
        break