import json

class RestAPI:
    def __init__(self, database=None):
        # Constructor initializes the instance with an optional database and an empty list of users.
        self.database = database
        self.users = {"users": []}

    def get(self, url, payload=None):
        # Handle GET requests to the API.
        if payload:
            # If a payload is provided, extract the username from it.
            user_name = json.loads(payload)["users"][0]
            
            # Search the database for a user with the extracted username.
            for user in self.database["users"]:
                if user["name"] == user_name:
                    # If found, add the user's data to the response.
                    self.users["users"].append(user)
                    break
                    
        # Return the JSON representation of the users.
        return json.dumps(self.users)

    def post(self, url, payload=None):
        # Handle POST requests to the API.
        if url == "/add":
            # If the URL is "/add", add a new user to the database.
            user_name = json.loads(payload)["user"]
            
            # Create a new user with initial values and add it to the database.
            user_data = {"name": user_name, "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database["users"].append(user_data)
            
            # Return the JSON representation of the newly added user.
            return json.dumps(user_data)

        elif url == "/iou":
            # If the URL is "/iou", process a financial transaction between a lender and a borrower.
            lender = json.loads(payload)["lender"]
            borrower = json.loads(payload)["borrower"]
            amount = json.loads(payload)["amount"]

            # Search for the lender and borrower in the database.
            for user in self.database["users"]:
                if user["name"] == lender:
                    # Process the transaction for the lender.
                    if borrower in user["owes"].keys():
                        if amount < user["owes"][borrower]:
                            user["owes"][borrower] -= amount
                        elif amount == user["owes"][borrower]:
                            del user["owes"][borrower]
                        else:
                            user["owed_by"].update(
                                {borrower: amount - user["owes"][borrower]}
                            )
                            del user["owes"][borrower]
                    else:
                        if borrower not in user["owed_by"].keys():
                            user["owed_by"].update({borrower: amount})
                        else:
                            user["owed_by"][borrower] += amount
                    user["balance"] += amount
                    self.users["users"].append(user)

                if user["name"] == borrower:
                    # Process the transaction for the borrower.
                    if lender in user["owed_by"].keys():
                        if amount < user["owed_by"][lender]:
                            user["owed_by"][lender] -= amount
                        elif amount == user["owed_by"][lender]:
                            del user["owed_by"][lender]
                        else:
                            user["owes"].update(
                                {lender: amount - user["owed_by"][lender]}
                            )
                            del user["owed_by"][lender]
                    else:
                        if lender not in user["owes"].keys():
                            user["owes"].update({lender: amount})
                        else:
                            user["owes"][lender] += amount
                    user["balance"] -= amount
                    self.users["users"].append(user)

            # Return the JSON representation of the updated user data, sorted by keys.
            return json.dumps(self.users, sort_keys=True)
