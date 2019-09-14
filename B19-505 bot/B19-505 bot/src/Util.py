def get_user_id(api, link):
    id = link
    if 'vk.com/' in link: 
        id = link.split('/')[-1]  
    if not id.replace('id', '').isdigit(): 
        id = api.utils.resolveScreenName(screen_name=id)['object_id'] 
    else:
        id = id.replace('id', '')

    return int(id)

def get_attachs(attachments):
    formatted = []
    for attach in attachments:
        type = attach['type']
        owner_id = attach[type]['owner_id']
        id = attach[type]['id']
        access_key = ''
        if 'access_key' in attach[type]:
            access_key = '_' + attach[type]['access_key']

        # <type><owner_id>_<access_token>
        formatted.append(type + str(owner_id) + '_' + str(id) + str(access_key))

    return formatted
