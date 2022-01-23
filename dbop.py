from src.Database import Database

class Dbop(object):


    def __init__(self, decision_vector, x, y, type, cause, treatment, heredity):
        self.decision_vector = decision_vector
        self.x = x
        self.y = y
        self.type = type
        self.cause = cause
        self.treatment = treatment
        self.heredity = heredity


    def insert_to_database(self):
        Database.insert(collection='Db',
                        data=self.json())

    @staticmethod
    def update_0f_database(query, new_values):
        Database.update(query, new_values, collection = 'Db')

    @staticmethod
    def show_all_values_in_database():
        x = Database.find(collection = 'Db', query = None)
        for p in x:
            print(p)

    @staticmethod
    def find_particular_value_in_database(_id):
        x = Database.find_one(collection = 'Db', query = _id)

        print('x = ',x)
        print('vector = ',_id )

    @staticmethod
    def delete_a_record(_id):
        Database.delete(_id, collection = 'Db')

    def json(self):
        return{
            'Decision Vector': self.decision_vector,
            'Type': self.type,
            'G1': self.x,
            'G2': self.y,
            'Cause': self.cause,
            'Treatment': self.treatment,
            'Heredity': self.heredity
        }







