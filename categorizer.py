import os
import ollama

model = "eaqubai"

input_file = './data/grocery_list.txt'
output_file = './data/categorized_grocery_list.txt'


if not os.path.exists(input_file):
    print(f'input file {input_file} not found')
    exit(1)

with open(input_file, "r") as f:
    items = f.read().strip()
    print(type(items))


prompt = f""" you are an product categorized analyzer 

 here is a grocery list item and you'll categorized them into appropriate category such as produce, dairy, bevaraage and many more 
 then sort them alphabetically
 presetn the cateogry in a clear organization matter with bullet point or numbering 

"""

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print(generated_text)
except Exception as e:
    print("an error pccured", str(e))


