# return individual data record
def get_individual_user_data(user):
    return {
        "id": str(user["_id"]),
        "employee_id": int(user["employee_id"]),
        "employee_name": str(user["employee_name"]),
        "employee_email": str(user["employee_email"]),
        "employee_domain": str(user["employee_domain"]),
        "employee_password": str(user["employee_password"]),
        "employee_status": str(user["employee_status"])
    }

# return a list of users
def get_all_user_data(users):
    return [get_individual_user_data(user) for user in users]