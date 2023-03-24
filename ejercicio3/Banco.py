
class CuentaBancaria:
    def __init__(self, nombre, fecha_apertura, saldo_inicial):
        self.id = None
        self.nombre = nombre
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = str(random.randint(10**11, 10**12-1))
        self.saldo = saldo_inicial

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("No se puede retirar más dinero del disponible en la cuenta.")
            return False
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}€ de la cuenta.")
            return True

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Se han ingresado {cantidad}€ en la cuenta.")

    def transferir_dinero(self, cantidad, cuenta_destino):
        if cantidad > self.saldo:
            print("No se puede transferir más dinero del disponible en la cuenta.")
            return False
        else:
            self.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            print(f"Se han transferido {cantidad}€ a la cuenta de {cuenta_destino.nombre}.")
            return True
class Cuentapplazofijo(CuentaBancaria):
    def __init__(self, nombre, fecha_apertura, fecha_vencimiento, saldo_inicial):
        super().__init__(nombre, fecha_apertura, saldo_inicial)
        self.fecha_vencimiento = fecha_vencimiento

    def retirar_dinero(self, cantidad):
        if date.today() < self.fecha_vencimiento:
            cantidad += cantidad * 0.05 
        return super().retirar_dinero(cantidad)
class cuentaviip(cuentabancria):