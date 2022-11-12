import shutil

print("numberを入力")
number = int(input())
new_folder_name = f"./arc_code/ac_{number}"

shutil.copytree("./arc_code/sample", new_folder_name)
