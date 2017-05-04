from org.salesforce.account.account import Account


if __name__ == "__main__":
    account = Account()
    new_account = {"Name": "BlueDart__2"}
    account.create(new_account)




