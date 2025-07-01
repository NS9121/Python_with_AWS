# Exception handling questions
def main():
    service = "EKS"
    aws_status = get_service_status(service)

    if aws_status:
        if aws_status == "Operational":
            print(f" {service} is Operational")
        else:
            print(f"{service} is {aws_status}")
    

def get_service_status(service):
    service_status = {
        "S3" : "Operational",
        "Lambda" : "Under Maintainance",
        "EC2" : "Down",
        "RDS" : "Opeartional"
    }
    try:
        return service_status[service]
    except KeyError as ke:
        print(f"{ke} is not under the known AWS service ")


if __name__ == "__main__":
    main()