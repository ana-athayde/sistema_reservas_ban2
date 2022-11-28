-- SQLBook: Code
-- DDL-SQL
CREATE DATABASE reservas;

CREATE TABLE cartao
(
	id_cartao serial NOT NULL,
	no_cartao char(16) NOT NULL,
	cod_seguranca char(3) NOT NULL,
	nome_proprietario character varying(50) NOT NULL,
	bandeira character varying(50) NOT NULL,
	data_vencimento date NOT NULL,
	CONSTRAINT cartao_pkey PRIMARY KEY (id_cartao)
	
);

ALTER TABLE cartao OWNER TO postgres;

CREATE TABLE pagamento
(
	id_pagamento serial NOT NULL,
	forma_pag boolean NOT NULL,
	total double precision NOT NULL,
	endereco_cob character varying(50) NOT NULL,
	parcelamento integer NOT NULL,
	nome_responsavel character varying(50) NOT NULL,
	id_cartao integer NOT NULL,
	CONSTRAINT pagamento_pkey PRIMARY KEY (id_pagamento),
	CONSTRAINT pagamento_fkey FOREIGN KEY (id_cartao) REFERENCES cartao (id_cartao)


);

ALTER TABLE pagamento OWNER TO postgres;

CREATE TABLE companhia
(
	id_companhia serial NOT NULL,
	nome character varying(50) NOT NULL,
	tarifa double precision NOT NULL,
	CONSTRAINT companhia_pkey PRIMARY KEY (id_companhia)
);

ALTER TABLE companhia OWNER TO postgres;

CREATE TABLE passagem
(
	id_passagem serial NOT NULL,
	preco double precision NOT NULL,
	no_assentos integer NOT NULL,
	id_companhia integer NOT NULL,
	CONSTRAINT passagem_pkey PRIMARY KEY (id_passagem),
	CONSTRAINT passagem_fkey FOREIGN KEY (id_companhia) REFERENCES companhia (id_companhia)

);

ALTER TABLE passagem OWNER TO postgres;


CREATE TABLE reserva
(
	id_reserva serial NOT NULL,
	prazo_validade date NOT NULL,
	quantidade integer NOT NULL,
	emitido boolean NOT NULL,
	bagagem boolean NOT NULL,
	id_pag integer NOT NULL,
	id_passagem integer NOT NULL,
CONSTRAINT reserva_pkey PRIMARY KEY (id_reserva),
CONSTRAINT reserva_fkey1 FOREIGN KEY (id_pag) REFERENCES pagamento (id_pagamento),
CONSTRAINT reserva_fkey2 FOREIGN KEY (id_passagem) REFERENCES passagem (id_passagem)
);

ALTER TABLE reserva OWNER TO postgres;

CREATE TABLE passageiro
(
	id_passageiro serial NOT NULL,
	nome character varying(50) NOT NULL,
	assistencia boolean NOT NULL,
	rg char(7) NOT NULL,
	cpf char(11) NOT NULL,
	crianca boolean NOT NULL,
	email character varying(50) NOT NULL,
	endereco character varying(50) NOT NULL,
	telefone character varying(50) NOT NULL,
	CONSTRAINT passageiro_pkey PRIMARY KEY (id_passageiro)
);

ALTER TABLE passageiro OWNER TO postgres;


CREATE TABLE horario
(
	id_horario serial NOT NULL,
	data_partida date NOT NULL,
	hora_partida time NOT NULL,
	data_chegada date NOT NULL,
	hora_chegada time NOT NULL,
	CONSTRAINT horario_pkey PRIMARY KEY (id_horario)
);

ALTER TABLE horario OWNER TO postgres;



CREATE TABLE pais
(
	id_pais serial NOT NULL,
	nome character varying(50) NOT NULL,
	cod_pais char(10) NOT NULL,
	CONSTRAINT pais_pkey PRIMARY KEY (id_pais)
);

ALTER TABLE pais OWNER TO postgres;

CREATE TABLE cidade
(
	id_cidade serial NOT NULL,
	nome character varying(50) NOT NULL,
	cod_cidade char(10) NOT NULL,
	id_pais integer NOT NULL,
	CONSTRAINT cidade_pkey PRIMARY KEY (id_cidade),
CONSTRAINT aeroporto_fkey FOREIGN KEY (id_pais) REFERENCES pais (id_pais)
);

ALTER TABLE cidade OWNER TO postgres;

