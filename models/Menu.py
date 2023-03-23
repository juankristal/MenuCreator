from models.Category import Category


class Menu:
    def __init__(self):
        self.root = Category('Root')

    def __iter__(self):
        return MenuIterator(self)


class MenuExternalIterator:
    def __init__(self, menu: Menu):
        self.categories = [category for category in menu]
        self.current_element_index = 0

    def next(self):
        self.current_element_index += 1 % len(self.categories)
        return self.categories[self.current_element_index]

    def previous(self):
        self.current_element_index -= 1 % len(self.categories)
        return self.categories[self.current_element_index]


class MenuIterator:
    def __init__(self, menu: Menu):
        self.stack = [menu.root]

    def __next__(self):
        if not self.stack:
            raise StopIteration("Finished Iteration")
        current_element = self.stack.pop()
        for category in current_element.children:
            self.stack.append(category)
        return current_element
