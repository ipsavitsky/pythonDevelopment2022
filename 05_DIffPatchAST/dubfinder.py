from sys import argv
import itertools
import importlib
import inspect
import ast
import textwrap
import difflib

def get_subnames(obj, prefix):
    res = []
    names = inspect.getmembers(obj)
    names = map(lambda x: (prefix + '.' + x[0], x[1]), names)
    names, to_filter = itertools.tee(names)
    objects = filter(lambda x: inspect.isclass(x[1]), names)
    for cur_object in objects:
        if cur_object[0].rsplit('.', 1)[1].startswith('__'):
            continue
        res += get_subnames(cur_object[1], cur_object[0])
    # print(list(to_filter))
    res += list(filter(lambda x: inspect.ismethod(x[1]) or inspect.isfunction(x[1]), to_filter))
    return res

def make_pills(names):
    name2pill = dict()
    for name, obj in names:
        source_code = inspect.getsource(obj)
        source_code = textwrap.dedent(source_code)
        ast1 = ast.parse(source_code)

        for node in ast.walk(ast1):
            node.__setattr__('name', '_')
            node.__setattr__('id', '_')
            node.__setattr__('arg', '_')
            node.__setattr__('attr', '_')
        name2pill[name] = ast.unparse(ast1)
    return name2pill
 
if __name__ == '__main__':
    names = argv[1:]
    pills = list()
    for name in names:
        i1 = importlib.import_module(name)
        sub_names = get_subnames(i1, name)
        names_dict = make_pills(sub_names)
        pills.append(names_dict)

    all_dicts_melded = sum(map(lambda x: list(x.items()), pills), [])
    for comb in itertools.combinations(all_dicts_melded, 2):
        sources = (comb[0][1], comb[1][1])
        # print(comb[0][0], comb[1][0], difflib.SequenceMatcher(None, *sources).ratio())
        if difflib.SequenceMatcher(None, *sources).ratio() > 0.95:
            print(comb[0][0], comb[1][0])