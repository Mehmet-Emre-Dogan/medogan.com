from math import sqrt, atan2, degrees, cos, sin, radians
# https://stackoverflow.com/questions/12586601/remove-last-stdout-line-in-python
# CURSOR_UP_ONE = '\033[F'
# ERASE_LINE = '\033[K'

class ExitInputException(Exception):
    """Raised when user wants to exit from an input loop"""

def myInput(txt = ""):
    # print(txt, end="\r")
    str = input()
    if str.lower() != 'exit':
        # print(CURSOR_UP_ONE + ERASE_LINE, end="\r")
        # print(txt + str)
        # print(CURSOR_UP_ONE + txt + str)
        print(txt + str)
        return str
    else:
        raise ExitInputException("Exited")
def calculate(*args, **kwargs):
    try:
        precision = 4
        print("Please enter the coordinates. Type 'exit' to exit.")
        print(f"Precision is set to {precision}. You cannot change it in web edition\n")
        r = float(myInput("R (meters): "))
        theta = radians(float(myInput("θ (degrees): ")))
        phi = radians(float(myInput("ϕ (degrees): ")))

        print("\n" + " Cartesian ".center(70, "="))
        x = r*sin(theta)*cos(phi)
        y = r*sin(theta)*sin(phi)
        z = r*cos(theta)

        maxVal = str( max( (abs(int(x)), abs(int(y)), abs(int(z))) ) )
        print(f"--> x: {round(x, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        print(f"--> y: {round(y, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        print(f"--> z: {round(z, precision)} ".ljust(10 + len(maxVal) + precision) + "meters")
        
        print("\n" + " Cylindrical ".center(70, "="))
        rCyl = sqrt(x**2 + y**2)
        phiCyl = atan2(y, x)
        
        print(f"--> r: {round(rCyl, precision)} meters")
        print(f"--> ϕ: {round(degrees(phiCyl), precision)}°  --> ϕ: {round(phiCyl, precision)} radians")
        print(f"--> z: {round(z, precision)} meters")
        print(" ")

    except Exception as ex:
        print(ex)

calculate()