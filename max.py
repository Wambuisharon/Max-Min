def find_max_min(list):

  
  if all(num == list[0] for num in list) == True:

   
    new_list.append(len(list))
    return new_list
  else:

   
    maxx = max(list)
    
    
    minn = min(list)

    list2 = []
    
    list2.append(minn)
    list2.append(maxx)
    
    return list2