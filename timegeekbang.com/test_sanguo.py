
#读取人物名称
try:
    namefile = open('name.txt')
    data = namefile.read()
    names = data.split('|')
    print(names)
except Exception as e:
    print(e)
finally:
    namefile.close()

nameCount = {}
weaponCount = {}
# for name in names:
#     nameCount[name] = 0
# print(nameCount)

# 读取武器内容
weapons = []
try:
    weaponfile = open('weapon.txt')
    for each_line in weaponfile:
        # print(each_line)
        if each_line != '\n':
            weapons.append(each_line.replace('\n',''))
    print(weapons)
except Exception as e:
    print(e)
finally:
    weaponfile.close()

# 读取三国演义内容
try:
    sanguoFile = open('sanguo.txt',encoding='GB18030')
    data2 = sanguoFile.read().replace('\n','')
    # print("data2 is %s" %data2)
except Exception as e:
    print(e)
finally:
    sanguoFile.close()

for name in names:
    nameCount[name] = data2.count(name)
print(nameCount)

for weapon in weapons:
    weaponCount[weapon] = data2.count(weapon)
print(weaponCount)

def func(filename):
    print(open(filename).read())
    print('test func')

func('name.txt')