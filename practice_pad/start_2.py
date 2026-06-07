import ollama

model_list = ollama.list()

# print(model_list)

hello_chat = ollama.chat(

    model="llama3.2",
    messages=[
        {
            "role": "user",
            "message": "hi how are you doing "
        }
    ]
)

print(hello_chat)
modelfile = '''
FROM llama3.2

PARAMETER temperature 0.4

SYSTEM  A very smart assistant who answers question sincerly and informatively 



'''

new_model =  ollama.create(model="eaqubai", from_="llama3.2")