
class PrioritizedList:

    def __init__(self, max_length=None, reversed=False):

        self.max_length = max_length
        self.reversed = reversed

        # The priorities are stored as the first item in a tuple
        # The second item in the tuple is a list of all items that have that priority
        self.priority_list = []
        # This list holds all currently used priorities as keys to their index in self.priority_list
        self.priorities = {}

    def add_item(self, item, priority=None):
        # For priority, if it is not reversed then lower numbers will come first
        # if it is reversed then the highest numbers will come first
        # None is always the lowest priority in the list
        # Between items that have the same priority, most recently added ones come first

        # Is the priority already in the list?
        if self.priorities.get(priority):
            # If so then find the appropriate list and insert it at the beginning
            self.priority_list[self.priorities[priority]].insert(item, -1)


