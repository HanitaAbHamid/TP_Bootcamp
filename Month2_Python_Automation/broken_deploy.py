# Simulated deployment configuration script
app_name = "Hani_Web_App"
replica_count = 3
target_folder = r"C:\Users\hanit\OneDrive\Desktop\TP_Bootcamp\Month2_Python_Automation"

print("Deploying application: " + app_name)

if replica_count > 1:
    print(f"Scaling infrastructure to {replica_count} active replicas.")




