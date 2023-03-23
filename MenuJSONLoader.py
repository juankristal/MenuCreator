from models.Menu import Menu


class MenuJSONLoader:
    def parse(self, filename: str) -> Menu:
        return Menu()
