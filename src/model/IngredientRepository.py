import sqlite3
from config.Configuration import Configuration
from model.Ingredient import Ingredient


class IngredientRepository:

    def __init__(self):
        self.conf = Configuration.getInstance()
        self.conn = sqlite3.connect(self.conf.db.file)
        pass

    def add(self, data: Ingredient) -> int:
        stmt = '''
      INSERT INTO Ingredient(name, measure_unit, available) VALUES(?,?,?)
    '''
        cursor = self.conn.cursor()
        cursor.execute(stmt, (data.name, data.unit, data.available))
        self.conn.commit()
        id = cursor.lastrowid
        return id

    def delete(self, id):
        stmt = '''
      DELETE FROM Ingredient WHERE id = ?)
    '''
        cursor = self.conn.cursor()
        cursor.execute(stmt, (id,))
        self.conn.commit()
        return id

    def update(self, data: Ingredient) -> Ingredient:
        stmt = '''
      UPDATE SET name = ?, unit = ? WHERE id = ?
    '''
        cursor = self.conn.cursor()
        cursor.execute(stmt, (data.name, data.unit, data.available, data.id,))
        self.conn.commit()
        return data

    def getById(self, id) -> Ingredient:
        cursor = self.conn.execute("SELECT * FROM Ingredient WHERE id = ?",(id,))
        results = cursor.fetchall()
        if(len(results) == 0):
          return None
        ingredient: Ingredient = Ingredient()
        ingredient.id = results[0][0]
        ingredient.name = results[0][1]
        ingredient.unit = results[0][2]
        ingredient.available = results[0][3]
        

# Use Abastract base class module
