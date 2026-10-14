servers =["i-web-01", "i-db-02", "i-api-03"]

#loop through the list of servers and print each one
for server in servers:
    print(f"Checking server: {server}")

#Inject conditional logic to check if the server name contains "db"
if "db" in server:
    print(f"Database cluster detected on {server}.")
else:
    print(f"{server} is not a database server.")