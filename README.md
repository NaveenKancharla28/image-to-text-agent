# 🧠 Image-to-Text Agent

This is an intelligent agent that can analyze images containing text (like handwritten notes or meal plans) and extract meaningful content from them using LangChain and OpenAI.

> Example Use Case: Upload a handwritten meal plan image and the agent will tell you what groceries you need to buy.

---

## 🚀 Features

- 🖼️ Converts handwritten or printed images into text
- 🧠 Uses LangChain’s agentic framework with OpenAI Vision (GPT-4o)
- 🔍 Capable of answering natural language questions based on the image content
- 🛠️ Modular codebase: easy to extend with your own tools or prompts

---

## 📂 Project Structure

├── agent_app.py # Main file to run the agent
├── agenttype.py # Defines the agent logic (react-style)
├── graph.py # Connects tools and message flow
├── tools.py # Custom tools (image input, etc.)
├── Batman_training_and_meals.png # Sample image to test
├── .env # Contains your OpenAI API key (not committed)

