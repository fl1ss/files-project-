with open("new_file.txt" , "a") as file:
    file.write("Test")
with open("new_file.txt" , "r") as file:
  for line in file:
    print(line.strip())
    with open("example.txt" , "r") as file:
       for line in file:
          print(len[1])
with open("example.txt" , "r") as file:
   for line in file:
      print(line.split(",", 1)[1].strip())
new_line = input("Enter the line you want to add to the file: ")
       with open("example.txt" , "a") as file:
          file.write(new_line + "\n")
line_to_delete = "This is the line to delet\n"
with open("example.txt" , "w") as file:
   lines = file.readlines()

with open("example.txt" , "w") as file:
   for line in lines:
      if line!= line_to_delete:
         file.write(line)