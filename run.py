from inventory_agent.agent import agent

def main():
    print("Inventory Agent is ready. Type your query.")
    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        response = agent.run(user_input)
        print("🤖 Agent:", response)

if __name__ == "__main__":
    main()
