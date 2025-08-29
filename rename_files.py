import os

folder_path = r'C:\Users\vbath\OneDrive\Desktop\Python Projects\Folder_Rename_Automation\DummyFolder'
for count, filename in enumerate(os.listdir(folder_path)):
    dst = f'renamed_{count}{os.path.splitext(filename)}'
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, dst)
    os.rename(src, dst)
