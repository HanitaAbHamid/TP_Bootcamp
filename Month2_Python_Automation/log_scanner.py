# =====================================================================
# DEVOPS FILE READING AUTOMATION TEMPLATE
# PROJECT: LIVE LOG FILE SCRAPER
# =====================================================================

print("--- [PRODUCTION] DETECTING EXTERNAL FILE DATA ---")

# 1. Open the external text file securely in read ('r') mode
with open("server_crashes.txt", "r") as file_pointer:
    # Read all lines from the text file into a Python processing loop
    all_lines = file_pointer.readlines()

# 2. Iterate through each line extracted from the server log
for line in all_lines:
    # Strip away extra hidden line spacing format tags
    clean_line = line.strip()
    
    # Check if the text string contains a system crash alert
    if "ERROR_CRITICAL" in clean_line:
        print(f"🚨 ALERT FAULT INGESTED: {clean_line}")
