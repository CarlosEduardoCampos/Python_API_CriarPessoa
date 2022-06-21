from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'               # Cria uma tabela
    id = Column(Integer, primary_key=True)  # Chave primaria : valor inteiro
    nome = Column(String(40), index=True)   # Texto : valor string : temanho 40 caracteres
    # nc_data = Column(Integer)             # Data de nacimento
    cpf = Column(String(11))                # Numero de Cpf
    rg = Column(String(12))                 # Numero do RG

    # Resposta padrão para requisição de dados
    def __repr__(self):
        return f'<ID = {self.id} / Pessoa = {self.nome}>'

    # Cadastra um objeto no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Exclui um cadastro do banco
    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
