morse_dict = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F",  "--.":"G",  "....":"H", "..":"I", ".---":"J",
                   "-.-":"K", ".-..":"L","--":"M","-.":"N","---":"O", ".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T",
                   "..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z", ".----":"1", "..---":"2", "...--":"3",
                   "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0", ".-.-.-":"Stop",
                   "--..--":",","..--..":"?"}

encoded_str = "-.-. .-. -.-- .--. - .- -. .- .-.. -.-- ... .. ..."

temp_str = ""
decoded_str = ""
for i in range(len(encoded_str)):
    if(encoded_str[i]==' '):
        decoded_str+= morse_dict[temp_str]
        temp_str = ""
    else:
        temp_str+=encoded_str[i]
decoded_str+= morse_dict[temp_str]

        
    
print(decoded_str)    


key = [["C", "R", "Y", "P", "T"],
["A", "N", "L", "S", "I"],
["B", "D", "E", "F", "G"],
["H", "K", "M", "O", "Q"],
["U", "V", "W", "X", "Z"]]



cipher_text = 'DF ULYP XO CQD LFWC RUBHEDY, CQDYG LN XDYL EGIYIG LMP CQDYF.LYFNH HXPZ CQF YNILXKPB "NDCB_AN_BBHCN" PQ FQ CQPKZBK. OLC PMCUNUG YMB IPYDIDCQ OXY CMB LDZP AULHDFY. CX OALG RMB FWGI PMXBNTIP ZLSWS LFWFE PQ ZCYGY KIBAT XMNKI PMBYD.'

def get_pos(char):
    for i in range(len(key)):
        for j in range(len(key[0])):
            if(char == key[i][j]):
                return (i,j)
    return (-1,-1)

char1 = ''
char2 = ''
plain_text = ''
flag = 0
flagchar = ''
for i in range(len(cipher_text)):
    if(cipher_text[i].isalpha()):
        if(char1==''):
            char1 = cipher_text[i]
        elif(char2==''):
            char2 = cipher_text[i]
            pos_tuple1 = get_pos(char1)
            pos_tuple2 = get_pos(char2)
           # print('char1 char2',char1,char2,pos_tuple1, pos_tuple2)
            if(pos_tuple1[0] == pos_tuple2[0]):
                plain_text+= key[pos_tuple1[0]][(pos_tuple1[1]-1)%5]
                if(flag==1):
                    plain_text+=flagchar
                    flag = 0
                plain_text+= key[pos_tuple2[0]][(pos_tuple2[1]-1)%5]
            elif(pos_tuple1[1] == pos_tuple2[1]):
                plain_text+= key[(pos_tuple1[0]-1)%5][pos_tuple1[1]]
                if(flag==1):
                    plain_text+=flagchar
                    flag = 0
                plain_text+= key[(pos_tuple2[0]-1)%5][pos_tuple2[1]]
            else:
                plain_text+= key[pos_tuple1[0]][pos_tuple2[1]]
                if(flag==1):
                    plain_text+=flagchar
                    flag = 0
                plain_text+= key[pos_tuple2[0]][pos_tuple1[1]]
            char1 = ''
            char2 = ''
    else:
        if(char1==''):
            plain_text+=cipher_text[i]
        else:
            flag = 1
            flagchar = cipher_text[i]
        
        
        
print(plain_text)
                

                
                
            
            
            
    