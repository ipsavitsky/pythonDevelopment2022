import readline
import shlex
import cmd
import importlib
from pynames import GENDER, LANGUAGE

class NameGenerator(cmd.Cmd):

    current_language: str = LANGUAGE.NATIVE

    def do_language(self, args):
        match args[0]:
            case 'RU':
                self.current_language = LANGUAGE.RU
            case 'EN':
                self.current_language = LANGUAGE.EN
            case 'NATIVE':
                self.current_language = LANGUAGE.NATIVE

    def do_generate(self, args):
        arguments = shlex.split(args)
        i = importlib.import_module('pynames.generators.'+arguments[0])
        # generator_objects = [s for s in dir(i) if s.endswith('NamesGenerator')]
        match arguments:
            case ['iron_kingdoms', _]:
                generator_object = arguments[1] + 'FullnameGenerator'
                cls = eval(f'i.{generator_object}')()
                print(cls.get_name_simple(language=self.current_language))
            case ['elven', _]:
                generator_object = arguments[1] + 'NamesGenerator'
                cls = eval(f'i.{generator_object}')()
                print(cls.get_name_simple(language=self.current_language))
            case [_, _]:
                generator_object = [s for s in dir(i) if s.endswith('NamesGenerator')][0]
                cls = eval(f'i.{generator_object}')()
                match arguments[1]:
                    case 'male':
                        print(cls.get_name_simple(gender=GENDER.MALE, language=self.current_language))
                    case 'female':
                        print(cls.get_name_simple(gender=GENDER.FEMALE, language=self.current_language))




    def do_info(self, args):
        arguments = shlex.split(args)
        i = importlib.import_module('pynames.generators.'+arguments[0])
        generator_objects = [s for s in dir(i) if s.endswith('NamesGenerator')]
        match arguments:
            case [_, 'language']:
                for object_name in generator_objects:
                    cls = eval(f'i.{object_name}')()
                    print(f'class {object_name} has {cls.languages} languages')
            case [_, _]:
                for object_name in generator_objects:
                    cls = eval(f'i.{object_name}')()
                    match arguments[-1]:
                        case 'male':
                            print(f'class {object_name} has {cls.get_names_number(GENDER.MALE)} male names')
                        case 'female':
                            print(f'class {object_name} has {cls.get_names_number(GENDER.FEMALE)} female names')
            case [_]:
                for object_name in generator_objects:
                    cls = eval(f'i.{object_name}')()
                    print(f'class {object_name} has {cls.get_names_number()} names')



if __name__ == '__main__':
    NameGenerator().cmdloop()