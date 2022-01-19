# folder_struct = {
#     'my_proj': [
#         {
#             'settings': [{'__init__.py', 'dev.py', 'prod.py'}],
#             'mainapp': [{'__init__.py', 'models.py', 'views.py', 'templates'}],
#             'adminapp': [],
#             'authapp': [{'__init__.py', 'models.py', 'views.py', 'templates'}}]




import os
import shutil

folder = r'C:\Users\diman\PycharmProjects\helloworld\code\new_f\home_worck\my_proj'

files = [os.path.relpath(os.path.join(root, file), folder) for root, _, files in os.walk(

    folder) for file in files if file.endswith(".html")]

for rel_path in files:

    path, file = os.path.split(rel_path)

    test_path = os.path.join(folder, "template", path)

    if not os.path.exists(test_path):

        os.makedirs(test_path)

    shutil.copyfile(os.path.join(folder,rel_path), os.path.join(test_path, file))
