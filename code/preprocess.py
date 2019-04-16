import ast
import symtable


def get_stmts(module):
    lastlineno = None
    for stmt in reversed(module.body):
        if isinstance(stmt, ast.FunctionDef):
            yield (stmt.name, (stmt.lineno-1, (None if lastlineno is None else lastlineno)))
        lastlineno = stmt.lineno - 1


def get_imports(module):
    for stmt in module.body:
        if isinstance(stmt, ast.ImportFrom):
            assert stmt.level == 0
            assert '.' not in stmt.module
            for alias in stmt.names:
                assert alias.asname is None
                yield (alias.name, (stmt.module,alias.name))


def get_child_tables(table):
    return [table]+[ct for t in table.get_children() for ct in get_child_tables(t)]


def parse_module(module_name):
    filename = module_name + ".py"
    with open(filename, 'r') as f:
        source = f.read()

    srclines = source.splitlines()
    module = ast.parse(source, filename)
    table = symtable.symtable(source, filename, "exec")
    stmts = list(get_stmts(module))
    last_fun = stmts[0][0]
    lines = {name:"\n".join(srclines[s:e]).strip() for (name,(s,e)) in stmts}
    imports = dict(get_imports(module))

    def parse_dependencies(name):
        for tab in get_child_tables(table.lookup(name).get_namespace()):
            for g in tab.get_globals():
                if g in dir(__builtins__):
                    continue

                if table.lookup(g).is_imported():
                    imported = imports[g]
                    if imported[0] != "leetcode":
                        yield imported
                else:
                    yield (module_name, g)

    return last_fun, lines, {name:tuple(parse_dependencies(name)) for name in lines}


def get_module(modules, module_name):
    module = modules.get(module_name, None)
    if module is None:
        module = parse_module(module_name)
        modules[module_name] = module
    return module


def get_dependencies(modules, mf):
    return get_module(modules, mf[0])[2][mf[1]]


def get_lines(modules, mf):
    return get_module(modules, mf[0])[1][mf[1]]


def load_functions(module_name):
    modules = {}
    visited = set()

    root = (module_name, get_module(modules, module_name)[0])
    unresolved = [root]

    while unresolved:
        mf = unresolved[0]
        unresolved = unresolved[1:]
        if mf in visited:
            continue
        visited.add(mf)
        unresolved += get_dependencies(modules, mf)

    code = "\n\n".join(get_lines(modules, mf) for mf in visited)
    return root[1], code


def get_function_args(module_name, fun_name):
    filename = module_name + ".py"

    with open(filename, 'r') as f:
        source = f.read()

    module = ast.parse(source, filename)

    for stmt in module.body:
        if not isinstance(stmt, ast.FunctionDef):
            continue

        if stmt.name == fun_name:
            assert stmt.args.vararg is None
            assert stmt.args.kwarg is None
            assert not stmt.args.defaults
            return [arg.arg for arg in stmt.args.args]


SOLUTION = """
class Solution:
    def {name}(self, {args}):
        return {name}({args})
"""

def preprocess(filename):
    if filename.endswith(".py"):
        module_name = filename[:-3]
    else:
        module_name = filename

    fun_name, code = load_functions(module_name)
    args = get_function_args(module_name, fun_name)
    return "\n\n".join(
        [code.strip(),
         SOLUTION.format(name=fun_name, args=", ".join(args)).strip()])


def main():
    import os
    import logging
    from argparse import ArgumentParser

    logging.captureWarnings(True)
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)


    parser = ArgumentParser()
    parser.add_argument("--timestamps", action="store_true", default=False, help="show timestamp on each log line")
    parser.add_argument("--debug", action="store_true", default=False, help="turn on debug logging")
    parser.add_argument("--submit", action="store_true", default=False, help='submit solution')
    parser.add_argument("filename", nargs="*")

    args = parser.parse_args()
    names = args.filename
    if not names:
        names = [
            name
            for name in os.listdir(os.path.dirname(__file__) or '.')
            if name.endswith(".py") and name.split("-",1)[0].isdigit() ]

    if args.timestamps:
        formatter = logging.Formatter(fmt='{asctime} {message}',datefmt='%Y-%m-%d %H:%M:%S', style='{')
        handler.setFormatter(formatter)
    if args.debug:
        logger.setLevel(logging.DEBUG)

    if not args.submit:
        logger.info(name)
        print(preprocess(name))
        return

    from miasma import task
    from wronganswer import Profile
    profile = Profile()
    profile.set_debug(args.debug)

    oj = 'leetcode.com'
    env = 'python3'

    @task(f"submit {filename}")
    async def submit(filename):
        data = preprocess(name).encode()

        token = await profile.submit(oj, pid, env, data)
        status = None
        while status is None:
            status, message, *extra = await profile.status(oj, token)
        assert status, message
        print(message)
        if extra:
            print(extra[0])

    @task(f"submit")
    async def _main():
        for name in names:
            await submit(name)

    _main().run(retry=3)


if __name__ == '__main__':
    main()
