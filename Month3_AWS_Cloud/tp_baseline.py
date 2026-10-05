vpc_infrastructure =[
    {"id": "i-frontend-01", "subnet": "Public", "status": "running"},
    {"id": "i-database-02", "subnet": "Private", "status": "stopped"},
]
print("🚀Starting Temasek Poly Course Simluation Check...")

# Python Loop Layout: Stepping through our network array step-by-step
for ec2_instance in vpc_infrastructure:
   name = ec2_instance["id"]
   subnet = ec2_instance["subnet"]
   status = ec2_instance["status"]
print(f"\nEvaluating machine: {name} in {subnet} subnet with status: {status}")

if status != "running":
    print(f"⚠️ Alert:  {name} in {subnet} is {status.upper()}. Run 'aws ec2 start-instances --instance-ids {name}' to start it.")

else:
    print(f"✅ {name} in {subnet} is running smoothly.")
   