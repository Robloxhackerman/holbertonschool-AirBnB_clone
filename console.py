#!/usr/bin/python3
"""aaaaa"""

import cmd
from models.base_model import BaseModel
from models import storage
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
        elif comandito not in self.clases:
            print("** class doesn't exist **")
        else:
            cosita = eval(comandito[0])()
            cosita.save()
            print(cosita.id)
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
