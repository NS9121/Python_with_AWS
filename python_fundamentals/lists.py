def main():

    # Create a list

    aws_service = ['S3', 'Lambda', 'EC2', 'DynamoDB', 'RDS']

    # Access first item in the list

    print(f"First item in list : {aws_service[0]}")

    # Access last item in the list

    print(f"Last item in the list : {aws_service[-1]}")

    # Change the last item in the list

    aws_service [-1] = 'SNS'

    #print(f" Updated aws service --> {aws_service}")

    # append an item to the list 

    aws_service.append('SQS')

    #print(f"aws_service --> {aws_service}")

    # Delete the item at the second place 

    aws_service.pop(1)

    print(f"aws_service --> {aws_service}")

    # Slice the list 

    sliced_list = aws_service[1:3]

    print(f"Sliced list --> {sliced_list}")
    print(f"aws_service --> {aws_service}")

if __name__ == '__main__':
    main()