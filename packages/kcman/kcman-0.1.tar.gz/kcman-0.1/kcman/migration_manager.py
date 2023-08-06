class PersistanceItem:
    def __init__(self, manager, description, action, params, environment=None, id=None):
        self.manager = manager
        self.description = description
        self.action = action
        self.params = params
        self.environment = environment
        self.id = id

    def execute(self):
    # TODO: add implementation for execution of persistence item
        print("executing\n{}".format(self.toString()))
        return 

    def persist(self):
    # TODO: add implementation for persistance of persistance item
        print("saving\n{}".format(self.toString()))
        return 

    def toString(self):
        objectString = " Manager: {}\n Description: {}\n Action: {}\n Params: {}\n Environment: {}\n Id: {}".format(self.manager, self.description, self.action, self.params, self.environment, self.id)
        return objectString

class MigrationManager:
    def main(): 
        # TODO: add main method to migrate between environments 
        return