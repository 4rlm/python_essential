##Note: Sample runner script to import 'ajb_modules.py'
####################################

##Run Script: python3 ajb_module_prac.py
## == OR ==
##Import to CLI step 1: $ python3
##Import to CLI step 2: >>> import ajb_module_prac
####################################

## == Import Module ==
import pdb                            ## Import Debugger
# pdb.set_trace()                     ## Debug: pause

# import ajb_modules                # Import module
import ajb_modules as ajb_mods      # Rename module
# from ajb_modules import person1     # Selectively import
# print (person1["age"])              # Access w/out ref module name
####################################


## == Access Module ==
# pdb.set_trace()                     ## Debug: pause
var_meth_list = dir(ajb_mods)       ## Get vars & meths list
print(var_meth_list)                ## Print vars & meths list

ajb_mods.greeting("Jonathan")       ## Call greeting() function
age = ajb_mods.person1["age"]       ## Access person1 dictionary
print(age)                          ## Print age

person_dict = ajb_mods.make_person_dict()    # Call make_person_dict() & save to var
print(person_dict)

person_dict = ajb_mods.update_person_dict(person_dict, "Adam", 42, "Austin")
print(person_dict)
pdb.set_trace()                     ## Debug: pause
####################################


## == Built-in Modules ==
import platform                     ## Import Platform Module
syst = platform.system()            ## Save system() to var
print(syst)                         ## Print syst
plat_dir = dir(platform)            ## Get vars & meths list
print(plat_dir)                     ## Print vars & meths list
####################################
