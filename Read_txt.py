def main():
    text_list = []
    with open("real_test.TXT", "r") as f:
        for line in f:
            text_list.append(line)

    text_list = text_list[10::]
    counter = 1
    for i in range(0,len(text_list)):
        if "Mess_Datum_Uhrzeit" in text_list[i]:
            temp_list = text_list[i].split()
            
            date_list = temp_list[1].split(".")
            date_list.reverse()
            temp_list[1] = "".join(date_list)

            time_list = str(temp_list[2]).split(":")
            new_time = time_list[0] + time_list[1]
            temp_list[2] = new_time

            fin_item = " ".join(temp_list)
            text_list[i] = fin_item + "\n"

        if "Messwert_CG" in text_list[i]:
            if "Ovr" in text_list[i]:
                text_list[i] = text_list[i].replace("Ovr", "0")
            

        # text_list[i] = text_list[i].replace('"',"")
        print(f"{i} " + f"{text_list[i]}")
        counter += 1
        if counter == 10:
            counter = 1
    

    new_file = open("text_output.LAF", "w")
    new_file.writelines(text_list)

main()
