import csv

def carregar_dados(filename):
    dados = []
    with open(filename, encoding='latin-1') as csvfile:
        leitor = csv.reader(csvfile)
        header = next(leitor)  
        for linha in leitor:
            try:
                track_name = linha[0]
                artist_name = linha[1]
                artist_count = int(linha[2])
                released_year = int(linha[3])
                streams = int(linha[8])
                
                if 2012 <= released_year <= 2022:
                    dados.append([track_name, artist_name, released_year, streams])
            except:
                continue 

    return dados

def obter_musicas_top_por_ano(dados):
    top_musicas_por_ano = {}
    for track_name, artist_name, released_year, streams in dados:
        if released_year not in top_musicas_por_ano:
            top_musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]
        else:
           
            if streams > top_musicas_por_ano[released_year][3]:
                top_musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]
  
    top_musicas_ordenadas = [top_musicas_por_ano[ano] for ano in sorted(top_musicas_por_ano.keys())]
    return top_musicas_ordenadas

filename = 'spotify-2023.csv'

dados = carregar_dados(filename)

top_musicas_ordenadas = obter_musicas_top_por_ano(dados)

for musica in top_musicas_ordenadas:
    print(musica)
