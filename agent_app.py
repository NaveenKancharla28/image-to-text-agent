import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from graph import build_graph

load_dotenv()

react_graph = build_graph()

file_path = os.path.join(os.getcwd(), "Batman_training_and_meals.png")

messages = [HumanMessage(content="According to the image, what items do I need to buy for dinner?")]

result = react_graph.invoke({
    "messages": messages,
    "input_file": file_path
})

for m in result["messages"]:
    print(m.content)
