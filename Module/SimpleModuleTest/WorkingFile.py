import ModuleFile

import sys

print(sys.path)

print('Python Paths = ')
for p in sys.path:
    print(p)

# ---- Get global variable ---- #
#print(ModuleFile.global_var)

#imported_global_var = ModuleFile.global_var
#print(imported_global_var)


# ---- Get function ---- #
#ModuleFile.module_fun()

#imported_fun = ModuleFile.module_fun
#imported_fun()


# ---- Get class ---- #
#print(ModuleFile.module_class)

imported_class = ModuleFile.module_class
#print(imported_class)

#a = ModuleFile.module_class()
#print(a)

a = imported_class()
#print(a)

#a.class_method()


# ---- Get local variables ---- #
#in_fun_var = ModuleFile.in_fun_var
#in_class_var = ModuleFile.in_class_var_1
#in_class_var = ModuleFile.in_class_var_2


