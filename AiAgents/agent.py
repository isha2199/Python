import ollama


# TOOL 1: Calculator
def calculator(expression):
    return eval(expression)


# TOOL 2: Weather
def get_weather(city):
    weather_data = {
        "mumbai": "32°C, sunny",
        "delhi": "28°C, cloudy",
        "bangalore": "24°C, rainy",
        "london": "15°C, cloudy"
    }

    return weather_data.get(
        city.lower(),
        "Weather information not available"
    )


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Start a conversation with the user
    messages = [
        {
            "role": "system",
            "content": """
            You are an AI agent with access to two tools.

            TOOL 1: calculator
            Use this for mathematical calculations.

            TOOL 2: weather
            Use this for weather questions.

            If you need a tool, respond EXACTLY like:

            TOOL: calculator
            INPUT: 2000 + 10

            OR:

            TOOL: weather
            INPUT: Mumbai

            If you already have enough information to answer,
            respond like:

            FINAL: Your answer here

            Do not add anything else.
            """
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    # AGENT LOOP
    while True:

        response = ollama.chat(
            model="qwen2.5:3b",
            messages=messages
        )

        ai_response = response["message"]["content"].strip()

        print("\nAI:", ai_response)

        # ---------------------------------
        # AI wants to use a tool
        # ---------------------------------

        if ai_response.startswith("TOOL:"):

            lines = ai_response.split("\n")

            tool = lines[0].replace("TOOL:", "").strip()
            tool_input = lines[1].replace("INPUT:", "").strip()

            # Execute calculator
            if tool == "calculator":

                result = calculator(tool_input)

            # Execute weather
            elif tool == "weather":

                result = get_weather(tool_input)

            else:

                result = "Unknown tool"

            print("Tool result:", result)

            # Give the result BACK to the AI
            messages.append({
                "role": "assistant",
                "content": ai_response
            })

            messages.append({
                "role": "user",
                "content": f"Tool result: {result}"
            })

            # Continue the agent loop
            continue

        # ---------------------------------
        # AI has final answer
        # ---------------------------------

        elif ai_response.startswith("FINAL:"):

            final_answer = ai_response.replace(
                "FINAL:",
                ""
            ).strip()

            print("\nFinal answer:", final_answer)

            break

        else:

            print("\nUnexpected response from AI.")
            break