from read_data import read_data

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    n=0
    for i in data['messages']:
        if i['id']==users_id:
            n+=1
    return n

data=read_data('data/result.json')
print(find_user_message_count(data,-999814828),)