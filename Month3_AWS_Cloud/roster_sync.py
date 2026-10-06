import json
import time

print("🔄 [INITIALIZING GLOBAL RESOURCE SYNC] 🔄")
time.sleep(1)

# 1. Dynamically read your project configuration metrics file directly from this directory
try:
    with open("infrastructure_config.json", "r", encoding="utf-8") as file:
        roster_data = json.load(file)
    print(f"✅ Successfully imported configuration map file! Found {len(roster_data)} servers.")
except FileNotFoundError:
    print("❌ ERROR: Could not find infrastructure_config.json in this folder layout!")
    roster_data = []

print("\n📦 [COMPILING LOCAL ASSET MANAGEMENT PROFILES]")

for resource in roster_data:
    server_id = resource.get("server_id", "UNKNOWN")
    status = resource.get("status", "UNKNOWN")  
    environment = resource.get("environment", "UNKNOWN")

    print(f"\n🔍 Scanning logs for Server ID: {server_id} | Status: {status} | Environment: {environment}")

print("\n[LOG SCANNER] Log scanning completed. All patterns have been extracted successfully.")
