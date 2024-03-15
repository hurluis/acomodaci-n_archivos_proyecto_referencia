# Clase de excepcion cuando el interes es muy alto
class ExcesiveInterestError( Exception ):
   pass

# Error cuando ingresan una compra menor o igual a cero
class InvalidPurchaseException( Exception ):
   """El monto de la compra no puede ser inferior a Cero"""

def calcPayment(purchase_amount,interest_rate,num_payments):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito
    compra : Valor de la compra con la tarjeta
    tasa : Debe ser un porcentaje entre 1 y 100
    plazo : numero de cuotas a diferir la compra

    El resultado no esta redondeado
    """

    # Verificamos que la tasa de interes no se a mayor que 3.8% mensual
    if interest_rate > ( 3.8/100 ) :
       raise ExcesiveInterestError( "ERROR: La tasa de interes supera el máximo. No puede superar 3.8%" )

    if purchase_amount <= 0 :
      raise InvalidPurchaseException(  )

    i = interest_rate
    return (purchase_amount * i) / (1 - (1 + i) ** (-num_payments))

