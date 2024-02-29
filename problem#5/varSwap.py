def swap_values(user_val1, user_val2, user_val3, user_val4):   
   place_holder = 0
   place_holder = user_val1
   user_val1 = user_val2
   user_val2 = place_holder

   place_holder = user_val3
   user_val3 = user_val4
   user_val4 = place_holder
   out_list = [user_val1, user_val2, user_val3, user_val4]
   return out_list

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   print(str(swap_values(user_input1, user_input2, user_input3, user_input4)[0])+' '+str(swap_values(user_input1, user_input2, user_input3, user_input4)[1])+' '+str(swap_values(user_input1, user_input2, user_input3, user_input4)[2])+' '+str(swap_values(user_input1, user_input2, user_input3, user_input4)[3]))

 