print("🔍 [LOG PATTERN SCANNER] Commencing automated text string extraction...")
with open("server_logs.txt", "r") as log_file:
    lines = log_file.readlines() #read all the lines in the log file

print(f"Total lines read: {len(lines)}. Filtering for error patterns...")

for log_line in lines:
    cleaned_line = log_line.strip()  # Remove leading/trailing whitespace
    if "ERROR" in log_line or "Exception" in log_line:
        print(f"⚠️ Found error pattern: {log_line.strip()}")

print("\n✅ Log pattern scanning completed. All error patterns have been extracted.")