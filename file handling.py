try:
    f = open("student.txt", "a")

    f.write("Roll\tName\tMarks\n")

    while True:
        print("Please Enter Student Details:")

        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        data = f"{roll}\t{name}\t{marks}\n"
        f.write(data)

        print("Data Saved Successfully!")

        ans = input("Want to enter more records? (Y/N): ")
        if ans.lower() == "n":
            break

except Exception as e:
    print("An error occurred:", e)

finally:
    f.close()
    print("File Closed Successfully.")
