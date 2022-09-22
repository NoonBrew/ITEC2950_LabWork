from cgitb import text
from unicodedata import name
from peewee import *

db = SqliteDatabase('cats.sqlite') # Can call db files with .sqlite or .db based on prefrence

# class Owner(Model):
#     name = CharField()

#     class Meta:
#         database = db

#     def __str__(self):
#         return f'{self.id}, {self.name}'

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()
    #owner = ForeignKeyField(Owner, backref='cats')

    class Meta: # Associates a speceic model class with a DB
        database = db

    def __str__(self):
        return f'{self.id}, {self.name}, {self.color}, {self.age}' #ID is made my the database we are not defining it.


db.connect()
db.create_tables([Cat]) # create tables expects a list of tables

Cat.delete().execute() # Clears data from table at start so we do not keep readding the same sample data.
# Sample Cat Data
# Owner.delete().execute()

#### 
# sam = Owner(name='Sam')
# sam.save()

# lily = Cat(name='Lily', color='Black', age=1, owner=sam)
# lily.save()

# print(lily)
# print(lily.owner.name)

zoe = Cat(name='Zoe', color='Ginger', age=3)
zoe.save() # Make sure to save. This is like a commit

holly = Cat(name='Holly', color='Tabby', age=5)
holly.save()

fluffy = Cat(name='Fluffy', color='Black', age=1)
fluffy.save()

bro_bro = Cat(name='Bro Bro', color='Tuxedo', age=10)
bro_bro.save()

cats = Cat.select()
# cats is a query object after this select statment.
# Cannot access a query object by index so cats[0] IS NOT going to return row 1.

for row in cats:
    print(row)

list_of_cats = list(cats) # Turns the query object into a list that can be accessed by index. 

'''CRUD OPERATIONS
Create - insert
Read - select
Update
Delete
'''

fluffy.age = 2 # Can update like you would a object normally by calling the field and saving
fluffy.save()

print('After Fluffy age changed')
cats = Cat.select()
for cat in cats:
    print(cat)

rows_modified = Cat.update(age=6).where(Cat.name == 'Holly').execute()

print('After Holly age changed')

cats = cat.select()
for cat in cats:
    print(cat)

print('Rows Modified:')
print(rows_modified)

buzz = Cat(name='Buzz', color='Gray', age=3)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, 'cats that are 3')

cat_with_l_in_name = Cat.select().where(Cat.name % '*l*') # * == Wildcard symbol
# .where(Cat.name.contains % '*l*') would allow for non-casesensetive searching. Need .contains
for cat in cat_with_l_in_name:
    print(cat, 'has l in name')

zoe_from_db = Cat.get_or_none(name='Zoe') # Will return a None value if in this case Zoe is not a named cat in the database.
print(zoe_from_db)

cat_1 = Cat.get_by_id(1) # If the ID does not exist it will raise an exception.
print(cat_1)

# Count, sort, limit
total_cats = Cat.select().count()
print(total_cats)

total_cats_who_are_3 = Cat.select().where(Cat.age == 3).count()
print(total_cats_who_are_3)

cats_sorted_by_name = Cat.select().order_by(Cat.name.desc()) # ascending order is default, .asc() to force ascending order.
print(list(cats_sorted_by_name))

first_3_cats = Cat.select().order_by(Cat.name).limit(3)

print(list(first_3_cats))

# delete

rows_deleted_with_where = Cat.delete().where(Cat.name == 'Holly').execute()
print(list(Cat.select()))

rows_delete_with_all = Cat.delete().execute() # DELETES EVERYTHING IN TABLE (table still exists.)
print(list(Cat.select()))

print(rows_deleted_with_where)
print(rows_delete_with_all)