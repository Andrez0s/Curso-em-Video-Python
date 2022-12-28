# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato Brasileiro de Futebol,
# Na ordem de colocação, Depois mostre: A > Apenas os 5 primeiros colocados, B > Os últimos 4 colocados
# C > Uma lista com os times em ordem alfabética, D > Em que posição na tabela esta a Chapecoense

teams = (
        "Flamengo", "São Paulo", "Internacional", "Palmeiras", "Corinthians", "Atlético Mineiro", "Athletico Paranaense",
        "Fortaleza", "Ceará", "Fluminense", "Atlético Goianiense", "Santos", "Botafogo", "Athletico Paranaense", "Cuiabá",
        "Goiás", "Coritiba", "Sport Recife", "Bragantino", "Red Bull Bragantino"
        )
print(f'Os primeiros 5 times são {teams[0:5]}')
print(f'Os 4 últimos times são {teams[16:20]}')
print(f'Times em ordem alfabética: {sorted(teams)}')
print(f'O são paulo está na posição {teams.index("São Paulo") + 1}°')
