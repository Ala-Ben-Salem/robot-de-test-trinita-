class Param:
    def __init__(self, url, login, psw, option):
        self.url = url
        self.login = login
        self.psw = psw
        self.option = option

    def __str__(self):   # comment representer
        return (f"URL: {self.url} , "
                f"LOGIN: {self.login}, "
                f"PASSWORD: {self.psw}, "
                f"OPTION: {self.option}")

    @classmethod
    def from_dict(cls, data):
        """Create an Adherent instance from a dictionary."""
        return cls(
            url=data.get('url'),
            login=data.get('login'),
            psw=data.get('psw'),
            option=data.get('option'),
        )