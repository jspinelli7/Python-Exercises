# Create a Temperature Class. Make two methods
# 1) convertFahrenheit - take C turn to F. 2) convertCelsius - take F turn to C

class Temperature:
    temp = 0

    def __init__(self, temp):
        self.temp = temp

    def convertFahrenheit(self):
        tf = (self.temp*9/5) + 32
        return tf

    def convertCelsius(self):
        tc = (self.temp-32) * 5/9
        return tc

# What is the proper way to call these?

input_Temperature = int(input("Enter the temperature in Celsius: "))
temp1 = Temperature(input_Temperature)
print(temp1.convertFahrenheit())

input_Temperature = int(input("Enter the temperature in Fahrenheit: "))
temp1 = Temperature(input_Temperature)
print(temp1.convertCelsius())

