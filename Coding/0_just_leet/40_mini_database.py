from typing import Dict, List, Optional
import uuid
from pydantic import BaseModel
from enum import Enum

class MessageType(Enum):
    INFO = "Info"
    ERROR = "Error"

class Response(BaseModel):
    message_type: MessageType
    message: str
    action: str
    data_id: Optional[str] = None

class Data(BaseModel):
    name: str
    age: int

class Column(BaseModel):
    id: str
    name: str | None
    age: int | None

class Repository:
    def __init__(self):
        self._dataframe_list: List[Data] = []
        self._dataframe_dict: Dict[str, Column] = {}

        self._logs: List[Response] = []

    def insert(self, data: Data):
        try:
            if data:
                current_id = str(uuid.uuid4())
                new_data = Column(
                    id = current_id,
                    name = data.name,
                    age = data.age
                )

                self._dataframe_list.append(new_data)
                self._dataframe_dict[current_id] = new_data

                response = Response(
                    message_type = MessageType.INFO,
                    message = f"Data inserted",
                    action = "INSERT",
                    data_id = current_id
                )

                self._logs.append(response)

                return current_id
        except Exception as e:
            response = Response(
                message_type = MessageType.ERROR,
                action = "INSERT",
                message = e
            )
            self._logs.append(response)

    def update(self, update_data: Column):
        try:
            current_data = self._dataframe_dict.get(update_data.id)
            if current_data:
                updated_name = current_data.name
                updated_age = current_data.age
    
                if update_data.name:
                    updated_name = update_data.name
    
                if update_data.age is not None:
                    updated_age = update_data.age
    
                updated_obj = Column(
                    id = str(update_data.id),
                    name = updated_name,
                    age = updated_age
                )
    
                self._dataframe_dict[update_data.id] = updated_obj

                for index in range(len(self._dataframe_list)):
                    if self._dataframe_list[index].id == update_data.id:
                        self._dataframe_list[index] = updated_obj

                response = Response(
                            message_type = MessageType.INFO,
                            message = f"Data Updated",
                            action = "UPDATE",
                            data_id = str(update_data.id)
                        )
                
                self._logs.append(response)

            response = Response(
                                message_type = MessageType.ERROR,
                                message = f"Data Not Found",
                                action = "UPDATE",
                                data_id = update_data.id
                            )
                            
            self._logs.append(response)

            return

        except Exception as e:
            response = Response(
                    message_type = MessageType.ERROR,
                    action = "UPDATE",
                    message = str(e)
                )
            self._logs.append(response)

    def delete(self, id: str):
        try:
            current_data = self._dataframe_dict.get(id)

            if current_data:
                del self._dataframe_dict[id]

                response = Response(
                                message_type = MessageType.INFO,
                                message = f"Data Deleted",
                                action = "DELETE",
                                data_id = id
                            )
                    
                self._logs.append(response)

                return

            response = Response(
                    message_type = MessageType.ERROR,
                    message = f"Data Not Found",
                    action = "DELETE",
                    data_id = id
                )
                
            self._logs.append(response)
            
        except Exception as e:
            response = Response(
                    message_type = MessageType.ERROR,
                    action = "DELETE",
                    message = e
                )
            self._logs.append(response)

    def search(self, id: str):
        try:
            current_data = self._dataframe_dict.get(id)

            if current_data:
                response = Response(
                            message_type = MessageType.INFO,
                            message = f"Data Found",
                            action = "SEARCH",
                            data_id = id
                        )
                return current_data

            response = Response(
                    message_type = MessageType.ERROR,
                    message = f"Data Not Found",
                    action = "SEARCH",
                    data_id = id
                )
                
            self._logs.append(response)
            
        except Exception as e:
            response = Response(
                    message_type = MessageType.ERROR,
                    action = "SEARCH",
                    message = e
                )
            self._logs.append(response)

    def sort(self, attribute: str, condition: str = None):
        try:
            if not self._dataframe_list:
                response = Response(
                    message_type=MessageType.INFO,
                    action="SORT",
                    message="No Data Found"
                )
                self._logs.append(response)
                return

            first_obj = self._dataframe_list[0]

            if hasattr(first_obj, attribute):

                if attribute == "name" and condition == "len":
                    result = sorted(
                        self._dataframe_list,
                        key=lambda element: len(element.name)
                    )

                elif attribute == "name":
                    result = sorted(
                        self._dataframe_list,
                        key=lambda element: element.name
                    )

                elif attribute == "age":
                    result = sorted(
                        self._dataframe_list,
                        key=lambda element: element.age
                    )

                else:
                    response = Response(
                        message_type=MessageType.ERROR,
                        action="SORT",
                        message=f"Sorting not supported for attribute: {attribute}"
                    )
                    self._logs.append(response)
                    return

                response = Response(
                    message_type=MessageType.INFO,
                    action="SORT",
                    message=f"Data Sorted by {attribute}"
                )
                self._logs.append(response)

                return result

            else:
                response = Response(
                    message_type=MessageType.ERROR,
                    action="SORT",
                    message=f"Attribute Not Found: {attribute}"
                )
                self._logs.append(response)

        except Exception as e:
            response = Response(
                message_type=MessageType.ERROR,
                action="SORT",
                message=str(e)
            )
            self._logs.append(response)

    def show_logs(self):
        for response in self._logs:
            current_message_type = response.message_type
            current_message_value = response.message
            current_data_id = response.data_id
            current_action = response.action

            print(
                f"{current_message_type.name} => "
                f"{': ACTION = ' + str(current_action)} "
                f"{current_message_value} "
                f"{': Data ID = ' + str(current_data_id) if current_data_id else ''}"
            )

    def show(self, limit: int = None):
        try:
            end = None
            if limit:
                end = limit
            else:
                end = len(self._dataframe_list)
            for iterator in range(end):
                print(self._dataframe_list[iterator])

            response = Response(
                            message_type = MessageType.INFO,
                            action = "SHOW",
                            message = f"Data Shown <{end}>"
                        )
            self._logs.append(response)
        except Exception as e:
            response = Response(
                        message_type = str(MessageType.ERROR),
                        action = "SHOW",
                        message = e
                    )
            self._logs.append(response)

cursor = Repository()
track_ids = []

first_data = Data(
    name = "Madhan Kumar",
    age = 22
)

# Test Cases

# 1. Insert valid data
get_id = cursor.insert(Data(name="Madhan Kumar", age=22))

# 2. Insert another valid data
cursor.insert(Data(name="Arun", age=30))

# 3. Search existing ID
# Use the data_id generated from the insert log
cursor.search("<existing_id>")

# 4. Search non-existing ID
cursor.search("invalid-id")

# 5. Update existing data
cursor.update(
    Column(
        id="<existing_id>",
        name="Madhan",
        age=25
    )
)

# 6. Update only name
cursor.update(
    Column(
        id="<existing_id>",
        name="Madhan Kumar Updated",
        age=None
    )
)

# 7. Update only age
cursor.update(
    Column(
        id="<existing_id>",
        name=None,
        age=35
    )
)

# 8. Update non-existing data
cursor.update(
    Column(
        id="invalid-id",
        name="Test",
        age=50
    )
)

# 9. Delete existing data
cursor.delete("<existing_id>")

# 10. Delete non-existing data
cursor.delete("invalid-id")

# 11. Sort by name
cursor.sort("name")

# 12. Sort by age
cursor.sort("age")

# 13. Sort by invalid attribute
cursor.sort("salary")

# 14. Sort when no data exists
empty_cursor = Repository()
empty_cursor.sort("name")

# 15. Show logs
cursor.show_logs()

cursor.show(1)

cursor.show_logs()