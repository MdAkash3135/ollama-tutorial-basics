import ollama

model_list = ollama.list()

# print(model_list)

hello_chat = ollama.chat(

    model="llama3.2",
    messages=[
        {
            "role": "user",
            "message": "hi"
        }
    ]
)

print(hello_chat)