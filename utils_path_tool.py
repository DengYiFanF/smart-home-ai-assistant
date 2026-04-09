import os
# def get_project_root():
#     '''获取工程所在的根目录'''
#     #当前文件的绝对路径
#     current_file = os.path.abspath(__file__)
#     # 获取文件所在的文件夹的绝对路径
#     current_dir = os.path.dirname(current_file)
#     # 再获取工程目录
#     project_root = os.path.dirname(current_dir)
#
#     return project_root
#
#
# def get_abs_path(relative_path:str):
#     project_root = get_project_root()
#     return os.path.join(project_root,relative_path)




def get_project_root():
    '''获取工程所在的根目录'''
    return os.path.dirname(os.path.abspath(__file__))

def get_abs_path(relative_path: str):
    project_root = get_project_root()
    return os.path.join(project_root, relative_path)











