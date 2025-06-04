import os
import subprocess
from config import path

def hd_create(name):
    handlers_path = os.path.join(path, "handlers")
    handlers_template_path = os.path.join(os.path.dirname(__file__), "handler_template.py")
    new_handler_path = os.path.join(handlers_path, f"{name}.py")
    print("Template:", handlers_template_path)
    print("New file:", new_handler_path)
    # Проверяем, существует ли директория
    if not os.path.exists(handlers_path):
        print("Директория не найдена:", handlers_path)
        return
    # Проверяем, существует ли шаблон
    if not os.path.exists(handlers_template_path):
        print("Шаблон не найден:", handlers_template_path)
        return
    result = subprocess.run(
        f"cp '{handlers_template_path}' '{new_handler_path}'",
        shell=True, capture_output=True, text=True
    )
    if result.returncode != 0:
        print("Ошибка:", result.stderr)
    else:
        print("Файл создан успешно")
    return result.stdout

