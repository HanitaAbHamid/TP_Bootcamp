# Edited: Added infrastructure tracking metadata tags
server_config = {
    "server_id": "srv-001",
    "environment": "Production",
    "status": "running",
    "cpu_utilization": 84.5,
    "Owner": "Hanita Ab Hamid",
    "Cost_center": "CC_DEVOPS-99"
}
print("--- Update Cloud Resource Report ---")
print(f"Server ID: {server_config['server_id']}")
print (f"Owner: {server_config['Owner']}")
print(f"Billing Code: {server_config['Cost_center']}")
