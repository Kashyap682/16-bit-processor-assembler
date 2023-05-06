def d2b(decNum):
    return bin(decNum)[2:]

def l2S(s):
	str1 = " "
	return (str1.join(s))

def b2d(n):
    return int(n,2)
#--------------------------------------------------------

instructions = {}
ISA_file = open('D:/16-bit processor/ISA.txt','r')
ISA = ISA_file.readlines()
for i in range(0,len(ISA),2):
    instructions[ISA[i].strip('\n')] = ISA[i+1].strip('\n')
print(instructions)

registers = {}
register_file = open('D:/16-bit processor/registers.txt','r')
registers1 = register_file.readlines()
for i in range(0,len(registers1),2):
    registers[registers1[i+1].strip('\n')] = registers1[i].strip('\n')
print(registers)


myFile1 = []
myLb = []
myOutFile = open('D:/16-bit processor/out.txt','r')
myLabelFile = open('D:/16-bit processor/label.txt','r')

myOut = myOutFile.readlines()
myLOut = myLabelFile.readlines()

for ii in myOut:
    myFile1.append(ii.strip('\n'))
print(myFile1)

for iii in myLOut:
    myLb.append(iii.strip('\n'))
print(myLb)

#--------------------------------------------------------

regout = {'$zero': 0, '$pc': 0, '$high': 0, '$low': 0, '$r0': 11, '$r1': 1, '$r2': 1, '$r3': 0, '$r4': 0, '$r5': 0, '$r6': 0, '$r7': 0}
flags = {'overflow': 0, 'carry': 0, 'parity': 0}
pc = 0

memory = {}
for i in range(0,129,2):
    memory[hex(i)] = d2b(0).zfill(16)

#--------------------------------------------------------

def add(dest,opr1,opr2):
    a = regout[registers[str(b2d(opr1))]]
    b = regout[registers[str(b2d(opr2))]]
    
    result = a + b
    
    regout[registers[str(b2d(dest))]] = result

    flags['carry'] = 0
    if result > 65535:
        flags['carry'] = 1

    flags['overflow'] = 0
    if result < -32768 or result > 32767:
        flags['overflow'] = 1

    flags['parity'] = int(bin(result).count('1') % 2 == 0)

def sub(dest,opr1,opr2):
    a = regout[registers[str(b2d(opr1))]]
    b = regout[registers[str(b2d(opr2))]]

    result = a - b
    regout[registers[str(b2d(dest))]] = result

    flags['carry'] = 0
    if b > a:
        flags['carry'] = 1

    flags['overflow'] = 0
    if result < -32768 or result > 32767:
        flags['overflow'] = 1

    flags['parity'] = int(bin(result).count('1') % 2 == 0)


def mul(opr1,opr2):
    mul1 = (regout[registers[str(b2d(opr1))]] * regout[registers[str(b2d(opr2))]])
    mul1b = d2b(mul1).zfill(32)
    mu = mul1b[0:16]
    ml = mul1b[16:33]
    regout['$high'] = b2d(mu)
    regout['$low'] = b2d(ml)
    

def div(opr1,opr2):
    div1 = int(regout[registers[str(b2d(opr1))]] / regout[registers[str(b2d(opr2))]])
    div1b = d2b(div1).zfill(32)
    du = div1b[0:16]
    dl = div1b[16:33]
    regout['$high'] = b2d(du)
    regout['$low'] = b2d(dl)

def lw(dest,opr1,opr2):
    addr = (regout[registers[str(b2d(opr1))]] + regout[registers[str(b2d(opr2))]])
    regout[registers[str(b2d(dest))]] = b2d(memory[hex(addr)])

def sw(dest,opr1,opr2):
    val = regout[registers[str(b2d(dest))]]
    addr = regout[registers[str(b2d(opr1))]] + regout[registers[str(b2d(opr2))]]
    memory[hex(addr)] = d2b(val)

def and1(dest,opr1,opr2):
    and1 = regout[registers[str(b2d(opr1))]] & regout[registers[str(b2d(opr2))]]
    regout[registers[str(b2d(dest))]] = and1

def or1(dest,opr1,opr2):
    or1 = regout[registers[str(b2d(opr1))]] | regout[registers[str(b2d(opr2))]]
    regout[registers[str(b2d(dest))]] = or1

def xor1(dest,opr1,opr2):
    xor1 = regout[registers[str(b2d(opr1))]] ^ regout[registers[str(b2d(opr2))]]
    regout[registers[str(b2d(dest))]] = xor1

