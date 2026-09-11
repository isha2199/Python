import ollama


# -----------------------------
# TOOL 1: Calculator
# -----------------------------

def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    return str(eval(expression))


# -----------------------------
# TOOL 2: Weather
# -----------------------------

def get_weather(city: str) -> str:
    """Get the weather for a city."""

    weather_data = {
        "mumbai": "32°C, sunny",
        "delhi": "28°C, cloudy",
        "bangalore": "24°C, rainy",
        "london": "15°C, cloudy"
    }

    return weather_data.get(
        city.lower(),
        "Weather information not available."
    )


# -----------------------------
# TOOL 3: Greeting
# -----------------------------

def greet(name: str) -> str:
    """Give someone a friendly greeting."""
    return f"Hello {name}! Nice to meet you."


# -----------------------------
# Give all tools to Qwen
# -----------------------------

tools = [
    calculator,
    get_weather,
    greet
]


# Map function names to functions
available_functions = {
    "calculator": calculator,
    "get_weather": get_weather,
    "greet": greet
}


# -----------------------------
# Agent
# -----------------------------

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages = [
        {
            "role": "user",
            "content": user_input
        }
    ]

    # Ask Qwen what to do
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=messages,
        tools=tools
    )

    # Add Qwen's response to conversation
    messages.append(response.message)

    # Did Qwen request a tool?
    if response.message.tool_calls:

        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print("\nAI chose:", function_name)
            print("Arguments:", arguments)

            # Find the Python function
            function = available_functions[function_name]

            # Execute it
            result = function(**arguments)

            print("Tool result:", result)

            # Send result back to Qwen
            messages.append({
                "role": "tool",
                "tool_name": function_name,
                "content": result
            })

        # Ask Qwen for final answer
        final_response = ollama.chat(
            model="qwen2.5:3b",
            messages=messages,
            tools=tools
        )

        print("\nAI:", final_response.message.content)

    else:

        print("\nAI:", response.message.content)