import os

dir_path = 'my_proj'
folder = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(dir_path):
    path_dir = [os.makedirs(os.path.join(dir_path, i)) for i in folder]







# for i in folder:
#     os.makedirs(dir_path+i)
#     os.makedirs(dir_path+folder)

