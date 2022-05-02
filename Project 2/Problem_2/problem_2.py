import os

def find_files(suffix, path):

    if not os.path.isdir(path):
        return 'Invalid Directory'
         
    paths = os.listdir(path)
    outputs = []
    
    for item in paths:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            outputs += find_files(suffix,item_path)
        if os.path.isfile(item_path) and item_path.endswith(suffix):
            outputs.append(item_path)
            
    return outputs

# Solution
print('All the files in the directory ending with ".c"')
print(find_files('.c', 'testdir'))
print('\n')

print('All the files in the directory')
print(find_files('', 'testdir'))
print('\n')

print('Checking for non-existing extension')
print(find_files('.k', 'testdir'))
print('\n')

print('Checking for non-existing directory')
print(find_files('.c', 'doxa'))
print('\n')

print('Printing files with ".c" extension in an empty directory')
print(find_files('.c', 'emptydir'))