def not1(dest,opr1):
    not1 = ~(regout[registers[str(b2d(opr1))]])
    regout[registers[str(b2d(dest))]] = not1

def sl(dest,opr1,opr2):
    sl1 = regout[registers[str(b2d(opr1))]]<< regout[registers[str(b2d(opr2))]]
    regout[registers[str(b2d(dest))]] = sl1

def sr(dest,opr1,opr2):
    sr1 = regout[registers[str(b2d(opr1))]] >> regout[registers[str(b2d(opr2))]]
    regout[registers[str(b2d(dest))]] = sr1

def slt(dest,opr1,opr2):
    if regout[registers[str(b2d(opr1))]] < regout[registers[str(b2d(opr2))]]:
    	regout[registers[str(b2d(dest))]] = 1
    else:
    	regout[registers[str(b2d(dest))]] = 0

def beq(dest,opr1,opr2,pc):
    if regout[registers[str(b2d(dest))]] == regout[registers[str(b2d(opr1))]]:
        pc = myLb[b2d(opr2)]
        print(pc)
        return pc
    else:
        pc = pc + 1
        return pc
    
def jmp(dest):
    pc = myLb[b2d(dest)]
    return pc
       
def lui(dest,opr1):
    regout[registers[str(b2d(dest))]] = b2d((opr1).zfill(8) + '00000000')


opertation = ''

il = int(len(myFile1))
bi = 0

while bi < il:
    
    print(bi)
    op = myFile1[bi][0:4]
    
    for key in instructions:
        if str(b2d(op)) == instructions[key]:
            operation = key
            print(operation)

            if operation == 'add':
                dest = myFile1[bi][4:8]
                print(dest)
                opr1 = myFile1[bi][8:12]
                print(opr1)
                opr2 = myFile1[bi][12:16]
                print(opr2)
                add(dest,opr1,opr2)
                
                bi = bi + 1
            
            elif operation == 'sub':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                sub(dest,opr1,opr2)
                
                bi = bi + 1
            
            elif operation == 'mul':
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                mul(opr1, opr2)
                
                bi = bi + 1
                
            elif operation == 'div':
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                div(opr1, opr2)
                
                bi = bi + 1
            
            elif operation == 'lui':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:16]
                lui(dest, opr1)
                
                bi = bi + 1
        
            elif operation == 'lw':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                lw(dest,opr1,opr2)
                
                bi = bi + 1
            
            elif operation == 'sw':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                sw(dest,opr1,opr2)
                
                bi = bi + 1
            
            elif operation == 'and':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                and1(dest, opr1, opr2)
                
                bi = bi + 1
                
            elif operation == 'or':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                or1(dest, opr1, opr2)
                
                bi = bi + 1
            
            elif operation == 'xor':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                xor1(dest, opr1, opr2)
                
                bi = bi + 1
            
            elif operation == 'not':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                not1(dest, opr1)
                
                bi = bi + 1
            
            elif operation == 'sl':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                sl(dest,opr1,opr2)
                
                bi = bi + 1
            
            elif operation == 'sr':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                sr(dest,opr1,opr2)
                
                bi = bi + 1
            
            elif operation == 'slt':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                slt(dest, opr1, opr2)
                
                bi = bi + 1
            
            elif operation == 'beq':
                dest = myFile1[bi][4:8]
                opr1 = myFile1[bi][8:12]
                opr2 = myFile1[bi][12:16]
                bi = int(beq(dest, opr1, opr2, bi))
            
            elif operation == 'jmp':
                dest = myFile1[bi][4:16]
                temp = 0
                bi = int(jmp(dest))

regfile = open('D:/16-bit processor/regout.txt','w+')
r = []
for k in regout:
    print(str(k) + ' : ' + str(regout[k]))
    r.append(str(k) + ' : ' + str(regout[k]) + '\n')

r.append('\n')

for k in flags:
    print(str(k) + ' : ' + str(flags[k]))
    r.append(str(k) + ' : ' + str(flags[k]) + '\n')


regfile.writelines(r)
regfile.flush()
regfile.close()

rg = open('D:/16-bit processor/regout.txt','r')
rr = rg.read()
print(rr)

import tkinter as tk
root = tk.Tk()
root.geometry('300x300')
label = tk.Label(root, text=rr)
label.pack()
root.mainloop()

print(memory)