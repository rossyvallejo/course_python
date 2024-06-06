"""
A pharmaceutical company wants to know whether an experimental drug affects systolic blood pressure.
Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact,
their systolic blood pressures were recorded.
The data appears in a python list.

THE FOLLOWING POINTS MUST BE DONE USING SOME FUNCTIONS OF SOME MODULE, AND WITH ANOTHER FUNCTION THAT YOU BUILT,
THAT IS, IMITATE THE BEHAVIOUR OF THAT FUNCTION

1. Calculate the value of 'x bar' (sample mean) and the value of s (the sample standard deviation)

"""
import statistics

data = [172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]
data.append(45)
# apend es un metodo de un objeto, que es la lista, por lo que no se puede utilizar como:
# append(data, 45). Esto solo se puede hacer para builtin functions
my_norm = statistics.NormalDist()  #Instance of a class, ie, the creation of an object

print(my_norm)
print(my_norm.pdf(0.5))
print(my_norm.mean)