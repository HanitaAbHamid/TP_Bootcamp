import os
folder = r"C:\Users\hanit\OneDrive\Desktop\TP_Bootcamp\Month1_Linux_Git\log_folders\logs"
for filename in os.listdir(folder):
    if filename.endswith(".log"):
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                if "ERROR" in line:
                    print(f"Error found in {filename}: {line.strip()}")