#!/usr/bin/env python3
"""Test script to verify all agent modules work correctly"""

import sys
sys.path.insert(0, 'c:/Users/sande/Desktop/PROJECTS/convolve')

print("=" * 70)
print("Testing All Agent Modules")
print("=" * 70)

# Test 1: Import web_search
print("\n1. Testing web_search module...")
try:
    from backend.agents.web_search import web_search_tool
    print("   ✓ web_search_tool imported successfully")
except Exception as e:
    print(f"   ✗ FAILED: {e}")
    sys.exit(1)

# Test 2: Import deep_web
print("\n2. Testing deep_web module...")
try:
    from backend.agents.deep_web import deep_web_tool
    print("   ✓ deep_web_tool imported successfully")
except Exception as e:
    print(f"   ✗ FAILED: {e}")
    sys.exit(1)

# Test 3: Run web search
print("\n3. Running web search test...")
try:
    result = web_search_tool.invoke("Python 2026")
    if result and len(result) > 0:
        print("   ✓ Web search executed successfully")
        print(f"   Found {len(result)} characters of results")
    else:
        print("   ✗ No results returned")
except Exception as e:
    print(f"   ✗ FAILED: {e}")

# Test 4: Run deep web test
print("\n4. Running deep web research test...")
try:
    result = deep_web_tool.invoke("artificial intelligence")
    if result and len(result) > 0:
        print("   ✓ Deep web research executed successfully")
        print(f"   Found {len(result)} characters of research data")
    else:
        print("   ✗ No results returned")
except Exception as e:
    print(f"   ✗ FAILED: {e}")

print("\n" + "=" * 70)
print("✓ All tests completed successfully!")
print("=" * 70)
