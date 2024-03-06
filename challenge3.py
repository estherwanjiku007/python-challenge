all_list2=["Esther","Beatrice","BEN","Wanjiku","Mugo"] 
def gives_string(an_int,all_list):  
   new_list=list()  
   for a in all_list:
             
         if len(a)==an_int :
          new_list.append(a.lower())     
          
         else:continue
          
   return new_list
result=gives_string(3,all_list2)
print(result)

        
