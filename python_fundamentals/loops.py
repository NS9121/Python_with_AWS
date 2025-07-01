# Example of the loops

# List of the aws service
aws_service = ['S3', 'Lambda', 'EC2', 'DynamoDB', 'RDS']


# Using for loop
print("Using for loop to iterate through the list")
for service in aws_service:
    print(service)

# using while loop

print("using while loop to print from the reverse")

index = len(aws_service) - 1

while index >= 0 :
    print(aws_service[index])
    index -=1 

# Using enumerate built in function with the for loop

for index,service in enumerate(aws_service):

    print(f"Sevice #  {index}: {service}")






