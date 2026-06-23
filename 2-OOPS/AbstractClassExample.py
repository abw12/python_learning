from abc import abstractmethod,ABC

# ABC` class from the `abc` module, which stands for Abstract Base Class
class PaymentMethod(ABC): 

    @abstractmethod
    def payOnline(paymentId:str,amount:int):
        pass
    
    @abstractmethod
    def emi(cardDetails:str,amount:int):
        pass

class HDFCCreditCard(PaymentMethod):

    def payOnline(self,paymentId: str, amount: int):
        return f"Payment ID = ${paymentId} with Amount = ${amount}"
    def emi(self,cardDetails: str, amount: int):
        return f"Payment with Card = ${cardDetails} for amount =${amount}"

class AXISCeditCard(PaymentMethod):

    def payOnline(self,paymentId:str,amount:int):
        return f"Payment ID = ${paymentId} with Amount = ${amount}"
    def emi(self,cardDetails:str,amount:int):
        return f"Payment with card = ${cardDetails} for amount=${amount}"
    

hdfc = HDFCCreditCard()
axis = AXISCeditCard()
print(hdfc.payOnline("jau78#a0",7000))
print(axis.payOnline("axssde0982$#32",9000))