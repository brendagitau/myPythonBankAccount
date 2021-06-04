class Bank:
    type="premium"#shared attribute
    def __init__(self,name,amount,currency,krapin):
        self.name=name
        self.amount=amount
        self.currency=currency
        self.krapin=krapin
    def balance(self):
        return f"Hello {self.name}.You are a {self.type} account holder and  your  current balance is {self.amount} {self.currency}."    
    def pin(self):
        return f"As requested your KRA pin is {self.krapin} ."    