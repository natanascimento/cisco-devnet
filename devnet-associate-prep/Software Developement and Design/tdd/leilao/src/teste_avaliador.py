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
        
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        
if __name__ == '__main__':
    main = TestAvaliador()
    main.test_avalia()