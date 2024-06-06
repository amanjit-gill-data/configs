from platform import python_version 

# set startup banner e.g. "Python 3.10.12"
c.InteractiveShell.banner1 = f"Python {python_version()}\n"

# put newline between end of input and start of output
c.InteractiveShell.separate_out = "\n"

# "Linux" scheme is for dark backgrounds
c.InteractiveShell.colors = "Linux"

