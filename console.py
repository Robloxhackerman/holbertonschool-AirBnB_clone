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
        comandito = []
        if len(arg) != 0:
            comandito = arg.split()

            if comandito == None:
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

            if len(arg) == 2:
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
