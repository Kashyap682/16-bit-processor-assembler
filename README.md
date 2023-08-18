# 16-bit-processor-assembler
In this project the 16-bit processor assembler is implemented using python. In that user can simply write the instructions in the GUI window and the output will be generated and showed to the user through GUI window. Also, user can open the prewritten txt file in instruction window and edit and save it. Project is carried out through two processes. First one is to convert instructions into machine code and second one is to perform the operations.

Total number of instructions: 16 \
Total number of registers: 12 ( general purpose = 8 )

## Instructions 

| Instruction | Opcode |
| :----: | :-----: |
| ADD | 0000 |
| SUB | 0001 |
| MUL | 0010 |
| DIV | 0011 |
| LUI | 0100 |
| LW | 0101|
| SW | 0110 |
| AND | 0111 |
| OR | 1000|
| XOR | 1001 |
| NOT | 1010 |
| SL | 1011 |
| SR | 1100 |
| SLT | 1101 |
| BEQ | 1110|
| JMP | 1111 |

## Registers 
| Register | Reg Code |
| :---: | :---: |
$zero | 0000 |
$pc | 0001 |
$high | 0010 |
$low | 0011 |
$r0 | 0100 |
$r1 | 0101 |
$r2 | 0110 |
$r3 | 0111 |
$r4 | 1000 |
$r5 | 1001 |
$r6 | 1010 |
$r7 | 1011 |

## Instruction Format

* R Format
* I Format
* J Format

| R Format               ||||
|:---:|:---:|:---:|:---:|
| 4 Bits <br> opcode| 4 Bits <br> rd | 4 Bits <br> rs | 4 Bits <br> rt |

| I Format               |||
|:---:|:---:|:---:|
| 4 Bits <br> opcode| 4 Bits <br> rd | 8-bit immediate value |

| J Format               ||
|:---:|:---:|
| 4 Bits <br> opcode| 12 Bits (Memory word address) | 

## Instruction Types 
1. Arithmetic Instructions 
2. Logical Instructions 
3. Load and Store Instructions 
4. Jump and Branch Instructions 
5. Conditional Instructions

## Screenshots

<a href="https://imgur.com/i86tsdD"><img width=290px src="https://i.imgur.com/i86tsdD.jpg" title="source: imgur.com" /></a> \
<a href="https://imgur.com/UlYEvIX"><img width=290px src="https://i.imgur.com/UlYEvIX.jpg" title="source: imgur.com" /></a>
