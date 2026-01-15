from app.database.models import User, Service

users_list = [
    User(1, "resident1", "pass1"),
    User(2, "resident2", "pass2"),
    User(3, "admin", "admin")
]

services_list = [
    Service(1, "Gym", 5),
    Service(2, "Pool", 3),
    Service(3, "Sauna", 2),
    Service(4, "Tennis Court", 4),
    Service(5, "Music Room", 1)
]

def get_user_by_username(username):
    for user in users_list:
        if user.username == username:
            return user
    return None

def get_service_by_id(service_id):
    for service in services_list:
        if service.id == int(service_id):
            return service
    return None

def get_reservations_for_user(username):
    user_reservations = []
    
    for service in services_list:
        for date, times in service.schedule.items():
            for time, users in times.items():
                if username in users:
                    user_reservations.append({
                        "service_name": service.name,
                        "date": date,
                        "time": time
                    })
    
    return user_reservations

def get_reservations_for_user(username):
    user_reservations = []
    
    for service in services_list:
        for date, times in service.schedule.items():
            for time, users in times.items():
                if username in users:
                    user_reservations.append({
                        "service_id": service.id,
                        "service_name": service.name,
                        "date": date,
                        "time": time
                    })
    
    return user_reservations