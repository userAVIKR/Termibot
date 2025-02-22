

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below:

Here is the conversation history: {context}

Question: {question}

Answer:

"""

chat_prompt_template = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")
chain = chat_prompt_template | model 

def handle_conversation():
    context = ""
    print("Welcome to the chatbot! Type exit to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)
        context += f"User: {user_input}\nBot: {result}\n"

if __name__ == "__main__":
    handle_conversation()