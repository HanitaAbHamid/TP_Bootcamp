import time
print("[AWS SDK SIMULATOR] Initializing connection using local credentials...")
time.sleep(1)  # Simulate delay

aws_profile = {
    "access_key": "abc123",
    "default_region" : "ap-southeast-1",
    "output_format" : "json"
}
print(f"Authenticated with Target Region: {aws_profile['default_region']}, Output Format: {aws_profile['output_format']}, Access Key: {aws_profile['access_key']}")
print("Fethcing multi-region infrastructure metrics data stream.../n")
time.sleep(1.5)  # Simulate delay

regional_clusters = [
    {"region" : "ap-southeast-1", "zone": "Singapore-Zone-A", "active-nodes": 12,},
    {"region" : "ap-southeast-2", "zone": "Sydney-Zone-B", "active-nodes": 8,},
    {"region" : "us-east-1", "zone": "Virginia-Zone-C", "active-nodes": 15,},
    {"region" : "eu-west-1", "zone": "Ireland-Zone-D", "active-nodes": 0,}
]
for cluster in regional_clusters:
    region = cluster["region"]
    datacenter_zone = cluster["zone"]
    nodes_count = cluster["active-nodes"]
    print(f"Region: {region}, Datacenter Zone: {datacenter_zone}, Active Nodes: {nodes_count}")

if nodes_count == 0:
    print(f"Warning: Region {region} - {datacenter_zone} has ZERO nodes.Failover required./n")
else:
    print(f"Status Healthy: Handling traffic across: {nodes_count} active cloud workers. /n")

print("[Simulation Complete] Multi-region infrastructure metrics data stream fetched successfully.  ")