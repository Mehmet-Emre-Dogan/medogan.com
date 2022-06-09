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
    print("#"*75)
    print("y = f(x), type 'exit' to exit.")
    xMin = float(myInput("x1--> " ))
    xKnown = float(myInput("xKnown--> " ))
    xMax = float(myInput("x2--> " ))
    yMin = float(myInput("y1--> " ))
    yMax = float(myInput("y2--> " ))

    deltax = xMax - xMin
    xDifference = xKnown - xMin
    ratio = xDifference/deltax

    deltay = yMax - yMin
    y = deltay*ratio + yMin
    print(f"==> y: {y}")

calculate()
# while True:
#     try:
#         calculate()
#     except ExitInputException:
#         break
#     except Exception as ex:
#         print(f"An error occured: {ex}")
    