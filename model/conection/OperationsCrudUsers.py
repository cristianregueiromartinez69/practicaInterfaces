from DatabaseConection import *

from OperationsCreateTablesDB import  createUsuarios, createCoches, createMotos, createBicicletas, dropTables, create_table


dropTables()
create_table(createUsuarios())
create_table(createCoches())
create_table(createMotos())
create_table(createBicicletas())