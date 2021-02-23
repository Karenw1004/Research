#!/mnt/c/Users/karen/Downloads/anaconda3/bin/python
import json

myDict = {}
with open("output.txt") as f:  
    start_flag = False 
    key_name = ""
    assembly_dict = {}
    key_assembly = ""
    for line in f:
        split_line = line.split()
        if "# {method}" in line:
            key_name=split_line[3]+" "+split_line[4]+" " +split_line[5]+" " +split_line[6]
            start_flag = True
        elif start_flag and ( '[Exception Handler]' in line or '[Stub Code] ' in line ):
            start_flag = False
        elif start_flag and split_line and split_line[0].startswith('0x'):
            assembly_dict.update({split_line[0]: split_line [1:]})
            myDict.update({key_name : assembly_dict })
print(json.dumps(myDict, indent=4 ))

    

# {
#     " 'hashCode' '()I' in 'java/lang/String' "  :  {
#           "0x00007f3381100ce0": ["mov"  ,  "0x8(%rsi),%r10d" ],
#           "0x00007f3381100ce4": ["shl"  ,  "$0x3,%r10"],
#           "0x00007f3381100ce8": ["cmp"  ,  "%rax,%r10 "],
#           "0x00007f3381100ceb": ["jne"  ,  "0x00007f3381045ba0"  ,";"  , "{runtime_call}" ] ,
#           "0x00007f3381100cf1": ["nopw" ,  "0x0(%rax,%rax,1)"],
#           "0x00007f3381100cfc": ["xchg" , "%ax,%ax"  ]
#       }
# }