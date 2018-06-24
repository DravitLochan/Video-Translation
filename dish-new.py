from googletrans import Translator
translator = Translator()

output = open("output.txt","w")
lines = [line.rstrip('\n') for line in open("black.srt", "r")]

for i in range(len(lines)):
    dialog = lines[i]
    if "-->" in dialog:
        output.write(dialog + "\n")
        continue
    if dialog and dialog.isdigit():
        continue
    dialog = dialog.replace("<i>",'')
    dialog = dialog.replace("</i>",'')
    dialog = dialog.replace("</ i>",'')
    try:
        num = int(dialog)
        output.write(dialog + "\n")
        continue
    except:
        result =  translator.translate(dialog, dest='pa').text
        print result 
        result = result + "\n"
        output.write(result.encode('utf-8', 'ignore'))
    

