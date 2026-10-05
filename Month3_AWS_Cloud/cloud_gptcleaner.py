import json

print("🔄 [LOADING EXTERNAL INFRASTRUCTURE CONFIGURATION] 🔄")

# 1. Open and read the external JSON configuration playbook safely
with open("infrastructure_config.json", "r", encoding="utf-8") as config_file:
    # Transform the text file data back into a clean Python list
    aws_instances = json.load(config_file)

print("📝 [PLAYBOOK LOADED] Starting dynamic resource audit...\n")

# 2. Iterate through our newly loaded database fleet
for instance in aws_instances:
    server_id = instance["instance_id"]
    current_status = instance["status"]
    env_tier = instance["environment"]
    
    # Automation logic: identify non-running targets for dynamic cleanup actions
    if current_status != "running":
        print(f"🛑 ACTION REQUIRED [{env_tier}]: Target {server_id} is {current_status.upper()}. Triggering AWS stop/cleanup script sequence...")
    else:
        print(f"🟢 STABLE [{env_tier}]: Target {server_id} is actively running traffic.")

print("\n✨ Dynamic infrastructure cleanup check complete!")
