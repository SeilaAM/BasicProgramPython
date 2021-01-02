import ModuleFile

'''
# ---- Get global variable ---- #
print('Direct access >>>')
print(ModuleFile.module_variable)

imported_variable = ModuleFile.module_variable
print('\nSave to variable >>>')
print(imported_variable)
'''

'''
# ---- Get function ---- #
print('Direct access >>>')
print(ModuleFile.module_function)
ModuleFile.module_function()

imported_function = ModuleFile.module_function
print('\nSave to variable >>>')
print(imported_function)
imported_function()
'''

'''
# ---- Get class ---- #
print('Direct access >>>')
print(ModuleFile.module_class)
direct_built_object = ModuleFile.module_class()
print(direct_built_object)
direct_built_object.class_method()

imported_class = ModuleFile.module_class
print('\nSave to variable >>>')
print(imported_class)
indirect_built_object = imported_class()
print(indirect_built_object)
indirect_built_object.class_method()
'''

'''
# ---- Get local variable ---- #
#print(ModuleFile.in_function_variable)
#print(ModuleFile.in_class_variable_1)
#print(ModuleFile.in_class_variable_2)
'''

'''
import math
print('Objects from math module:')
print(dir(math))
'''

names_in_module = dir(ModuleFile)
print(names_in_module)

print('\n')
print('A list of names in module:')

for name in names_in_module:
    print(name)

print('\n')
print('Module.__name__ = ' + ModuleFile.__name__)
print('Module.__file__ = ' + ModuleFile.__file__)





