from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


# 1. Определяем модель SQLModel
class Hero(SQLModel, table=True):  # table=True делает эту модель таблицей в БД
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True) # index=True создаст индекс по этому полю
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)



# Данные для подключения к БД (например, SQLite)
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True) # echo=True для вывода SQL-запросов


# 2. Функция для создания таблиц
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# 3. CRUD операции (пример)
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero

def get_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes


print(Hero(name="Deadpond", secret_name='Dive Wilson', age=48))  # Пример создания объекта Hero

# Основная часть для демонстрации
if __name__ == "__main1__":
    create_db_and_tables()

    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=16)
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


    created_hero_1 = create_hero(hero_1)
    created_hero_2 = create_hero(hero_2)
    created_hero_3 = create_hero(hero_3)


    print("Created heroes:")
    print(created_hero_1)
    print(created_hero_2)
    print(created_hero_3)

    all_heroes = get_heroes()
    print("\nAll heroes in DB:")
    for hero in all_heroes:
        print(hero)