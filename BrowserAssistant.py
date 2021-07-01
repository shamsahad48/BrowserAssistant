import webbrowser as wb
print("-----------Welcome to your Browser Assistant---------------")

dict={}

dict['Google']='https://google.com'
dict['Youtube'] = 'http://www.youtube.com'

print(dict)

for i in dict.keys():
    print("Opening:" + i)
    wb.open(dict[i],new=2)