CREATE TABLE aeroporto
(
	id_aeroporto serial NOT NULL,
	nome character varying(50) NOT NULL,
	id_cidade integer NOT NULL,
	CONSTRAINT aeroporto_pkey PRIMARY KEY (id_aeroporto),
	CONSTRAINT aeroporto_fkey FOREIGN KEY (id_cidade) REFERENCES cidade (id_cidade)
);

ALTER TABLE aeroporto OWNER TO postgres;

CREATE TABLE origem
(
	id_origem serial NOT NULL,
	id_aeroporto integer NOT NULL,
	CONSTRAINT origem_pkey PRIMARY KEY (id_origem),
	CONSTRAINT origem_fkey FOREIGN KEY (id_aeroporto) REFERENCES aeroporto (id_aeroporto)
);

ALTER TABLE origem OWNER TO postgres;

CREATE TABLE destino
(
	id_destino serial NOT NULL,
	id_aeroporto integer NOT NULL,
	CONSTRAINT destino_pkey PRIMARY KEY (id_destino),
	CONSTRAINT destino_fkey FOREIGN KEY (id_aeroporto) REFERENCES aeroporto (id_aeroporto)
);

ALTER TABLE destino OWNER TO postgres;

CREATE TABLE modelo_aeronave
(
	id_modelo serial NOT NULL,
	nome character varying(50) NOT NULL,
	max_assentos integer NOT NULL,
	empresa character varying(50) NOT NULL,
	capacidade_b double precision NOT NULL,
	CONSTRAINT modelo_aeronave_pkey PRIMARY KEY (id_modelo)
);

ALTER TABLE modelo_aeronave OWNER TO postgres;

CREATE TABLE aeronave
(
	id_aeronave serial NOT NULL,
	total_assentos integer NOT NULL,
	id_modelo integer NOT NULL,
	CONSTRAINT aeronave_pkey PRIMARY KEY (id_aeronave),
	CONSTRAINT aeronave_fkey FOREIGN KEY (id_modelo) REFERENCES modelo_aeronave (id_modelo)
);

ALTER TABLE aeronave OWNER TO postgres;

CREATE TABLE reserva_passageiro
(
	id_reserva integer NOT NULL,
	id_passageiro integer NOT NULL,
	CONSTRAINT reserva_passageiro_pkrp PRIMARY KEY (id_reserva, id_passageiro),
CONSTRAINT reserva_passageiro_fkey1 FOREIGN KEY (id_reserva) REFERENCES reserva (id_reserva),
CONSTRAINT reserva_passageiro_fkey2 FOREIGN KEY (id_passageiro) REFERENCES passageiro (id_passageiro)
);

ALTER TABLE reserva_passageiro OWNER TO postgres;

CREATE TABLE trecho
(
	id_trecho serial NOT NULL,
	classe character varying(50) NOT NULL,
	assento char(3) NOT NULL,
	id_horario integer NOT NULL,
	id_passagem integer NOT NULL,
	id_aeronave integer NOT NULL,
	id_origem integer NOT NULL,
	id_destino integer NOT NULL,
CONSTRAINT trecho_pkey PRIMARY KEY (id_trecho),
CONSTRAINT trecho_fkey1 FOREIGN KEY (id_horario) REFERENCES horario (id_horario),
CONSTRAINT trecho_fkey2 FOREIGN KEY (id_passagem) REFERENCES passagem (id_passagem),
CONSTRAINT trecho_fkey3 FOREIGN KEY (id_aeronave) REFERENCES aeronave (id_aeronave),
CONSTRAINT trecho_fkey4 FOREIGN KEY (id_origem) REFERENCES origem (id_origem),
CONSTRAINT trecho_fkey5 FOREIGN KEY (id_destino) REFERENCES destino (id_destino)
);

ALTER TABLE trecho OWNER TO postgres;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

INSERT INTO cartao (no_cartao, cod_seguranca, nome_proprietario, bandeira, data_vencimento) VALUES ('1111222233334444', '123', 'Luiz F Almeida', 'Visa', '2029-03-22'), ('1234123412341234', '000', 'Jose C da Silva', 'Mastercard', '2026-06-01'), ('6789678967896789', '555', 'Luisa Ferreira', 'Elo', '2028-04-30'), ('5555666677778888', '666', 'Luana S Oliveira', 'Visa', '2030-06-08'), ('7777432155556789', '333', 'Pedro Rodrigues', 'Mastercard', '2027-07-07');

