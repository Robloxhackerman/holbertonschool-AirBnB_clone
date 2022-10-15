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
            
            if arg1 not in self.clases:
                print("** class doesn't exist **") 
            if len(arg) != 1:
                arg2 = comandito[1]
                
                datin = models.storage.all().get(arg1 + "." + arg2)
            elif datin is None:
                print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        comandito = []
        if len(arg) != 0:
            comandito = arg.split()
            arg1 = comandito[0]

            if len(arg) != 1:
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
        if len(arg) == 0:
            print("** class name missing **")
        elif comandito[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            if len(arg) > 3:
                arg1 = comandito[0]
                arg2 = comandito[1]
                datin = models.storage.all().get(arg1 + "." + arg2)
                if datin is None:
                    print("** no instance found **")
                elif len(arg) == 2:
                    print("** attribute name missing **")
                elif len(arg) == 3:
                    print("** value missing **")
                else:
                    arg3 = comandito[2]
                    arg4 = comandito[3]
                    setattr(datin, arg3, arg4)
                    setattr(datin, "updated_at", datetime.datetime.now())
                    models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
