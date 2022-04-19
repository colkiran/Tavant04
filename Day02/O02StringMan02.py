
player = "emp001, Mike Tyson, 53, boxing, 65 knockout, usa"
print(f"player :{player}")

# convert a string into a list
plr_details = player.split(", ")
print(f"plr_details :{plr_details}")
print(type(plr_details))
print(f"Name :{plr_details[1]}")

# convert a list into a string
res = ", ".join(plr_details)
print(f"res :{res}")
print(type(res))

print("replace".center(40, "-"))
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = st.replace("the", 'The')
print(f"res :{res}")

res = st.replace("the", 'The', 1)
print(f"res :{res}")

res = st.replace("fox", 'wolf')
print(f"res :{res}")

print("find".center(40, "-"))
st = "the quick brown fox jumps over the lazy dog"

res = st.find("fox")
print(f"res :{res}")

res = st.find("the")
print(f"res :{res}")

res = st.find("the", 5)
print(f"res :{res}")

# maketrans, translate
print("maketrans".center(40, "-"))
st = 'hello world'
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("Translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print("strip".center(40, "-"))
st = "********Hello*********"
print(f"st :{st}")

rst = st.rstrip("*")
print(f"rst :{rst}")
lst = st.lstrip("*")
print(f"lst :{lst}")
bst = st.strip("*")
print(f"bst :{bst}")
