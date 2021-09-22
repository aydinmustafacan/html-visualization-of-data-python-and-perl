import sys
import csv

file_name = sys.argv[1]

array_of_data = []
set_to_count_num_of_devices = set()
list_from_entry_to_temperature = []
dict = {}
max_temperature = 0
num_of_card = 0  # equals to length of resulting list
hottest_card_or_device = ""
list_of_output_table = []

with open(file_name) as file:
    csv_reader_object = csv.reader(file)
    for row in csv_reader_object:
        if row[0] == "Device;Card;Temperature":
            print(" ")
        else:
            list_of_each_row = row[0].split(";")
            # max temperature check
            if max_temperature < int(list_of_each_row[2]):  # assumme temperature is integer
                max_temperature = int(list_of_each_row[2])
                hottest_card_or_device = list_of_each_row[1] + "/" + list_of_each_row[0]

            array_of_data.append(list_of_each_row)
            if list_of_each_row[0] in set_to_count_num_of_devices:
                temp_list = dict[list_of_each_row[0]]
                temp_list[0] = temp_list[0] + 1
                if int(list_of_each_row[2]) >= 70:
                    temp_list[1] = temp_list[1] + 1
                if temp_list[2] < int(list_of_each_row[2]):
                    temp_list[2] = int(list_of_each_row[2])

                temp_list[3] = temp_list[3] + int(list_of_each_row[2])  # average temp
                dict[list_of_each_row[0]] = temp_list
            else:
                set_to_count_num_of_devices.add(list_of_each_row[0])
                temp_list = [1]
                if int(list_of_each_row[2]) >= 70:
                    temp_list.append(1)
                else:
                    temp_list.append(0)
                temp_list.append(int(list_of_each_row[2]))  # max temp
                temp_list.append(int(list_of_each_row[2]))  # average
                dict[list_of_each_row[0]] = temp_list

for i in dict:
    avg_temp = dict[i][3] // dict[i][0]
    temp_list = dict[i]
    temp_list[3] = avg_temp
    dict[i] = temp_list

# FInd total devices, total cards , max card temperature, hottest card/device
num_of_devices = len(set_to_count_num_of_devices)
num_of_card = len(array_of_data)


analytics_list = [str(num_of_devices), str(num_of_card), str(max_temperature), hottest_card_or_device]

mylist = []
for i in dict:
    tmp_ls = [i]
    tmp_ls.extend(dict[i])
    mylist.append(tmp_ls)


output_name_ls = file_name.split(".")
output_file = output_name_ls[0]+".html"
f = open(output_file, 'w')



def html_table(lol, analytics_list_for_html_creation):
    f.write("<font size=\"+7\">Summary</font>")
    f.write("<table border=\"1\" class=\"dataframe\" style=\"border:2px solid black;\">")
    f.write("<tr>")
    f.write("<th>")
    f.write("Total Devices")
    f.write("</th>")
    f.write("<td>")
    f.write(analytics_list_for_html_creation[0])
    f.write("</td>")
    f.write("</tr>")
    f.write("<tr>")
    f.write("<th>")
    f.write("Total Cards")
    f.write("</th>")
    f.write("<td>")
    f.write(analytics_list_for_html_creation[1])
    f.write("</td>")
    f.write("</tr>")
    f.write("<tr>")
    f.write("<th>")
    f.write("Max Card Temperature")
    f.write("</th>")
    f.write("<td>")
    f.write(analytics_list_for_html_creation[2])
    f.write("</td>")
    f.write("</tr>")
    f.write("<tr>")
    f.write("<th>")
    f.write("Hottest Card/Device")
    f.write("</th>")
    f.write("<td>")
    f.write(analytics_list_for_html_creation[3])
    f.write("</td>")
    f.write("</tr>")
    f.write("</table>")
    f.write("<font size=\"+5\">Devices</font>")
    f.write("<table border=\"1\" class=\"dataframe\">")
    f.write("<tr>")
    f.write("<th>")
    f.write("Device")
    f.write("</th>")
    f.write("<td>")
    f.write("Total # of cards")
    f.write("</td>")
    f.write("<td>")
    f.write("High Temp Cards #")
    f.write("</td>")
    f.write("<td>")
    f.write("Max Temprature")
    f.write("</td>")
    f.write("<td>")
    f.write("Avg. Temprature")
    f.write("</td>")
    f.write("</tr>")
    for i in lol:
        f.write("<tr>")
        f.write("<th>")
        f.write(i[0])
        f.write("</th>")
        f.write("<td>")
        f.write(str(i[1]))
        f.write("</td>")
        f.write("<td>")
        f.write(str(i[2]))
        f.write("</td>")
        f.write("<td>")
        f.write(str(i[3]))
        f.write("</td>")
        f.write("<td>")
        f.write(str(i[4]))
        f.write("</td>")
        f.write("</tr>")
    f.write("</table>")
    f.write("<h>(High Temperature >= 70)</h>")


html_table(mylist, analytics_list)
f.close()
