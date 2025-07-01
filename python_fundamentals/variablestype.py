# Create variable of different types
def main():
    # String
    instance_type = 't2.micro'
    message = "My instances are of type : "

    print(f"{message}{instance_type}")

    # Integer
    num_of_instances = 5
    hours_running = 10
    

    print(f"I have total {num_of_instances} {instance_type} instances running for {hours_running} hours .")
    # Boolean
    instances_running = True

    print(f"Is my instance running ? \n{instances_running}")
    
    # Float
    instances_cost_per_hour = 0.25

    print(f"The price of the running instances {instances_cost_per_hour} $/hour")



if __name__=='__main__':
    main()
