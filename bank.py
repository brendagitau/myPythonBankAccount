class Account:
    
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transactionfee= 30
        self.loanlimit=1000
        self.loan=0
        self.loanfees=(0.05*self.loan)

        
        
    def deposit(self,depo_amount):
        if depo_amount <=0:
            print ("Enter a valid amount")
        else:
            self.balance=self.balance+depo_amount
            return f"{self.name} you have deposited {depo_amount} your new balance is {self.balance}"

    def widthdraw(self , widthdraw_amount)  :
        total=widthdraw_amount+self.transactionfee
        if  self.balance== 0:
          
            return f"{self.name} you have insufficient balance in your accout to make this transaction " 
            
        elif total>self.balance:
            return f"{self.name} your account balance {self.balance} is not enough to support transaction fee"

        elif total<self.balance:
            new_balance=self.balance-widthdraw_amount-self.transactionfee
            return f"{self.name} you have sucessfully withdrawn  {widthdraw_amount} from your account with a fee of {self.transactionfee}.Your new balance is {new_balance}"
    def borrow(self,borrow_amount) :
           
            
        if borrow_amount<=0:
             return f"unsucessful!Amount requested {borrow_amount} is below 0 your current loan limit is {self.loanlimit}"
    
        elif borrow_amount<=self.loanlimit:
            self.loanfees=0.05*borrow_amount
            self.loan=borrow_amount+self.loanfees
            return f"You have recieved your loan of {borrow_amount}.You will be charged an interest of {self.loanfees} per month till you  finish paying."
        else :
                return f" Failed.you have an existing loan."