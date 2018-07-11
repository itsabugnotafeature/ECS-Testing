
class System:

    def __init__(self):

        self.id = hash(self)
        self.working = False
        self.node_list = []

    # NECESSARY METHODS #

    def start(self):
        self.working = True
        return self.working

    def stop(self):
        self.working = False

    def update(self, time):
        pass

    def pause(self):
        pass
