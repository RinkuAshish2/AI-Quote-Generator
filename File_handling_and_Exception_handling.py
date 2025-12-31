#20/12/2025
#file handling (read and wite)
#=============== write operations ====================#
#file=open('requirements.txt','w')
#print(file.write("ashish"))
#file.close()

#================= read operations =====================#
#file=open('requirements.txt','r')
#print(file.read())
#file.close()

#================= appende operations ==============#
#file=open("sample_data.csv",'r')
#print(file.read())
#file.close()

#================= with operations ===========#
#with open("sample_data.csv",'r') as file:
#    file.read()





#============= File Expection Handling ======================#
# try , except, finally
#ry:
    # risky code
#xcept:
    # code to handle error

#a=10/0
#print(a) # it will show the error

#try:
#    a=10/0
#    print(a)
#except ZeroDivisionError:
#    print("you are dividing the 0")
#finally:
#    print("python class")
 
#============== Types of errors ========#
#| Exception           | Reason                 |
#| ------------------- | ---------------------- |
#| `ZeroDivisionError` | Division by zero       |
#| `ValueError`        | Invalid value          |
#| `TypeError`         | Wrong data type        |
#| `FileNotFoundError` | File missing           |
#| `IndexError`        | Index out of range     |
#| `KeyError`          | Dictionary key missing |

#we dont the what kind of error we check like this using the exception key word 
#try:
#    a=10/0
#    print(a)
#except Exception as e: # storing the erorr in e variable
#    print(e)
#finally:
#   print("python class")