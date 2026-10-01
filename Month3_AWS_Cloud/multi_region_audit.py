# A complex array representing cross-region multi-server deployments
aws_global_infrastructure = [
    {"region": "ap-southeast-1", "instance": "i-sg-web-01", "state": "running"},
    {"region": "ap-southeast-1", "instance": "i-sg-db-01", "state": "stopped"},
    {"region": "us-east-1", "instance": "i-us-api-01", "state": "running"},
    {"region": "us-east-1", "instance": "i-us-worker-01", "state": "terminated"}
]

# A lookup dictionary to translate raw IDs into human-readable server roles
server_name_mapping = {
    "i-sg-web-01": "Singapore Web Frontend",
    "i-sg-db-01": "Primary Production Database",
    "i-us-api-01": "US API Gateway",
    "i-us-worker-01": "US Background Task Worker"
}

print("🌍 [STARTING CROSS-REGION INFRASTRUCTURE INTEGRITY CHECK] 🌍")

# EDITED: Added encoding="utf-8" to support emojis inside the log text file!
with open("region_alerts.txt", "a", encoding="utf-8") as log_file:
    log_file.write("\n--- NEW INFRASTRUCTURE AUDIT SCAN ---\n")
    
    for resource in aws_global_infrastructure:
        aws_zone = resource["region"]
        server_id = resource["instance"]
        current_state = resource["state"]
        
        friendly_name = server_name_mapping[server_id]
        
        if current_state != "running":
            # 1. Print to the terminal screen for the engineer to see immediately
            print(f"🚨 REGION ALERT [{aws_zone}]: '{friendly_name}' is {current_state.upper()}!")
            
            # 2. Write the exact same alert string to our permanent log file record
            log_file.write(f"🚨 REGION ALERT [{aws_zone}]: '{friendly_name}' is {current_state.upper()}!\n")

print("📝 Operational alerts have been successfully written to region_alerts.txt!")
