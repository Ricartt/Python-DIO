valorPedido = int(input())

match valorPedido:

 case _ as valor if valor >=50:
  print('Parabens, você ganhou uma sobremesa gratis!')
  
 case _:
  print('Que pena, você nao ganhou nenhum brinde especial.')