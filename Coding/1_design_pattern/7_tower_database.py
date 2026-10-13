from dataclasses import dataclass
from typing import Dict

@dataclass
class Tower:
    _next_id = 0

    name: str
    id: int = 0

    def __post_init__(self):
        self.id = Tower._next_id
        Tower._next_id += 1

@dataclass
class Repository:
    database = {}

    def check_availability(self, id):
        if id not in Repository.database:
            print(f"{id} not found")
            return False
        return True

    def save(self, data):
        Repository.database[data.id] = data
        print(f"{data} added successfully")
    
    def get_by_id(self, id):
        if check_availability(id) == True:
            print(Repository.database[id])
    
    def delete(self, id):
        if check_availability(id) == True:
            del Repository.database[id]
            print(f"{id} deleted successfully")
    
    def get_all(self):
        if len(Repository.database.values()) == 0:
            print("No data available")
        else:
            for tower_data in Repository.database.values():
                print(f"id: {tower_data.id}, name: {tower_data.name}")
        
    def update(self, id, name):
        if check_availability(id) == True:
            Repository.database[id].name = name
            print(f"{id} updated successfully")

t1 = Tower("Tower 1")
t2 = Tower("Tower 2")

repo = Repository()
repo.save(t1)
repo.save(t2)

repo.get_all()