from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    search_params = request.args.to_dict()
    results = search_users(search_params)
    return results, 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters in the desired format
    """
    # Implement search here!
    search_id = args.get("id")
    search_name = args.get("name")
    search_age = args.get("age")
    search_occupation = args.get("occupation")

    results = []

    # Descript1 ID with extend result lower sensitivity
    if search_id:
        results.extend([user for user in USERS if user["id"].lower() == search_id.lower()])

    # Descript2 Name with extend result lower sensitivity
    if search_name:
        results.extend([user for user in USERS if search_name.lower() in user["name"].lower()])

    # Descript3 Age with extend result lower sensitivity
    if search_age:
        try:
            age = int(search_age)
            results.extend([user for user in USERS if age - 1 <= user["age"] <= age + 1])
        except ValueError:
            pass

    # Descript4 Occupation with extend result lower sensitivity
    if search_occupation:
        results.extend([user for user in USERS if search_occupation.lower() in user["occupation"].lower()])
    
    unique_results = list({user["id"]: user for user in results}.values())


    # Bonus
    # Arrange the results in the desired order: "id," "name," "age," and "occupation"
    arranged_results = [
        ("id=" + user["id"], "name=" + user["name"], "age=" + str(user["age"]), "occupation=" + user["occupation"])
        for user in unique_results
    ]

    return arranged_results
    