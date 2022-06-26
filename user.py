


class User:
    def __init__(self, *initial_data, **kwargs) -> None:
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
    
    def __str__(self) -> str:
        if self.id is not None and self.username is not None:
            return f'User: id: {self.id} username: {self.username}'
        return "Error user"