# =====================================================================
# ENTERPRISE DEVOPS LIVE INFRASTRUCTURE TEMPLATE
# PROJECT: AWS NODE MONITORING AUTOMATION
# =====================================================================
import time

# 1. TEMPLATE VARIABLES: A production list containing multiple live logs from AWS
aws_traffic_logs = [
    "SYSTEM: UP | NODE: SINGAPORE-1 | STATUS: OK",
    "SYSTEM: UP | NODE: SINGAPORE-2 | STATUS: ERROR_CRITICAL_502_BAD_GATEWAY",
    "SYSTEM: UP | NODE: SINGAPORE-3 | STATUS: OK",
    "SYSTEM: UP | NODE: MALAYSIA-1  | STATUS: ERROR_CRITICAL_404_NOT_FOUND",
    "SYSTEM: UP | NODE: INDONESIA-1 | STATUS: OK",
    "SYSTEM: UP | NODE: JAKARTA-1   | STATUS: ERROR_CRITICAL_500_INTERNAL_SERVER_ERROR"
]

print("--- [PROD ENVIRONMENT] WAKING UP AUTOMATED HEALTH MONITOR ---")
time.sleep(1) # Simulates the system connecting to the network cloud node

# 2. THE BLUEPRINT LOOP: Triage task to count total active crashes
error_count = 0

for log in aws_traffic_logs:
    # A junior engineer's job: read the condition logic string
    if "STATUS: OK" in log:
        print(f"🟢 Checking Node... Healthy status reported.")
    else:
        print(f"💥 WARNING: Outage detected! Details: {log}")
        error_count = error_count + 1

# 3. SUMMARY METRICS REPORT
print("\n=======================================================")
print(f"📊 REPORT COMPLETE. TOTAL ACTIVE CRITICAL OUTAGES: {error_count}")
print("=======================================================")
