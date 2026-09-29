# A dictionary tracking our active environment deployment metadata
deployment_status = {
    "app": "Hani_Web_App",
    "status": "SUCCESSFUL",
    "environment": "Staging"
}

# Python File Operations: "a" means Append mode!
# It targets our 'build_notes.txt' file that you created earlier in Git Bash.
with open("build_notes.txt", "a") as manifest_file:
    # Constructing a clean deployment log string
    log_message = f"\n[DEPLOYMENT DETECTED] App: {deployment_status['app']} | Status: {deployment_status['status']}"
    
    # Writing the code output directly into the file structure
    manifest_file.write(log_message)

print("📋 Infrastructure state successfully injected into build_notes.txt!")
