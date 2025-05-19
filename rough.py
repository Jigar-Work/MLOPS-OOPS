from OOPS_PROJ import facebook

### Encapsulation is a way of restricting access to certain details of an object.
# user1 = facebook()
#Encapsulated variables are only accesible through this method of _classname__attribute.
# print(user1._facebook__username)



# user1 = facebook()
# print(user1.id)

# user2 = facebook()
# print(user2.id)




# user1 = facebook()
# print(user1.id)

# # We can use static method directly through the class.method rather than obj
# facebook.set_id(10)
# user2 = facebook()
# print(user2.id)

# user3 = facebook()
# print(user3.id)


user1 = facebook()
print(facebook._user_id)
print(user1.id)
