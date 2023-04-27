# Crear una clase CuentaBancaria
# Crea una clase llamada CuentaBancaria que tenga los siguientes atributos: número de cuenta, titular de la cuenta y saldo. La clase debe tener un método que permita depositar dinero en la cuenta y otro que permita retirar dinero de la cuenta. Además, debe haber un método que permita consultar el saldo de la cuenta.

# Crear una clase Animal
# Crea una clase llamada Animal que tenga un método para emitir un sonido. Luego, crea subclases de Animal para representar diferentes tipos de animales, como Perro, Gato, Vaca, etc. Cada subclase debe implementar el método para emitir el sonido característico de su animal correspondiente.
class CuentaBancaria:

    def __init__(self, titular, numero, saldo):

        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        titular = "Perico de los Palotes"
        numero = "ES32 5848 2727 1919 2020"
        saldo = 20450

    def __repr__(self, titular, numero, saldo):
        return f"{self.titular}, {self.numero}, {self.saldo}"

    def __str__(self, titular, numero, saldo):
        return f"{self.titular, self.numero, self.saldo}"


datos = CuentaBancaria("Perico de los Palotes",
                       "ES32 5848 2727 1919 2020", 20450)
datos
print(datos.titular, "con el número de cuenta",
      datos.numero, "tiene", datos.saldo, "€.")


class ConsultaSaldo(CuentaBancaria):
    def __init__(self, saldo):
        self.saldo = ConsultaSaldo(saldo)

    def __str__(self, saldo):
        return f"{self.saldo}"


class Depositar(CuentaBancaria):
    def __init__(self, saldo, deposito, depositonuevo):
        self.saldo = saldo
        self.deposito = deposito
        self.depositonuevo = depositonuevo

    def __str__(self, deposito):
        return f"{self.deposito}"

    def deposito(self, deposito):
        return f"{self.deposito}"

    def saldo(self, saldo):
        return f"{self.saldo}"

    def __str__(self, depositonuevo):
        return f"{self.depositonuevo}"

    def depositonuevo(saldo):
        deposito = int(input("Introduzca el importe a depositar "))
        return deposito + saldo

    print(datos.titular, "con el número de cuenta",
          datos.numero, "tiene", depositonuevo(datos.saldo), "€.")
