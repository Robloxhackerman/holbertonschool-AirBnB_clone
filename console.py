#!/usr/bin/python3
"""aaaaa"""

import cmd
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None
    clases = ["BaseModel"]

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def do_create(self, arg):    
        comandito = arg.split()

        if comandito == None:
            print("** class name missing **")
        elif comandito[0] not in self.clases:
            print("** class doesn't exist **")
        else:
            cosita = eval(comandito[0])()
            cosita.save()
            print(cosita.id)
    
    def emptyline(self):
        pass

    def do_show(self, arg):
        comandito = arg.split()
        arg1 = comandito[0]
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
