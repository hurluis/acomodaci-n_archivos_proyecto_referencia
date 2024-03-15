# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
#Lo importamos para incluir la ruta de busqueda de python
import sys
sys.path.append("src")
from CreditCard import PaymentLogic 


# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testPayment1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        # Datos de Entrada
        purchase_amount = 200000
        interest_rate = 0.031
        num_payments = 36

        # Proceso
        result = PaymentLogic.calcPayment( purchase_amount, interest_rate, num_payments )

        # Datos de salida esperados
        expected = 9297.96

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( expected, result, 2  )

    def testExcesiveInterest( self ):
        # Entradas
        purchase_amount = 50000
        num_payments = 36
        interest_rate = 0.124

        testOk = False  # Bandera para indicar si la prueba es exitosa
        try:
            # llamar al proceso
            result = PaymentLogic.calcPayment( purchase_amount, interest_rate, num_payments )
            print("No ocurrió ningun excepcion")
            testOk = False
        except PaymentLogic.ExcesiveInterestError :
            # Aqui llega el control cuando se genera una excepcion
            print("SI ocurrio la excepcion")
            testOk = True

        self.assertTrue(  testOk, "No se disparó la excepcion esperada" )            

    def testExcesiveInterestOneLine( self ):
        # Entradas
        purchase_amount = 50000
        num_payments = 36
        interest_rate = 0.124

        # Verifica en una linea si una funcion dispara una excepcion
        self.assertRaises( PaymentLogic.ExcesiveInterestError, PaymentLogic.calcPayment, purchase_amount, interest_rate, num_payments  )


    def testPurchaseZero( self ):
        # Entradas
        purchase_amount = 0
        num_payments = 60
        interest_rate = 0.024

        # Verifica en una linea si una funcion dispara una excepcion por no haber compra
        self.assertRaises( PaymentLogic.InvalidPurchaseException, PaymentLogic.calcPayment, purchase_amount, interest_rate, num_payments  )

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()