# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])

# except FileNotFoundError:
#     #print("There was an error.")
#     file = open("a_file.txt","w")
#     file.write("something")

# except KeyError as error_message:
#     print(f"that key {error_message} doesn't exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     # file.close()
#     # print("file was closed.")
#     raise TypeError("this is an error I made.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be 3M over.")

bmi = weight / height ** 2
print(bmi)