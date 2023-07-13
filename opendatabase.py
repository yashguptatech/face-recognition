from subprocess import Popen
try:
    print("Opening The Database Please Wait..")
    p = Popen("Book1.csv", shell=True)
    print("Database Opened Successfully..")
except:
    print("Problem In Opening The Database!!")
