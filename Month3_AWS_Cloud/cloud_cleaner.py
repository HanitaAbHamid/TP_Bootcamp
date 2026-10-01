import json
print("Loading external Infrastructure Configuration")
with open("infrastructure_config.json", "r", encoding="utf-8") as config_file:
   aws_instances = json.load(config_file)
print("[PLAYBOOK LOADED] Starting dynamic resource audit ...\n")

for instance in aws_instances:
    server_id = instance["instance_id"]
    current_status = instance["status"]
    env_tier = instance["environment"]

    if current_status != "running":
        print(f"Action Required [{env_tier}]:Target {server_id} is {current_status.upper()}.")
    else:
        print(f"No Action Required [{env_tier}]: Target {server_id} is {current_status.upper()}.")

print("\n[PLAYBOOK COMPLETE] Dynamic resource audit completed successfully.")