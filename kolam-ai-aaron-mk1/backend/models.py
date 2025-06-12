from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///hotel_assistant.db', echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class ChatHistory(Base):
    __tablename__ = 'chat_history'
    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)  # 'guest' or 'bot'
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class MemoryLog(Base):
    __tablename__ = 'memory_log'
    id = Column(Integer, primary_key=True, index=True)
    memory = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
