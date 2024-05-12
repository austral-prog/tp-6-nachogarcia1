

def remove_elements(list_to_remove_elements):
    cant = len(list_to_remove_elements)
    if cant >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif cant < 6 and cant >= 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif cant < 5 and cant > 0:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif cant == 0:
        return list_to_remove_elements




def add_elements(list_to_add_elements):

    list_to_add_elements.append('Yellow') 
    list_to_add_elements.insert( 0,"Pink")
   

    return list_to_add_elements


def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False
    


def check_lists(list_to_compare1, list_to_compare2):
    list3 = len(list_to_compare1)
    list4 = len(list_to_compare2) 

    if list3 >= 3 and list4 >=3:
        return list_to_compare1 [2] == list_to_compare2 [2]
    else: 
        return False
 


def list_of_lists(list_of_lists_to_modify):

    if len(list_of_lists_to_modify[0]) >= 2:
        list_1 = list_of_lists_to_modify[0][:2]
    else:
        list_1 = list_of_lists_to_modify[0][:]

    if len(list_of_lists_to_modify[1]) >= 4:
        list_2 = list_of_lists_to_modify[1][1: 4]
    else:
        list_2 = list_of_lists_to_modify[1][1:]

    if len(list_of_lists_to_modify[2]) >= 2:
        list_3 = list_of_lists_to_modify[2][-2:]
    else:
        list_3 = list_of_lists_to_modify[2][:]

    list_of_lists_to_modify[0] = list_1
    list_of_lists_to_modify[1] = list_2
    list_of_lists_to_modify[2] = list_3

    return [list_1,list_2,list_3]
