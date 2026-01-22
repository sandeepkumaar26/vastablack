"""
Simple test script to verify the agent works correctly
"""
from langchain_core.messages import HumanMessage

print("Testing Agent Build...")

try:
    from backend.agents.agent import build_agent
    
    print("✅ Agent module imported successfully")
    
    # Build the agent
    agent = build_agent()
    print("✅ Agent built successfully")
    
    # Test with a simple query
    test_query = "What is the capital of France?"
    print(f"\nTesting with query: '{test_query}'")
    
    result = agent.invoke({"messages": [HumanMessage(content=test_query)]})
    
    # Extract the final response
    final_message = result["messages"][-1]
    response = final_message.content
    
    print("\n--- Agent Response ---")
    print(response)
    print("\n✅ Test completed successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
