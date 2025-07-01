""" Determine the aws service on the basis of the User requirements"""


def main():
    
    # Define the user service requirement file_service, serverless_computing
    # virtual server,others
    user_requirement = "serverless_computing"


    if user_requirement == "file_storage":
        aws_service ="s3"
    elif user_requirement == "virtual_server":
        aws_service = "EC2"
    elif user_requirement == "serverless_computing":
        aws_service = "lambda"
    else :
        aws_service = "Unknown"
    # If not from the user service set to unknown

    if user_requirement != "Unknown":
        print(f"Aws service --> {aws_service}")
    else:
        print(f"Unknown Service")


if __name__ == '__main__':
    main()