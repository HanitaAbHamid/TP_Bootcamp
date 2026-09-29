# A list containing multiple server metadata dictionaries
aws_fleet = [
    {"instance_id": "i-111", "status": "running", "type": "t3.micro"},
    {"instance_id": "i-222", "status": "stopped", "type": "t3.medium"},
    {"instance_id": "i-333", "status": "running", "type": "m5.large"},
    {"instance_id": "i-444", "status": "terminated", "type": "t3.micro"}
]

print("--- STARTING FLEET INTEGRITY AUDIT ---")

# The DevOps loop: Iterating through each server dictionary in our fleet list
for server in aws_fleet:
    server_id = server["instance_id"]
    current_status = server["status"]
    
    # Check if the server requires an operator alert
    if current_status != "running":
        print(f"⚠️ ALERT: Server {server_id} is {current_status.upper()}! Action required.")
    else:
        print(f"✅ Server {server_id} is healthy and running.")

print("--- AUDIT COMPLETE ---")
