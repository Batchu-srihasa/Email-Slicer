# get user email address

email = input("What is your email address?: ").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1 :]

# format message

output1 = "Your username is {} ".format(user)
output2 = "Your domain name is {}".format(domain)

# display output message 

print(output1)
print(output2)
