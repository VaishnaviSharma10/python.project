s = input("enter your email")
print(s.index("@"))
print(s.index("."))
print("Username:" + s[:s.index("@"):])
print("Componey Name:" + s[s.index("@")+1 :s.index("."):])
