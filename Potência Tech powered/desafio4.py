def main():
 """Função para calcular o valor total de um pedido a ser pago
 com base no cupom de desconto escolhido."""

 n: int = int(input())

 total: float = 0

 for i in range(1, n + 1):
   pedido: str = input().split(" ")
    
   nome: str = pedido[0]
   valor: float = float(pedido[1])
   total += valor
 desconto: str = input()  

 match desconto:

  case '10%':
   valor_do_desconto: float = total * 0.1
   total -= valor_do_desconto
   
  case '20%':
   valor_do_desconto: float = total * 0.2
   total -= valor_do_desconto


 print(f'Valor total: {total:.2f}')    
 
if __name__ == "__main__":
  main()