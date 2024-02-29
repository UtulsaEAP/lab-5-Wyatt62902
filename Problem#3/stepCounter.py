def feet_to_steps(user_feet):
   user_steps = user_feet //2.5
   return user_steps

if __name__ == '__main__':
    user_feet = float(input())
    print(int(feet_to_steps(user_feet)))
    
'''
Name: Wyatt Fulton
Lab Time: Thur 2:00PM
'''