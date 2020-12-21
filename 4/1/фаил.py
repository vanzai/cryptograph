import hashlib
X =input("Введите любое сообщение: ")

hash_object = hashlib.md5(X.encode())
print(hash_object.hexdigest())
f = input()