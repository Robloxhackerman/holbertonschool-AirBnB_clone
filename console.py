#!/usr/bin/python3
"""aaaaa"""

import cmd
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import datetime

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None
    clases = ["BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"]

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def do_create(self, arg):
        comandito = []
        if len(arg) != 0:
            comandito = arg.split()

            if comandito is None:
                print("** class name missing **")
            elif comandito[0] not in self.clases:
                print("** class doesn't exist **")
            else:
                cosita = eval(comandito[0])()
                cosita.save()
                print(cosita.id)
        else:
            print("** class name missing **")
    
    def emptyline(self):
        pass

    def do_show(self, arg):
        comandito = []
        if len(arg) != 0:
            comandito = arg.split()
            arg1 = comandito[0]

            if len(comandito) > 1:
                arg2 = comandito[1]

                if comandito == None:
                    print("** class name missing **")
                elif arg1 not in self.clases:
                    print("** class doesn't exist **")
                elif arg2 == None:
                    print("** instance id missing **")
                else:
                    datin = models.storage.all().get(arg1 + "." + arg2)
                    if datin == None:
                        print("** no instance found **")
                    else:
                        print(datin)
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **") 

    def do_destroy(self, arg):
        comandito = []
        if len(arg) != 0:
            comandito = arg.split()
            arg1 = comandito[0]

            if len(comandito) > 1:
                arg2 = comandito[1]

                if comandito == None:
                    print("** class name missing **")
                elif arg1 not in self.clases:
                    print("** class doesn't exist **")
                elif arg2 == None:
                    print("** instance id missing **")
                else:
                    datin = models.storage.all().get(arg1 + "." + arg2)
                    if datin == None:
                        print("** no instance found **")
                    else:
                        del models.storage.all()[arg1 + "." + arg2]
                        models.storage.save()
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
       comandito = arg.split()
       cositas = models.storage.all()
       queis = cositas.keys()

       if len(arg) == 0:
           for PEPE1 in cositas:
               print(str(cositas[PEPE1]))
       elif comandito[0] not in self.clases:
           print("** class doesn't exist **")
       else:
           queis = cositas.keys()
           for PEPE2 in queis:
               if PEPE2.startswith(comandito[0]):
                   print(str(cositas[PEPE2]))

    def do_update(self, arg):
        comandito = arg.split()
        arg1 = ""
        arg2 = ""
        arg3 = ""
        arg4 = ""
        if len(comandito) == 0:
            print("** class name missing **")
        elif comandito[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(comandito) == 1:
            arg1 = comandito[0]
            print("** instance id missing **")
        elif len(comandito) == 2:
            arg2 = comandito[1]
            print("** attribute name missing **")
        elif len(comandito) == 3:
            arg3 = comandito[2]
            print("** value missing **")
        else:
            arg4 = comandito[3]
            datin = models.storage.all().get(arg1 + "." + arg2)
            if datin is None:
                print("** no instance found **")
            else:
                if arg3.isdigit():
                    arg3 = int(arg3)
                elif arg3.replace('.', '', 1).isdigit():
                    arg3 = float(arg3)
                if arg4.isdigit():
                    arg4 = int(arg4)
                elif arg4.replace('.', '', 1).isdigit():
                    arg4 = float(arg4)
                setattr(datin, arg3, arg4)
                setattr(datin, 'updated_at', datetime.datetime.now())
                models.storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
