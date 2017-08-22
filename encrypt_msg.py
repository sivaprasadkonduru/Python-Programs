"""Spongebob and Patrick have devised a way of encrypting messages. They first decide secretly on the number of columns 
and write the message (letters only) down the columns, padding with extra random letters so as to make a rectangular 
array of letters. For example, if the message is “There’s no place like home on a snowy night” and there are five 
columns, Spongebob would write down

t o i o y
h p k n n
e l e a i
r a h s g
e c o n h
s e m o t
n l e w x

Note that Spongebob includes only letters and writes them all in lower case. 
In this example, Spongebob used the character ‘x’ to pad the message out to make a rectangle, 
although he could have used any letter. Spongebob then sends the message to Patrick by writing the letters in each row, 
alternating left-to-right and right-to-left. So, the above would be encrypted as

toioynnkpheleaigshareconhtomesnlewx

Your job is to recover for Patrick the original message (along with any extra padding letters) from the encrypted one.

Case 1 Input:
col_num = 5
encrypted_text = toioynnkpheleaigshareconhtomesnlewx
Output
theresnoplacelikehomeonasnowynightx

Case 2 Input:
col_num = 3
encrypted_text = ttyohhieneesiaabss

Output:
thisistheeasyoneab"""



def decode_text(col, encrypt_msg=None):

    if encrypt_msg is None:
        return "Please provide encrypt message"
    else:
        data = len(encrypt_msg) % col
        if data != 0:
            encrypt_msg = encrypt_msg + (col-data) * 'x'
        else:
            encrypt_msg = encrypt_msg
        rows = int(len(encrypt_msg) / col)
        val = []
        start = 0
        for i in range(1, rows+1):
            if i % 2 == 0:
                val.append(encrypt_msg[start:col*i][::-1])
            else:
                val.append(encrypt_msg[start:col * i])
            start = start + col
        out = "".join([j[i] for i in range(len(val)) for j in val if i < len(j)])
        return out

x = decode_text(5, "toioynnkpheleaigshareconhtomesnlew")
print(x)  # theresnoplacelikehomeonasnowynightx
y = decode_text(3, "ttyohhieneesiaabss")  # thisistheeasyoneab
print(y)