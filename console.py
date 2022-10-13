#!/usr/bin/python3
"""aaaaa"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None
    clasesitas = ['BaseModel']

    def do_quit(self, arg):

        return True

    def do_EOF(self, arg):

        return True

    def do_create(self, arg):
        
        comandito = self.parseline(arg)[0]

        if comandito == None:
            print("** class name missing **")
        elif comandito not in self.clasesitas:
            print("** class doesn't exist **")
        else:
            cosita = eval(comandito)()
            cosita.save()
            print(cosita.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
