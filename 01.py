class Curupira:
    def __init__(self, altura, poder, maturidade):
        self.altura = altura
        self.poder = poder
        self.maturidade = maturidade

    def mostrar_informacoes(self): 
        return f"Curupira - Altura: {self.altura}m | Poder: {self.poder} | Maturidade: {self.maturidade}"


curupira1 = Curupira(1.40, "Proteger a floresta", "Jovem")
curupira2 = Curupira(1.60, "Confundir caçadores", "Adulto")

print(curupira1.mostrar_informacoes())
print(curupira2.mostrar_informacoes())
