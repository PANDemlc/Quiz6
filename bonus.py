from abc import ABC, abstractmethod
from typing import List

# Add New Activity Types
# Observer tells other classes to 'notify' when collecting new data
class Observer(ABC):
    @abstractmethod
    def notify(self, data):
        raise NotImplementedError("Implement function!")
    
class Monitor(ABC):
    @abstractmethod
    def attach(self, observer):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def detach(self, observer):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def notify_change(self):
        raise NotImplementedError("Implement function!")

# Separate classes for User, Activity, ActivityMonitor, DataStorage, and Display to follow SRP
class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

class Activity:
    def __init__(self, activity: str, steps: int, distance: float, calories_burned: float):
        self.activity = activity
        self.steps = steps
        self.distance = distance
        self.calories_burned = calories_burned

class Display(Observer):
    def notify(self, data):
        print("Displaying user data: ")
        for item, value in data.items():
            print(f"{item}: {value} ")

class ActivityMonitor(Monitor):
    def __init__(self):
        self.observers: List[Observer] = []
        self.data_storage = DataStorage()

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify_change(self):
        data = self.data_storage.get_data()
        for observer in self.observers:
            observer.notify(data)
    
    def collect_data(self, user, activity):
        self.data_storage.add_data(user, activity)
        self.notify_change()
    
class DataStorage:
    def __init__(self):
        self.data = {}
    
    def add_data(self, user, activity):
        if user not in self.data:
            self.data[user] = {}
        self.data[user][activity.activity] = {"Steps": activity.steps, "Distance": activity.distance, "Calories_burned": activity.calories_burned}

    def get_data(self):
        return self.data
    
def main():
    bob = User("Bob", 90, 160)
    monitor = ActivityMonitor()
    monitor.attach(Display())

    # Add any new activity
    running = Activity("Running", 10000, 10, 500)
    monitor.collect_data(bob, running)

if __name__ == "__main__":
    main()