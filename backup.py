import shutil,os,datetime,time


source_dir = r"D:\img"
destination_dir = r"D:\copy"

all_file = os.listdir(source_dir)
time = datetime.date.today()


final_path = os.path.join(destination_dir,str(time))
os.makedirs(final_path,exist_ok=True)

for file in all_file:
    source = os.path.join(source_dir,file)
    destination = os.path.join(final_path,file)
    
    try:
        name = shutil.copy2(source,destination)
        print(f'done with name {name}')
    except Exception as e:
        print(f'Error in copy {e}')
