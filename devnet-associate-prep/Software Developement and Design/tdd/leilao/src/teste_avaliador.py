from unittest import TestCase
from dominio.dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    
    def test_avalia(self):
        natan = Usuario('Natan')
        jessica = Usuario('Jessica')
        
        lance_natan = Lance(natan, 100.0)
        lance_jessica = Lance(jessica, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_natan)
        leilao.lances.append(lance_jessica)
        
        avaliador = Avaliador()
        avaliador.avalia(leilao)
        
        menor_valor_esperado = 100
        maior_valor_esperado = 150
        
        teste_menor_valor = self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        teste_maior_valor = self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        
        if teste_maior_valor == None and teste_maior_valor == None:
            print("OK!")
        else:
            print ("{} \n {}".format(teste_menor_valor, teste_maior_valor))
        
if __name__ == '__main__':
    main = TestAvaliador()
    main.test_avalia()