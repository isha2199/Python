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
# Available tools
# -----------------------------

tools = [
    calculator,
    get_weather,
    greet
]


available_functions = {
    "calculator": calculator,
    "get_weather": get_weather,
    "greet": greet
}


# -----------------------------
# USER INPUT
# -----------------------------

user_input = input("You: ")

messages = [
    {
        "role": "user",
        "content": user_input
    }
]


# -----------------------------
# AGENT LOOP
# -----------------------------

while True:

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=messages,
        tools=tools
    )

    # Add AI response to conversation
    messages.append(response.message)


    # --------------------------------
    # Did AI request a tool?
    # --------------------------------

    if response.message.tool_calls:

        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print("\nAI wants to use:", function_name)
            print("Arguments:", arguments)

            # Find the correct Python function
            function = available_functions[function_name]

            # Execute function
            result = function(**arguments)

            print("Tool result:", result)

            # Send result back to AI
            messages.append({
                "role": "tool",
                "tool_name": function_name,
                "content": result
            })

        # Go back to the top of the loop
        continue


    # --------------------------------
    # No tool needed → final answer
    # --------------------------------

    else:

        print("\nAI:", response.message.content)

        break