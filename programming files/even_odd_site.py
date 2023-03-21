'''
Changed i % 2 to i / 2 -- HS

Changed first open to read ('r') instead of write ('w')
'''

# open numbers.html as write
with open("numbers.html", "r") as f:
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    for i in range(1, 50):
        # if i is an even number
        if i / 2 == 0:
            f.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        else:
            f.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    f.write("</table>\n</body>\n</html>")

with open("numbers.html", "r") as f:
    print(f.read())
    
