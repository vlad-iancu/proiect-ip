import sqlite3
from src.config.Configuration import Configuration
from src.models.Ingredient import Ingredient
from typing import List
from src.db import get_db


class IngredientRepository:

    def __init__(self):
        self.conf = Configuration.getInstance()
        self.conn = get_db()
        #self.conn = sqlite3.connect(self.conf.db.file, check_same_thread=False)

    def add(self, data: Ingredient) -> int:
        stmt = '''
      INSERT INTO Ingredient(name, measure_unit, available) VALUES(?,?,?)
    '''
        cursor = self.conn.cursor()
        cursor.execute(stmt, (data.name, data.unit, data.available))
        self.conn.commit()
        id = cursor.lastrowid
        return id

    def delete(self, id: int):
        existingIngredient = self.getById(id)
        if existingIngredient == None:
            return 0
        stmt = '''
      DELETE FROM Ingredient WHERE id = ?
    '''
        cursor = self.conn.cursor()
        cursor.execute(stmt, (id,))
        self.conn.commit()
        return id

    def update(self, data: Ingredient) -> Ingredient:
        stmt = '''
      UPDATE Ingredient SET name = ?, measure_unit = ?, available = ? WHERE id = ?
    '''
        cursor = self.conn.cursor()
        cursor.execute(stmt, (data.name, data.unit, data.available, data.id,))
        self.conn.commit()
        return data

    def getById(self, id: int) -> Ingredient:
        cursor = self.conn.execute("SELECT * FROM Ingredient WHERE id = ?", (id,))
        results = cursor.fetchall()
        if(len(results) == 0):
            return None
        ingredient: Ingredient = Ingredient()
        ingredient.id = results[0][0]
        ingredient.name = results[0][1]
        ingredient.unit = results[0][2]
        ingredient.available = results[0][3]
        return ingredient

    def getAll(self) -> List[Ingredient]:
        cursor = self.conn.execute("SELECT * FROM Ingredient ORDER BY id ASC")
        results: List[Ingredient] = []
        rows = cursor.fetchall()
        for row in rows:
            ingredient: Ingredient = Ingredient()
            ingredient.id = row[0]
            ingredient.name = row[1]
            ingredient.unit = row[2]
            ingredient.available = row[3]
            results.append(ingredient)
        return results

# Use Abastract base class module
