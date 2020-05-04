class Invoice:

    def greeting(self):
        return 'Hi There'


inv_one = Invoice()
print(inv_one.greeting())

inv_two = Invoice()
print(inv_two.greeting())

class Invoice:           # first say class and capitalize the first letter in the name followed by a colon

  def greeting(self):    #classes are object matchers creates a blueprint and contain functions so create a basic function here named greeting pass in default arg self
    return 'Hi there'
                        # to call class use instantiation 

inv_one = Invoice()       # instantiation here 
print(inv_one.greeting()) # to call the greeting is here