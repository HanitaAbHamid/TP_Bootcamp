cloud_servers = [
    {"name": "production-db-01", "env": "Prod", "status": "running"},
    {"name": "development-web-app", "env": "Dev", "status": "running"},
    {"name": "testing-api-service", "env": "Test", "status": "running"},
    {"name": "staging-analytics", "env": "Staging", "status": "stopped"},
    {"name": "dev-sandbox-hanita", "env": "Dev", "status": "running"}
]
print("CLOUD ENVIRONMENT AUDIT START...")

servers_to_stop = 0
for server in cloud_servers:
    if server["env"] == "Dev" or server["env"] == "Test":
        print(f"ALERT - {server['name']} is in {server['env']} environment and is currently {server['status']} after hours! Sending command to STOP.")
        servers_to_stop += 1
    else:
        print(f"SAFE: {server['name']} is in {server['env']} environment and is currently {server['status']} No modifications needed.")

#Summary report
print("\nSUMMARY REPORT:")
print(f"Audit Completed. Total servers flagged for stopping: {servers_to_stop}")
print("Estimated daily cost savings: $" + str(servers_to_stop * 10) + " SGD") # Assuming each server costs $10/day to run