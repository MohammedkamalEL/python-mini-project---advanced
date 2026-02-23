import os,shutil,json,sys


# SOURCE = r"D:\projects\py\learn_advance_py\script\data"
# TARGET = r'D:\projects\py\learn_advance_py'


def find_all_game_path(dir):
    # files = os.listdir(dir)
    game_path = []
    for root, dirs, files in os.walk(dir):
        for directres in dirs:
            if 'game' in directres:
                game_path.append(dirs)
            break
    return game_path[0]

def creat_dir(path):
    os.makedirs(path,exist_ok=True)

def remove_name(path):
    new_name=[]
    for i in path:
        if 'game' in i:
            right = i.replace("_game",'')
            new_name.append(right)
    return new_name

def make_json_file(path,game_dir):
    data = {
        "gameName":game_dir,
        "gameLingth":len(game_dir)
    }

    with open(path,'w') as f:
        json.dump(data,f)
    

def copy_and_overright(sour,des):
    if os.path.exists(des):
        shutil.rmtree(des)
    shutil.copytree(sour,des)

def main(source, target):
    cwd = os.getcwd()
    source_dir = os.path.join(cwd,source)
    target_dir = os.path.join(cwd,target)
    # print(source_dir,'-----------',target_dir)
    game_path = find_all_game_path(source_dir)
    name = remove_name(game_path)
    
    for sur,des in zip(game_path,name):
        des_path = os.path.join(target_dir,des)
        sur_path = os.path.join(source_dir,sur)
        copy_and_overright(sur_path,des_path)
        
    json_path = os.path.join(target_dir,f'{target}.json')
    make_json_file(json_path,name)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception('inter source and destenaion file onely ')
    source , target = args[1:]
    main(source,target)


# files = os.listdir(SOURCE)
# os.makedirs(TARGET,exist_ok=True)
# for i in range(len(files)):
#     file_path = os.path.join(f'\\{SOURCE}\\{files[i]}')
#     if "game" in file_path and os.path.isdir(file_path):
#         new_path = file_path.replace('_game','')
#     new_path_trget = os.path.join(f'{TARGET}\\game')
#     shutil.copytree(file_path,new_path_trget)
