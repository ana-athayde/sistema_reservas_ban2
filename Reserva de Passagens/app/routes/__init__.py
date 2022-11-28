from app.routes import aeronave, aeroporto, cidade, destino, origem, pagamento, passagem, reserva_passageiro, reserva, trecho

blueprints = [
    aeronave.blue, 
    aeroporto.blue,
    cidade.blue,
    destino.blue,
    origem.blue,
    pagamento.blue,
    passagem.blue,
    reserva_passageiro.blue,
    reserva.blue,
    trecho.blue
]