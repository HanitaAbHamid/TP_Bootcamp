import os

folder = "log_folders"

for filename in os.listdir(r"C:\Users\hanit\OneDrive\Desktop\TP_Bootcamp\Month1_Linux_Git\log_folders"):
    if filename.endswith(".log"):
        file_path = os.path.join(folder, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "ERROR" in line:
                    print(f"Error found in {filename}: {line.strip()}")
                    