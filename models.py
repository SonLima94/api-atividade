from sqlalchemy import create_engine, Collumn, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Collumn(Integer, primary_key=True)
    nome = Collumn(String(40), index=True)
    idade = Collumn(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Collumn(Integer, primary_key=True)
    nome = Collumn(String(80))
    pessoa_id = Collumn(Integer, ForeignKey=True('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Usuario(Base):
    __tablename__ == 'usuarios'
    id = Collumn(Integer, primary_key=True)
    login = Collumn(String(20), unique=True)
    senha = Collumn(String(20))

    def __repr__(self):
        return '</Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit

    

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()