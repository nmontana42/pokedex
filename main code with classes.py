import csv
import sqlite3
from sqlite3 import Error
import re
#Search finds base data, returns requests, constraints, executes SQL commands
class Search:

    type_list = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass",
             "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]
    gen_list = ['1','2','3','4','5','6']

    stat_list = ["total", "HP", "Attack", "Defense", "Speed"]

    def __init__(self, conn, response, data):
        self.response = response
        self.constraint = None
        self.data = data
        self.conn = conn
    def regex(self):
        for self.request in self.data:
            if re.search(self.request, self.response, re.IGNORECASE):
                self.constraint = True
                return self.request
        if self.constraint is True:
            return self.constraint
    def regex_Bravo(self):
        if re.search('legendar(ies)?', self.response, re.IGNORECASE):
            self.constraint = True
            return self.constraint

class Find(Search):

    def __init__(self, conn, Generation, Types, Statement):
        self.Generation = Search(conn, response, Search.gen_list)
        self.Types = Search(conn, response, Search.type_list)
        self.statement = statement
        self.conn = conn

        
    def sql_Generation(self):
        Search.regex(Generation)
        cur = self.conn.cursor()
        if Generation.constraint is True:
            cur.execute(self.statement, (self.request,))
            record = cur.fetchall()
            for row in record:
                print(row)
    def sql_Types(self):
        Search.regex(Types)
        cur = self.conn.cursor()
        if Types.constraint is True:
            cur.execute(self.statement, (self.request, self.request))
            record = cur.fetchall()
            for row in record:
                print(row)
#Create the connection to sqlite
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def user_input():
    global response
    
    response = input()
    return True
    return response

            
def main():
    database = 'pokemon.db'
    conn = create_connection(database)
    while user_input() == True:

            
if __name__ == '__main__':
    main()