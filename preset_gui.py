import os

srs_root_path = os.path.join("C:\Program Files\DCS-SimpleRadio-Standalone")

uhf1_path = os.path.join(srs_root_path, "ANARC-164_UHF_1.txt")
uhf2_path = os.path.join(srs_root_path, "ANARC-164_UHF_2.txt")
# uhf1_path = os.path.join("ANARC-164_UHF_1.txt")
# uhf2_path = os.path.join("ANARC-164_UHF_2.txt")

class channel:
    name = "Unnamed"
    freq = 243.0

    def print(self):
        return self.name + "|" + str(self.freq)
    
print("= SRS Channel Preset Configurator =")

print("----------------------------")
print("F-15C ANARC-164_UHF_1 Radio:")
channel_num = 1
current_channels = []

done_making_channels = False
while(not done_making_channels):
    channel_name = input(f"C{channel_num} Name: ")
    freq = float(input(f"C{channel_num} Frequency (MHz): "))
    new_channel = channel()
    new_channel.name = channel_name
    new_channel.freq = freq

    done_choice = input("Type y if you're done making channels: ")
    if(done_choice == "y"):
        done_making_channels = True
    
    print("--------------------")

    current_channels.append(new_channel)
    channel_num += 1

f15_radio1 = current_channels

print("----------------------------")
print("F-15C ANARC-164_UHF_2 Radio:")
channel_num = 1
current_channels = []

done_making_channels = False
while(not done_making_channels):
    channel_name = input(f"C{channel_num} Name: ")
    freq = float(input(f"C{channel_num} Frequency (MHz): "))
    new_channel = channel()
    new_channel.name = channel_name
    new_channel.freq = freq

    done_choice = input("Type y if you're done making channels: ")
    if(done_choice == "y"):
        done_making_channels = True

    print("--------------------")

    current_channels.append(new_channel)
    channel_num += 1

f15_radio2 = current_channels



print("Writing to files...")
with open(uhf1_path, "w") as radio1_file:
    for chan in f15_radio1:
        radio1_file.write(chan.print() + "\n")
with open(uhf2_path, "w") as radio2_file:
    for chan in f15_radio2:
        radio2_file.write(chan.print() + "\n")
print("Done")