class User:
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

class Service:
    def __init__(self, service_id, name, max_capacity):
        self.id = service_id
        self.name = name
        self.max_capacity = max_capacity
        self.schedule = {}

    def check_availability(self, date_str, time_str):
        if date_str not in self.schedule:
            return True
        
        if time_str not in self.schedule[date_str]:
            return True

        current_reservations = self.schedule[date_str][time_str]
        if len(current_reservations) < self.max_capacity:
            return True
        
        return False

    def add_reservation(self, date_str, time_str, username):
        if not self.check_availability(date_str, time_str):
            return False

        if date_str not in self.schedule:
            self.schedule[date_str] = {}
        
        if time_str not in self.schedule[date_str]:
            self.schedule[date_str][time_str] = []

        self.schedule[date_str][time_str].append(username)
        return True
    
    def cancel_reservation(self, date_str, time_str, username):
        if date_str in self.schedule:
            if time_str in self.schedule[date_str]:
                try:
                    self.schedule[date_str][time_str].remove(username)
                    return True
                except ValueError:
                    return False
        return False