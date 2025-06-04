# import os
# import importlib.util
#
#
#
# dir = os.path.dirname(__file__)
# files = os.listdir(dir)[2:]
# print(files)
#
# for filename in files:
#     module_name = os.path.splitext(filename)[0]
#     file_path = os.path.join(os.path.dirname(__file__), filename)
#     print(file_path,filename)
#     spec = importlib.util.spec_from_file_location(module_name, file_path)
#     print(spec)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#
#     dp.include_router(module.router)
#     # Теперь можно использовать module