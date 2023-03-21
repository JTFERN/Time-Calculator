def add_time(start, duration, wday=False):
    #cria lista para time start e am/pm
    tsa=start.split(":")
    apm=tsa[1].split()[1]
    tsa[1]=tsa[1].split()[0]
    tsa=[int(x) for x in tsa]
    
    #cria lista para time duration
    tdu=duration.split(":")
    tdu=[int(x) for x in tdu]
    
    #contas de minutos
    minu=tsa[1]+tdu[1]
    minuover=minu//60
    minu=minu-(60*minuover)
    if minu<10:
        minu="0"+str(minu)
    else: minu=str(minu)
    
    #contas de hora
    hour=tsa[0]+tdu[0]+minuover
    hourover=hour//12
    hour=str(hour-(12*hourover))
    if hour=="0": hour="12"
    
    #contas ampm
    napm=apm
    apmover=hourover%2
    if apmover!=0:
        if apm=="AM": napm="PM"
        else: napm="AM"
        
    #contas day later
    day=""
    if apm=="AM":
        if 2>=hourover>1: day=" (next day)"
        if hourover>2: day=" ({} days later)".format((hourover//2)+1)
    if apm=="PM":
        if 2>=hourover>0: day=" (next day)"
        if hourover>2: day=" ({} days later)".format((hourover//2)+1)
    
    #contas wday
    dayw=""
    week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if wday!=False:
        wday=wday.capitalize()
        pos=week.index(wday)
        if apm=="AM":
            if 2>=hourover>1: pos+=1
            if hourover>2: pos+=((hourover//2)+1)
        if apm=="PM":
            if 2>=hourover>0: pos+=1
            if hourover>2: pos+=((hourover//2)+1)
        dayw=", "+week[pos%7]       
        

    
    return (hour+":"+minu+" "+napm+dayw+day)
