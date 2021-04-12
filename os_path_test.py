import os
path="C:\\Users\\carlo\\Documents\\PythonStudy\\os_path_test.py"

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join(os.path.dirname(path),os.path.basename(path)))
print(os.path.split(path),os.path.split(path)[0],os.path.split(path)[1])
print(os.path.getsize(path))

