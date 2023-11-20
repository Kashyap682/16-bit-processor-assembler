def d2b(decNum):
    return bin(decNum)[2:]

def l2S(s):
	str1 = ""
	return (str1.join(s))

#--------------------------------------------------------

instructions = []
ISA_file = open('D:/16-bit processor/ISA.txt','r')
ISA = ISA_file.readlines()
for i in range(0,len(ISA),2):
    print(ISA[i].strip('\n'))
    instructions.append(ISA[i].strip('\n'))
    
opcode = []
for i in range(1,len(ISA),2):
    print(ISA[i].strip('\n'))
    opcode.append(d2b(int(ISA[i].strip('\n'))).zfill(4))

registers = []
register_file = open('D:/16-bit processor/registers.txt','r')
registers1 = register_file.readlines()
for i in range(0,len(registers1),2):
    print(registers1[i].strip('\n'))
    registers.append(registers1[i].strip('\n'))

regcode = []
for i in range(1,len(registers1),2):
    print(registers1[i].strip('\n'))
    regcode.append(d2b(int(registers1[i].strip('\n'))).zfill(4))
    
myFile1 = []
myFile = open('D:/16-bit processor/test.txt','r')
myOutFile = open('D:/16-bit processor/out.txt','a')
myLabelFile = open('D:/16-bit processor/label.txt','a+')
myFile_lines = myFile.readlines()
for i in myFile_lines:
    myFile1.append(i.strip('\n'))

#--------------------------------------------

for lb in myFile1:
    print(lb)
    outlb = []
    
    if (lb.endswith(":")):
        outlb.append(lb + '\n')
        outlb.append(str(myFile1.index(lb)) + '\n')
    
    else:
        continue

    print(outlb)
    myLabelFile.writelines(outlb)
    myLabelFile.flush()
    outlb.clear()

myLabelFile.flush()
myLabelFile.close()
#-----------------------------------------------

for i in myFile1:
    outf = []
    inst = i.split(',')
    op = inst[0]

    for j in instructions:
        if op == j:
            outf.append(opcode[instructions.index(j)])
            break
        else:
            continue
    if ((op == 'add') or (op == 'sub') or (op == 'and') or (op == 'or') or (op == 'xor') or (op == 'sl') or (op == 'sr') or (op == 'slt')):
        dest = inst[1]
        opr1 = inst[2]
        opr2 = inst[3]
        for k in registers:
            if dest == k:
                outf.append(regcode[registers.index(k)])
                break
            else:
                continue
    
        for l in registers:
            if opr1 == l:
                outf.append(regcode[registers.index(l)])
                break
            else:
                continue
            
        for m in registers:
            if opr2 == m:
                outf.append(regcode[registers.index(m)])
                break
            else:
                continue
        
        print(outf)
        s = l2S(outf) + '\n'
        print(s)
        myOutFile.writelines(s)
        myOutFile.flush()
        outf.clear()
    
    elif (op == 'mul' or op == 'div'):
        dest = d2b(0).zfill(4)
        opr1 = inst[1]
        opr2 = inst[2]
        
        outf.append(d2b(0).zfill(4))
        
        for l in registers:
            if opr1 == l:
                outf.append(regcode[registers.index(l)])
                break
            else:
                continue
            
        for m in registers:
            if opr2 == m:
                outf.append(regcode[registers.index(m)])
                break
            else:
                continue
        
        print(outf)
        s = l2S(outf) + '\n'
        print(s)
        myOutFile.writelines(s)
        myOutFile.flush()
        outf.clear()
    
    elif (op == 'lui'):
        dest = inst[1]
        opr1 = inst[2]
        
        for k in registers:
            if dest == k:
                outf.append(regcode[registers.index(k)])
                break
            else:
                continue
        
        outf.append(d2b(int(opr1)).zfill(8))
        
        print(outf)
        s = l2S(outf) + '\n'
        print(s)
        myOutFile.writelines(s)
        myOutFile.flush()
        outf.clear()
    
    elif (op == 'lw' or op == 'sw'):
        dest = inst[1]
        opr1 = inst[2]
        opr2 = inst[3]
        
        for k in registers:
            if dest == k:
                outf.append(regcode[registers.index(k)])
                break
            else:
                continue
        
        for l in registers:
            if opr1 == l:
                outf.append(regcode[registers.index(l)])
                break
            else:
                continue
            
        for j in registers:
            if opr2 == j:
                outf.append(regcode[registers.index(j)])
                break
            else:
                continue
        
        print(outf)
        s = l2S(outf) + '\n'
        print(s)
        myOutFile.writelines(s)
        myOutFile.flush()
        outf.clear()
        
    elif (op == 'not'):
        dest = inst[1]
        opr1 = inst[2]
        
        for k in registers:
            if dest == k:
                outf.append(regcode[registers.index(k)])
                break
            else:
                continue
        
        for l in registers:
            if opr1 == l:
                outf.append(regcode[registers.index(l)])
                break
            else:
                continue
        
        outf.append(d2b(0).zfill(4))
        
        print(outf)
        s = l2S(outf) + '\n'
        print(s)
        myOutFile.writelines(s)
        myOutFile.flush()
        outf.clear()
    
    elif (op == 'beq'):
        
        dest = inst[1]
        opr1 = inst[2]
        opr2 = inst[3]
        
        for k in registers:
            if dest == k:
                outf.append(regcode[registers.index(k)])
                break
            else:
                continue
        
        for l in registers:
            if opr1 == l:
                outf.append(regcode[registers.index(l)])
                break
            else:
                continue
        
        myL = []
        myLabelFile1 = open('D:/16-bit processor/label.txt','r')
        myLbl = myLabelFile1.readlines()
        myLabelFile1.close()
        for f in myLbl:
            myL.append(f.strip('\n'))
        print(myLbl)
        print(myL)
        ll = len(myL)
        print(ll)
        
        for li in range(0,ll,2):
            print(myL[li])
            if myL[li].strip(':') == opr2:
                a = li
                b = a + 1
                print(a)
                print(b)
                outf.append(d2b(b).zfill(4))
                break
            else:
                continue
            
        print(outf)
        s = l2S(outf) + '\n'
        print(s)
        myOutFile.writelines(s)
        myOutFile.flush()
        outf.clear()
    
    elif (op == 'jmp'):
        dest = inst[1]
        
        myL1 = []
        myLabelFile11 = open('D:/16-bit processor/label.txt','r')
        myLbl1 = myLabelFile11.readlines()
        myLabelFile11.close()
        for f in myLbl1:
            myL1.append(f.strip('\n'))
        print(myLbl1)
        print(myL1)
        ll1 = len(myL1)
        print(ll1)
        
        for li1 in range(0,ll1,2):
            print(myL1[li1])
            if myL1[li1].strip(':') == dest:
                a = li1
                b = a + 1
                print(a)
                print(b)
                outf.append(d2b(0).zfill(4))
                outf.append(d2b(0).zfill(4))
                outf.append(d2b(b).zfill(4))
                break
            else:
                continue
        
        print(outf)
        s = l2S(outf) + '\n'
        print(s)
        myOutFile.writelines(s)
        myOutFile.flush()
        outf.clear()

myOutFile.flush()
myOutFile.close()
myLabelFile.close()
