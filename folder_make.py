import shutil

print("numberを入力")
number = int(input())
new_folder_name = f"./code/ac_{number}"

shutil.copytree("./code/sample", new_folder_name)