INSERT INTO pagamento (forma_pag, total, endereco_cob, parcelamento, nome_responsavel, id_cartao) VALUES (true, 359.99, 'rua abc 454', 4, 'Marcia Torres', 5), (true, 484.50, 'rua fgh 88', 6, 'Luana S Oliveira', 4), (true, 120.20, 'rua tres 33', 2, 'Luisa Ferreira', 3), (false, 99.99, 'rua dezoito 18', 2, 'Jose C da Silva', 2), (true, 120.20, 'rua treze 13', 3, 'Luiz F Almeida', 1);

INSERT INTO companhia (nome, tarifa) VALUES ('VoeBem', 23.79), ('Ceu Linhas Aereas', 25.99), ('VooRapido', 32.00), ('Aves Aviação', 21.99), ('Expresso Linhas Aéreas', 24.49);

INSERT INTO passagem (preco, no_assentos, id_companhia) VALUES (359.99, 68, 1), (484.50, 118, 2), (120.20, 138, 3), (99.99, 144, 4), (120.20, 146, 5);

INSERT INTO reserva (prazo_validade, quantidade, emitido, bagagem, id_pag, id_passagem) VALUES ('2022-12-12', 1, false, true, 1, 1), ('2022-11-10', 2, true, true, 2, 2), ('2023-01-22', 1, false, false, 3, 3), ('2022-08-04', 1, true, false, 4, 4), ('2023-02-25', 2, false, false, 5, 5);

INSERT INTO passageiro (nome, assistencia, rg, cpf, crianca, email, endereco, telefone)  VALUES ('Paulo', false, '1234567', '01234567891', false, 'email@abc.com', 'rua endereco etc 123', '1234-5678'), ('Luana', false, '3216549', '22222222222', false, 'email2@abc.com', 'rua dois 48', '3322-4455'), ('Pedro', true, '1111111', '11111111111', false, 'email3@abc.com', 'rua tres 89', '5588-9977'), ('Joana', false, '3333333', '55555555555', true, 'email4@abc.com', 'rua quatro 34', '7898-5231'), ('Marcia', false, '1236548', '98765432155', false, 'email5@abc.com', 'rua cinco 66', '3366-4412');

INSERT INTO horario (data_partida, hora_partida, data_chegada, hora_chegada) VALUES ('2022-12-12', '14:20', '2022-12-12', '15:20'), ('2022-11-10', '20:30', '2022-11-10', '22:00'), ('2023-01-22', '17:50', '2023-01-22', '18:50'), ('2022-08-04', '08:40', '2022-08-04', '10:10'), ('2023-02-25', '15:00', '2023-02-25', '15:50');

INSERT INTO pais (nome, cod_pais) VALUES ('Brasil', 'BRA'), ('Bolivia', 'BOL'), ('Colombia', 'COL'), ('Argentina', 'ARG'), ('Chile', 'CHI');

INSERT INTO cidade (nome, cod_cidade, id_pais) VALUES ('Sao Paulo', 'SP', 1), ('La Paz', 'LP', 2), ('Bogota', 'BG', 3), ('Buenos Aires', 'BA', 4), ('Santiago', 'ST', 5);

INSERT INTO aeroporto (nome, id_cidade) VALUES ('Congonhas', 1), ('El Alto', 2), ('El Dorado', 3), ('Ezeiza', 4), ('Pudahuel', 5);

INSERT INTO origem (id_aeroporto) VALUES (1), (2), (3), (4), (5);

INSERT INTO destino (id_aeroporto) VALUES (3), (1), (5), (2), (4);

INSERT INTO modelo_aeronave (nome, max_assentos, empresa, capacidade_b) VALUES ('ATR 72-500', 68, 'VoeBem', 22000), ('Embraer 195', 118, 'Ceu Linhas Aereas', 51000), ('Boeing 737-700', 138, 'VooRapido', 68000), ('Airbus A319', 144, 'Aves Aviação', 73000), ('Embraer 195 E-2', 146, 'Expresso Linhas Aereas', 51000);

INSERT INTO aeronave (total_assentos, id_modelo) VALUES (68, 1), (118, 2), (138, 3), (144, 4), (146, 5);

INSERT INTO reserva_passageiro (id_reserva, id_passageiro) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5);

INSERT INTO trecho (classe, assento, id_horario, id_passagem, id_aeronave, id_origem, id_destino) VALUES ('Executiva', '08A', 1, 1, 1, 1, 1), ('Primeira', '22D', 2, 2, 2, 2, 2), ('Economica', '15C', 3, 3, 3, 3, 3), ('Executiva', '02F', 4, 4, 4, 4, 4), ('Economica', '25A', 5, 5, 5, 5, 5);
