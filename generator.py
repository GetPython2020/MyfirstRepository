#generator:not hold all results, so almost not occupy memory space, high performance.running time is short too
def square_number(nums):
    for i in nums:
        yield (i*i)  #yield makes the function a generator,no return value

my_nums = square_number([1,2,3,4,5])

print(my_nums) #won't print out anything

#generators don't hold entir results in memory, it yields one result at a time
#to call the results, use next

print next(my_nums) #1

print next(my_nums) #4

print next(my_nums) #9

print next(my_nums) #16

print next(my_nums) #25

#use for loop to get all results
for num in my_nums:
    print num
#############################################################
# use list comprehension, this is not a generator
my_num = [x*x for x in [1,2,3,4,5]]

#can print the results

print(my_nums)

#or use for loop to get all results
for num in my_nums:
    print num

#############################################################
# change [] to (), get a generator
my_num = [x*x for x in [1,2,3,4,5]]

#can not print the results

print(my_nums) #show object location
print list(my_nums) #can show all results in a list, but lose the advantage of generator, since oppupy large memory space, run slow

#use for loop to get all results
for num in my_nums:
    print num
