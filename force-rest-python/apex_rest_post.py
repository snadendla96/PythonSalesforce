from org.salesforce.account.apexobject import Students


if __name__ == "__main__":
    apexobject = Students()
    new_object = {"name": "PythonPost"}
    apexobject.create(new_object)






