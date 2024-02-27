'''
Task

'''


import cmath

def polar_coordinates(z):
    # Convert the complex number to polar coordinates
    r, phi = cmath.polar(z)
    
    # Print the value of r and phi with expected precision
    print("{:.15f}".format(r))
    print("{:.15f}".format(phi))
    
if __name__ == "__main__":
    z = complex(input().strip())  # Input complex number
    polar_coordinates(z)
    