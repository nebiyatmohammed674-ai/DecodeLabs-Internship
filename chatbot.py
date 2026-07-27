"""
DecodeLabs Project 1: Deterministic Rule-Based Chatbot
"""


def get_bot_response(user_input: str) -> str:
    """
    Evaluates normalized input against predefined rules.
    """
    cleaned_input = user_input.lower().strip()

    # Rule 1: Empty Input
    if not cleaned_input:
        return "Input empty. Please enter a valid query."

    # Rule 2: Greetings
    if cleaned_input in ["hello", "hi", "hey", "selam"]:
        return "Greetings. How may I assist you?"

    # Rule 3: Identity
    if "your name" in cleaned_input or "who are you" in cleaned_input:
        return "I am a System 2 Rule-Based Chatbot for DecodeLabs Project 1."

    # Rule 4: System Status
    if "how are you" in cleaned_input or "status" in cleaned_input:
        return "System status: Operational."

    # Rule 5: Capabilities
    if "help" in cleaned_input or "what can you do" in cleaned_input:
        return "Supported commands: greetings, status check, identity verification."

    # Fallback response for unmatched input
    return "Query not recognized. Please rephrase."


def run_chatbot() -> None:
    """
    Executes the interactive command-line interface loop.
    """
    print("--- DecodeLabs Rule-Based AI CLI ---")
    print("Type 'exit' to terminate session.\n")

    while True:
        try:
            user_input = input("User > ")

            if user_input.lower().strip() in ["exit", "quit", "bye"]:
                print("System > Session terminated. Goodbye.")
                break

            response = get_bot_response(user_input)
            print(f"System > {response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nSystem > Force terminated.")
            break


if __name__ == "__main__":
    run_chatbot()