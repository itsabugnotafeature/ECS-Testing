
class PrioritizedList:

    def __init__(self, max_length=None, reversed=False):

        self.max_length = max_length
        self.reversed = reversed

        # This stores the items in order of priority
        self.priority_list = []
        # This dict holds all currently used priorities as keys to a list of all items that have that priority
        self._priority_dict = {}

    def add_item(self, item, priority=None):
        # For priority, if it is not reversed then lower numbers will come first
        # if it is reversed then the highest numbers will come first
        # None is always the lowest priority in the list
        # Between items that have the same priority, most recently added ones come first
        # Each item can only be in the list once

        # Is the item already in the list?
        if item in self.priority_list:
            self.priority_list.remove(item)

        if priority in self._priority_dict:



