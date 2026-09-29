# Ask the operator for the safety limit when the scripts starts
user_limit = float(input("Please enter the CPU usage safety limit (as a percentage): "))

#A list of dictionaries representing real AWS instance data streams
cloud_metrics = [
    {"instance_id": "iweb-prod-01", "cpu_pct": 45.2},
    {"instance_id": "i-web-prod-02", "cpu_pct": 94.8},
    {"instance_id": "i-web-prod-03", "cpu_pct": 91.3},
]
     
for metric in cloud_metrics:
    # Extracting values by targeting their asset tag keys
    server_name = metric["instance_id"]
    cpu_usage = metric["cpu_pct"]

    # Checking if the CPU usage exceeds the threshold of 90%
    if cpu_usage > user_limit:
        print(f"CRITICAL ALERT: {server_name}  is at spike at {cpu_usage}% .")