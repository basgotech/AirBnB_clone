#!/usr/bin/python3
"""
This class provides a console ability.
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json
import shlex
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class inherits from cmd.Cmd and provides a console interface.
    """
    prompt = '(hbnb) '
    coll_mod_class = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        Exits the console.
        """
        return True

    def do_EOF(self, arg):
        """
        Handles EOF signal to exit the console gracefully.
        """
        print("")
        return True
    def do_nothing_at_all(self, arg):
        """
        Placeholder function that does nothing.
        """
        pass

    def emptyline(self):
        """
        Handles empty line input.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a specified class.
        """
        imp_val_arg = shlex.split(arg)

        if not arg:
            print("** class name missing **")
            return
        
        if imp_val_arg[0] not in HBNBCommand.coll_mod_class.keys():
            print("** class doesn't exist **")
            return
        
        inhance_imp_val_arg = HBNBCommand.coll_mod_class[imp_val_arg[0]]()
        inhance_imp_val_arg.save()
        print(inhance_imp_val_arg.id)

    def do_show(self, arg):
        """
        Displays information about a specified instance.
        """
        imp_val_arg = shlex.split(arg)

        if len(imp_val_arg) == 0:
            print("** class name missing **")
            return
        
        if imp_val_arg[0] not in HBNBCommand.coll_mod_class.keys():
            print("** class doesn't exist **")
            return
        
        if len(imp_val_arg) == 1:
            print("** instance id missing **")
            return
        
        storage.reload()
        real_entity_dic = storage.all()
        unique_grap = imp_val_arg[0] + "." + imp_val_arg[1]
        if unique_grap in real_entity_dic:
            obj_instance = str(real_entity_dic[unique_grap])
            print(obj_instance)
        else:
            print("** no instance found **")
    
    def do_all(self, arg):
        """
        Displays all instances of a specified class.
        """
        storage.reload()

        imp_val_arg = shlex.split(arg)
        json_f = []
        real_entity_dic = storage.all()

        if not arg:
            for unique_grap in real_entity_dic:
                json_f.append(str(real_entity_dic[unique_grap]))
            print(json.dumps(json_f))
            return
        
        if imp_val_arg[0] in HBNBCommand.coll_mod_class.keys():
            for unique_grap in real_entity_dic:
                if imp_val_arg[0] in unique_grap:
                    json_f.append(str(real_entity_dic[unique_grap]))
            print(json.dumps(json_f))
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes a specified instance.
        """
        imp_val_arg = shlex.split(arg)
        if len(imp_val_arg) == 0:
            print("** class name missing **")
            return
        
        if imp_val_arg[0] not in HBNBCommand.coll_mod_class.keys():
            print("** class doesn't exist **")
            return
        
        if len(imp_val_arg) <= 1:
            print("** instance id missing **")
            return
        
        storage.reload()
        real_entity_dic = storage.all()
        unique_grap = imp_val_arg[0] + "." + imp_val_arg[1]

        if unique_grap in real_entity_dic:
            del real_entity_dic[unique_grap]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """
        Updates the attributes of a specified instance.
        """
        imp_val_arg = shlex.split(arg)
        storage.reload()
        obj_dict_holdd = storage.all()

        if len(imp_val_arg) == 0:
            print("** class name missing **")
            return
        
        if imp_val_arg[0] not in HBNBCommand.coll_mod_class.keys():
            print("** class doesn't exist **")
            return
        
        if len(imp_val_arg) == 1:
            print("** instance id missing **")
            return
        
        try:
            unique_grapper = imp_val_arg[0] + "." + imp_val_arg[1]
            obj_dict_holdd[unique_grapper]
        except KeyError:
            print("** no instance found **")
            return
        
        if len(imp_val_arg) == 2:
            print("** attribute name missing **")
            return
        
        if len(imp_val_arg) == 3:
            print("** value missing **")
            return
        
        item_object = obj_dict_holdd[unique_grapper]
        if hasattr(item_object, imp_val_arg[2]):
            format_type = type(getattr(item_object, imp_val_arg[2]))
            setattr(item_object, imp_val_arg[2], format_type(imp_val_arg[3]))
        else:
            setattr(item_object, imp_val_arg[2], imp_val_arg[3])
        storage.save()
    
    def default(self, arg):
        """
        Handles default command behavior.
        """
        arg = arg.strip()
        input_data = arg.split(".")

        record_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }

        if len(input_data) != 2:
            cmd.Cmd.default(self, arg)
            return
        
        category_name = input_data[0]
        operation_name = input_data[1].split("(")[0]
        phrase = ""
        if (operation_name == "update" and input_data[1].split("(")[1][-2] == "}"):
            user_data = input_data[1].split("(")[1].split(",", 1)
            user_data[0] = shlex.split(user_data[0])[0]
            phrase = "".join(user_data)[0:-1]
            phrase = category_name + " " + phrase
            self.handle_update(phrase.strip())
            return
        try:
            user_data = input_data[1].split("(")[1].split(",")
            for num in range(len(user_data)):
                if (num != len(user_data) - 1):
                    phrase = phrase + " " + shlex.split(user_data[num])[0]
                else:
                    phrase = phrase + " " + shlex.split(user_data[num][0:-1])[0]
        except IndexError:
            user_data = ""
            phrase = ""
        phrase = category_name + phrase
        if (operation_name in record_dict.keys()):
            record_dict[operation_name](phrase.strip())

    def handle_update(self, arg):
        """
        Handles the update command with a dictionary-style argument.
        """
        mapping = "{" + arg.split("{")[1]
        imp_val_arg = shlex.split(arg)
        storage.reload()
        collection_dict = storage.all()

        if len(imp_val_arg) == 0:
            print("** class name missing **")
            return
        
        if imp_val_arg[0] not in HBNBCommand.coll_mod_class.keys():
            print("** class doesn't exist **")
            return
        
        if len(imp_val_arg) == 1:
            print("** instance id missing **")
            return
        try:
            unique_ent = imp_val_arg[0] + "." + imp_val_arg[1]
            collection_dict[unique_ent]
        except KeyError:
            print("** no instance found **")
            return
        
        if (mapping == "{"):
            print("** attribute name missing **")
            return

        mapping = mapping.replace("\'", "\"")
        mapping = json.loads(mapping)
        object_instance = collection_dict[unique_ent]
        for lookup_key in mapping:
            if hasattr(object_instance, lookup_key):
                gp = type(getattr(object_instance, lookup_key))
                setattr(object_instance, lookup_key, mapping[lookup_key])
            else:
                setattr(object_instance, lookup_key, mapping[lookup_key])
        storage.save()

    def do_count(self, arg):
        """
        Counts the number of instances of a specified class.
        """
        iteration_counter = 0
        collection_dict = storage.all()

        for lookup_key in collection_dict:
            if (arg in lookup_key):
                iteration_counter += 1
        print(iteration_counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
