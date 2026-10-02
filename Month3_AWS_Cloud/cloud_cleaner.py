import json
print("Loading external Infrastructure Configuration")
with open("infrastructure_config.json", "r", encoding="utf-8") as config_file:
   aws_instances = json.load(config_file)
print("[PLAYBOOK LOADED] Starting dynamic resource audit ...\n")

for instance in aws_instances:
    server_id = instance["instance_id"]
    current_status = instance["status"]
    env_tier = instance["environment"]

    if current_status == "running":
        print(f"Healthy [{env_tier}]: Target {server_id} is {current_status.upper()}.")
    elif current_status == "stopped":
        print(f"Warning [{env_tier}]: Target {server_id} is {current_status.upper()}. Needs to be restarted")
    elif current_status == "terminated":
       print(f"Action Required [{env_tier}]: Target {server_id} is {current_status.upper()}. Triggering AWS cleanup")
print("\n[PLAYBOOK COMPLETE] Dynamic resource audit completed successfully")