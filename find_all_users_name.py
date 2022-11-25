from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    lst=[]
    lst1=[]
    for i in data['messages']:
        if lst.count(i.get('actor_id'))==0 and i.get('actor_id')!=None:
            
            lst.append(i.get('actor_id'))
            lst1.append(i.get('actor'))
    
    return lst1
data=read_data('data/result.json')
print(find_all_users_name(data))
