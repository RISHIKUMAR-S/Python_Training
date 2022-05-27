import pickle

def save_object(data):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 
def create_list():
    students = []
    choice = input("Do you want to add 1 student details (add/stop) : ")
    i=1
    while choice.lower() == "add":
        detail = dict()
        detail["name"] = input("Enter the {} student\'s name : ".format(++i))
        detail["roll"] = int(input("Enter the rollno : "))
        detail["cgpa"] = int(input("Enter the cgpa : "))
        students.append(detail)
        choice = input("Do you want to continue (add/stop) : ")
    print(students)
    return students

report = create_list()
save_object(report)