
class NotAvailableDomen(Exception):
    def __init__(self, domen) -> None:
        super().__init__(
            f'Домен {domen} не зарегистрирован в базе или закончилась подписка.')
        
class EmailIsBusy(Exception):
    
    def __init__(self, email):
        super().__init__(
            f'Электронный адрес <<{email}>> занят, выберите другой.')
    