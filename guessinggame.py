import random

print("🎱 Welcome to the Magic 8-Ball Game!")
print("Ask me a question and I will reveal your fate...")
print("Type 'quit' to exit.\n")

responses = [
    "Yes, definitely! ✅",
    "No way! ❌",
    "Maybe... 🤔",
    "Ask again later ⏳",
    "It is certain. 🌟",
    "I wouldn't count on it. 💀",
    "Signs point to yes. 👍",
    "Very doubtful. 😒"
]

while True:
    question = input("❓ Your question: ")
    
    if question.lower() == "quit":
        print("Goodbye! 👋")
        break
    
    print("Thinking... 🤔")
    print(random.choice(responses))
    print()
