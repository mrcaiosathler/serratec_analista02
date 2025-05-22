-- Criação da tabela 'pessoas', para teste
CREATE TABLE pessoas (
  id SERIAL PRIMARY KEY,
  nome TEXT,
  idade INTEGER,
  cidade TEXT
);


-- Inserção de Dados na Tabela
INSERT INTO pessoas (nome, idade, cidade)
VALUES
('Caio', 31, 'Petrópolis'),
('Natasha', 31, 'Petrópolis');


-- SELECT para visualização do conteúdo da Tabela, após inserção
SELECT * FROM pessoas;
