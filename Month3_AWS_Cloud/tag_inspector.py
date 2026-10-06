# A global cloud roster where each server dictionary contains a nested 'tags' dictionary
cloud_fleet = [
    {
        "instance_id": "i-web-prod-01", 
        "tags": {"Environment": "Production", "Team": "WebOps"}
    },
    {
        "instance_id": "i-db-secure-02", 
        "tags": {"Environment": "Production", "Team": "Finance"}
    },
    {
        "instance_id": "i-test-sandbox-01", 
        "tags": {"Environment": "Development", "Team": "WebOps"}
    }
]

print("🔍 [SCANNING ASSET TAG RESOURCING] Searching for WebOps instances...")

# The loop steps through our fleet collection
for asset in cloud_fleet:
    server_id = asset["instance_id"]
    asset_tags = asset["tags"]  # This pulls out the internal tags dictionary!
    
    asset_tags["Owner"] = "Hanita"
    env_tier = asset_tags["Environment"]
    
    # Automation rule: trigger actions only for the WebOps team's systems
    if asset_tags["Team"] == "WebOps":
        print(f"🎯 MATCH FOUND: Server {server_id} is managed by WebOps ({env_tier} tier).")
        
# 🟢 NEW BRICK: Injecting the new key-value pair directly into the tags dictionary
    asset_tags["Owner"] = "Hanita"
    
    print(f"✅ Successfully updated {server_id} profile! Current Tags: {asset_tags}")

print("\n✨ Metadata asset tagging complete. Printing updated system map:")
print(cloud_fleet)

print("\n✨ Tag integrity scan completed successfully.")
