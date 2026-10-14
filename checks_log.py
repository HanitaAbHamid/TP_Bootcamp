import os

folder = "logs"

for filename in os.listdir(r"C:\Users\hanit\OneDrive\Desktop\TP_Bootcamp\.git\logs"):
    if filename.endswith(".log"):
        file_path = os.path.join(folder, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "ERROR" in line:
                    print(f"Error found in {filename}: {line.strip()}")