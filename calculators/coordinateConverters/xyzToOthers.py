from math import sqrt, atan2, degrees

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
        print("Please enter Cartesian coordinates. Type 'exit' to exit.")
        print(f"Precision is set to {precision}. You cannot change it in web edition\n")
        x = float(myInput("x (meters): "))
        y = float(myInput("y (meters): "))
        z = float(myInput("z (meters): "))

        print("\n" + " Cylindrical ".center(70, "="))
        rCyl = sqrt(x**2 + y**2)
        phiCyl = atan2(y, x)

        print(f"--> r: {round(rCyl, precision)} meters")
        print(f"--> ϕ: {round(degrees(phiCyl), precision)}°  --> ϕ: {round(phiCyl, precision)} radians")
        print(f"--> z: {round(z, precision)} meters")
        
        print("\n" + " Spherical ".center(70, "="))
        rSph = sqrt(x**2 + y**2 + z**2)
        thetaSph = atan2(sqrt(x**2 + y**2), z)
        phiSph = atan2(y, x)
        
        print(f"--> R: {round(rSph, precision)} meters")
        print(f"--> θ: {( str(round(degrees(thetaSph), precision)) + '°').ljust(5 + precision)}  --> θ: {str(round(thetaSph, precision)).ljust(4 + precision)} radians")
        print(f"--> ϕ: {( str(round(degrees(phiSph), precision)) + '°').ljust(5 + precision)}  --> ϕ: {str(round(phiSph, precision)).ljust(4 + precision)} radians")
        print(" ")
    except Exception as ex:
        print(ex)
calculate()