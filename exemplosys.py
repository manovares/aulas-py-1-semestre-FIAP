import sys

def main():
    if(len(sys.argv) == 3):
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        resultado = calcular_soma(num1, num2)
        print(f"A soma de {num1} e {num2} é: {resultado}")
    else: 
        print("Por favor, forneça dois números como argumentos de linha de comando.")
    




def calcular_soma(num1, num2):
    soma = num1 + num2
    return soma


if __name__ == "__main__":
    main()
