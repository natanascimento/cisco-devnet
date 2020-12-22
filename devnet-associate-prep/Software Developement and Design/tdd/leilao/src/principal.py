from dominio.dominio import Usuario, Lance, Leilao, Avaliador

natan = Usuario('Natan')
jessica = Usuario('Jessica')

lance_natan = Lance(natan, 100.0)
lance_jessica = Lance(jessica, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_natan)
leilao.lances.append(lance_jessica)

for lance in leilao.lances:
    print('Leilao de {} \nO usuario {} deu um lance de {}'.format(leilao.descricao, lance.usuario.nome, lance.valor))
    
avaliador = Avaliador()
avaliador.avalia(leilao)

print('O menor lance foi de {} e o maior lance foi de {}'.format(avaliador.menor_lance, avaliador.maior_lance))