def eliminateParts(name):
    if '"' in name:
        name = name.replace('"','')
        name = name.strip()
        return name
    elif '&' in name:
        print('estoy en el segudno if')
        name = name.replace("&",'')
        name = name.replace("'",'')
        name = name.strip()
        return name
        
    else:
        return name
        