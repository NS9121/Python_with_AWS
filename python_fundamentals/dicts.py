# File for displaying the Dictionary 
def main():
    
    aws_service = {
        "S3": "Simple Storage Service for AWS Storage",
        "EC2": "Elastic Cloud Computing",
        "Lambda": "Serverless Compute Service"
    }

    print("Simple Dictionary for AWS Service And Description")

    print(aws_service)
    # Displaying the Keys of the dictionary

    print(f"Keys of the Dictionary : {aws_service.keys()}")

    # Displaying the Values of the Dictionary

    print(f"Values of the Dictionary : {aws_service.values()}")

    lambda_description = aws_service["Lambda"]

    print(f"Description of the Lambda Service --> {lambda_description}")

    # Modify the value of the Dictionary
    aws_service["Lambda"] = "AWS Service for the Server Less Computing"

    # Add a new entry to the dictionary

    aws_service["SNS"] = "AWS simple Notification Service"
    print(aws_service)

    # Delete a value from the dictionary
    del aws_service["Lambda"]

    print(aws_service)
    




if __name__ == '__main__':
    main()