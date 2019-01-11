def getDelta():
    state = getReed_State()
    
    if state ==1:
        tijd_begin = getTime()
    if state ==0:
        tijd_eind = getTime()
    delta_tijd = tijd_eind-tijd_begin
    
    return(delta_tijd)
