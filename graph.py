from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.utils.function_calling import convert_to_openai_tool
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from agenttype import AgentState
from tools import tools

# Bind tools to LLM
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

# Assistant function
def assistant(state: AgentState):
    image = state["input_file"]
    sys_msg = SystemMessage(content=f"""You are a helpful agent that can analyze images and do math.\n
The current image is: {image}""")
    return {
        "messages": [llm_with_tools.invoke([sys_msg] + state["messages"])],
        "input_file": image
    }

# Build and compile LangGraph
def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")
    return builder.compile()
