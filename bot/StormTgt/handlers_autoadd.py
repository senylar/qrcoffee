import os
import importlib.util
from config import path, routers_name
from .loging_ import logging

def auto_add_h(dp):
    dir = path + 'handlers/'
    files = os.listdir(dir)[2:]
    print(files)

    for filename in files:
        module_name = os.path.splitext(filename)[0]
        file_path = os.path.join(dir, filename)
        if file_path[-1] == "_":
            continue
        print(file_path, module_name)
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None or spec.loader is None:
            logging.warning(f"Cannot import {file_path}: spec or loader is None.")
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        match getattr(module, routers_name, None):
            case None:
                logging.warning(f"The module {module_name} does not have a '{routers_name}' attribute. If this is a handler, ensure it has a '{routers_name}' defined, or move it to a different directory.")
            case _:
                dp.include_router(module.router)
