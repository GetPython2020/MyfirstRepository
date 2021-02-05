#Decorator
#一个函数可以作为另一个函数的参数，返回一个内部函数
#==========================================================
def decorate_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper_function ran')
        return original_function(*args,**kwargs)
    return wrapper_function
#===========================================================
def display():
    print('Display function ran')

display = decorate_function(display) #display equals wrapper_function,可以改变名称display
display()#run wrapper_function: wrapper_function ran Display function ran

#===========================================================
#另一种写法:
@decorate_function
def display():
    print('Display function ran')

display() #run wrapper_function: wrapper_function ran Display function ran,只能用display

    
