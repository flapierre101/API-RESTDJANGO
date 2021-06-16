import jwt

encoded_token = jwt.encode({'user_id': "abc"}, 'SECRET', algorithm='HS256')

print (encoded_token)

print(jwt.decode(encoded_token, 'SECRET', algorithms=['HS256']))

