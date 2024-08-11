import os

def create_file(filename):
    try:
        with open(filename , 'x') as f:
            print(f" File Name {filename}: Created Successfully!")

    except FileExistError:
        print(f'File Name {filename} already exist!')

    except Exception as E:
        print("An error occurred!")


def view_all_file():
    files = os.listdir()
    if not files:
        print("No files Found!")
    else:
        print("Files In directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")

    except FileNotFoundErorr:
        print(f"{filename} is not found!")

    except Exception as E:
        print("An erorr occur!")


def read_file(filename):
    try:
        with open( filename , 'r') as f:
            content = f.read()
            print(f" content of '{filename}' :\n {content} ")


    except FileNotFoundErorr:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print("An Erorr occurred!")

def edit_file(filename):
    try:
        with open( filename , 'a') as f:
            content = input("Enter the data to add : ")
            f.write(content + "\n")
            print(f"content add to {filename} successfully!")
    except FieNotFoundErorr :
        print("File is not found!")

    except Exception as e:
        print("An Erorr occurred!")

def main():
    while True:
        print("File Management App ")
        print("1: Creat file")
        print("2: View all file")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6:Exit ")

        choice = input("Enter Your Choice(1-6): ")

        if choice == '1':
            filename = input("Enter your file name: ")
            create_file(filename)

        elif choice == '2':
            view_all_file()

        elif choice == '3':
            filename = input("Enter the File Name for delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter File Name to Read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter File Name for edit: ")
            edit_file(filename)

        elif choice == '6':
            print("Closing the file!!!")
            break

        else:
            print("In-valid Syntax!")


if __name__ == "__main__":
    main()
























        

    


















        
