cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty Cars")




# Else combine with For loop means:
# If the loop completely ran through all of the elements WITHOUT
# encountering a break or an error, then run the else statement.