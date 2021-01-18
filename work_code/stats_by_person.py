import csv
import datetime
import operator
from datetime import date, timedelta
import os
import sys
#
"""
I prime each analys variable with 1 to avoid the divide by zero error
This will show a mismatch by 1 in total_tickets column  in the the assoc_stats file.
"""
Anne = 1
Anne_Made = 0
Anne_Miss = 0
Anne_SLA = 0

Adrian = 1
Adrian_Made = 0
Adrian_Miss = 0
Adrian_SLA = 0

Al = 1
Al_Made = 0
Al_Miss = 0
Al_SLA = 0

AnthonyA = 1
AnthonyA_Made = 0
AnthonyA_Miss = 0
AnthonyA_SLA = 0

AnthonyC = 1
AnthonyC_Made = 0
AnthonyC_Miss = 0
AnthonyC_SLA = 0

Brian = 1
Brian_Made = 0
Brian_Miss = 0
Brian_SLA = 0

Chris = 1
Chris_Made = 0
Chris_Miss = 0
Chris_SLA = 0

DSen = 1
DSen_Made = 0
DSen_Miss = 0
DSen_SLA = 0

Daniel = 1
Daniel_Made = 0
Daniel_Miss = 0
Daniel_SLA = 0

Debbie = 1
Debbie_Made = 0
Debbie_Miss = 0
Debbie_SLA = 0

Glendora = 1
Glendora_Made = 0
Glendora_Miss = 0
Glendora_SLA = 0

Ishita = 1
Ishita_Made = 0
Ishita_Miss = 0
Ishita_SLA = 0

Jino = 1
Jino_Made = 0
Jino_Miss = 0
Jino_SLA = 0

Kevin = 1
Kevin_Made = 0
Kevin_Miss = 0
Kevin_SLA = 0

Kherlyn = 1
Kherlyn_Made = 0
Kherlyn_Miss = 0
Kherlyn_SLA = 0

Leonard = 1
Leonard_Made = 0
Leonard_Miss = 0
Leonard_SLA = 0

Mohan = 1
Mohan_Made = 0
Mohan_Miss = 0
Mohan_SLA = 0

Muhammad = 1
Muhammad_Made = 0
Muhammad_Miss = 0
Muhammad_SLA = 0

Nayana = 1
Nayana_Made = 0
Nayana_Miss = 0
Nayana_SLA = 0

Neha = 1
Neha_Made = 0
Neha_Miss = 0
Neha_SLA = 0

Nitin = 1
Nitin_Made = 0
Nitin_Miss = 0
Nitin_SLA = 0

Patrick = 1
Patrick_Made = 0
Patrick_Miss = 0
Patrick_SLA = 0

Rashmi = 1
Rashmi_Made = 0
Rashmi_Miss = 0
Rashmi_SLA = 0

Seth = 1
Seth_Made = 0
Seth_Miss = 0
Seth_SLA = 0

Shannon = 1
Shannon_Made = 0
Shannon_Miss = 0
Shannon_SLA = 0

Shanthini = 1
Shanthini_Made = 0
Shanthini_Miss = 0
Shanthini_SLA = 0

Sourabh = 1
Sourabh_Made = 0
Sourabh_Miss = 0
Sourabh_SLA = 0

Sylvia = 1
Sylvia_Made = 0
Sylvia_Miss = 0
Sylvia_SLA = 0

Tessa = 1
Tessa_Made = 0
Tessa_Miss = 0
Tessae_SLA = 0

Tony = 1
Tony_Made = 0
Tony_Miss = 0
Tony_SLA = 0

Vennica = 1
Vennica_Made = 0
Vennica_Miss = 0
Vennica_SLA = 0

Vishal = 1
Vishal_Made = 0
Vishal_Miss = 0
Vishal_SLA = 0

Vivian = 1
Vivian_Made = 0
Vivian_Miss = 0
Vivian_SLA = 0

sla_file_path = "K:\\sla_file_details.csv"
 
assoc_file_path = "K:\\assoc_stats.csv"

def cleanup():
  print("Cleaup old Files")
  if os.path.isfile(assoc_file_path):
    os.remove(assoc_file_path)
  else:
    print("file not found. Extract needs to be completed", dump_file_path)
    sys.exit(1)
cleanup()

  
with open (sla_file_path,'r') as sla_file:
    with open (assoc_file_path,'a', newline='') as assoc:
        readablefile = csv.reader(sla_file)
        #writablefile = csv.writer(assoc) 
        #assoc.write("Name, Closed Tickets, SLA MADE, Percent Closed in SLA "+"\n")
        ##for row in readablefile:
            ##print("\n")
            ##break
        for row in readablefile:
          #date_format = datetime.datetime.strptime(row[12], '%m/%d/%Y %H:%M')
          name = str(row[1])
          SLA = str(row[7])
          if name == "":
            name = "BLANK"
          if name == "Anne Colucci":
            Anne = Anne +1
            target = SLA[3:7]
            if target == "MADE":
              Anne_Made = Anne_Made +1
            else:
              Anne_Miss = Anne_Miss +1
          if name == "Adrian Silva":
            Adrian = Adrian +1
            target = SLA[3:7]
            if target == "MADE":
              Adrian_Made = Adrian_Made +1
            else:
              Adrian_Miss = Adrian_Miss +1
          if name == "Al Dern":
            Al = Al +1
            target = SLA[3:7]
            if target == "MADE":
              Al_Made = Al_Made +1
            else:
              Al_Miss = Al_Miss +1
          if name == "Anthony Ayende":
            AnthonyA = AnthonyA +1
            target = SLA[3:7]
            if target == "MADE":
              AnthonyA_Made = AnthonyA_Made +1
            else:
              AnthonyA_Miss = AnthonyA_Miss +1
          if name == "Anthony Cruz Jr.":
            AnthonyC = AnthonyC +1
            target = SLA[3:7]
            if target == "MADE":
              AnthonyC_Made = AnthonyC_Made +1
            else:
              AnthonyC_Miss = AnthonyC_Miss +1
          if name == "Brian Daley":
            Brian = Brian +1
            target = SLA[3:7]
            if target == "MADE":
              Brian_Made = Brian_Made +1
            else:
              Brian_Miss = Brian_Miss +1
          if name == "Chris Scaglione":
            Chris = Chris +1
            target = SLA[3:7]
            if target == "MADE":
              Chris_Made = Chris_Made +1
            else:
              Chris_Miss = Chris_Miss +1
          if name == "D Sen Wan":
            DSen = DSen + 1
            target = SLA[3:7]
            if target == "MADE":
              DSen_Made = DSen_Made +1
            else:
              DSen_Miss = DSen_Miss +1
          if name == "Daniel Lau":
            Daniel = Daniel +1
            target = SLA[3:7]
            if target == "MADE":
              Daniel_Made = Daniel_Made +1
            else:
              Daniel_Miss = Daniel_Miss +1
          if name == "Debbie Kunovic":
            Debbie = Debbie +1
            target = SLA[3:7]
            if target == "MADE":
              Debbie_Made = Debbie_Made +1
            else:
              Debbie_Miss = Debbie_Miss +1
          if name == "Glendora Anacreon":
            Glendora = Glendora +1
            target = SLA[3:7]
            if target == "MADE":
              Glendora_Made = Glendora_Made +1
            else:
              Glendora_Miss = Glendora_Miss +1
          if name == "Ishita Mehta":
            Ishita = Ishita +1
            target = SLA[3:7]
            if target == "MADE":
              Ishita_Made = Ishita_Made +1
            else:
              Ishita_Miss = Ishita_Miss +1
          if name == "Jino Thomas":
            Jino = Jino +1
            target = SLA[3:7]
            if target == "MADE":
              Jino_Made = Jino_Made +1
            else:
              Jino_Miss = Jino_Miss +1
          if name == "Kevin Wholley":
            Kevin = Kevin +1
            target = SLA[3:7]
            if target == "MADE":
              Kevin_Made = Kevin_Made +1
            else:
              Kevin_Miss = Kevin_Miss +1
          if name == "Kherlyn Etienne":
            Kherlyn = Kherlyn +1
            target = SLA[3:7]
            if target == "MADE":
              Kherlyn_Made = Kherlyn_Made +1
            else:
              Kherlyn_Miss = Kherlyn_Miss +1
          if name == "Leonard Cheng":
            Leonard = Leonard +1
            target = SLA[3:7]
            if target == "MADE":
              Leonard_Made = Leonard_Made +1
            else:
              Leonard_Miss = Leonard_Miss +1
          if name == "Mohan Arun Kumar Bayyavarpu":
            Mohan = Mohan +1
            target = SLA[3:7]
            if target == "MADE":
              Mohan_Made = Mohan_Made +1
            else:
              Mohan_Miss = Mohan_Miss +1
          if name == "Muhammad Zulhilmi Bin Saifulyazan":
            Muhammad = Muhammad +1
            target = SLA[3:7]
            if target == "MADE":
              Muhammad_Made = Muhammad_Made +1
            else:
              Muhammad_Miss = Muhammad_Miss +1
          if name == "Nayana Moolya":
            Nayana = Nayana +1
            target = SLA[3:7]
            if target == "MADE":
              Nayana_Made = Nayana_Made +1
            else:
              Nayana_Miss = Nayana_Miss +1
          if name == "Neha Joshi":
            Neha = Neha +1
            target = SLA[3:7]
            if target == "MADE":
              Neha_Made = Neha_Made +1
            else:
              Neha_Miss = Neha_Miss +1
          if name == "Nitin Jadhav":
            Nitin = Nitin +1
            target = SLA[3:7]
            if target == "MADE":
              Nitin_Made = Nitin_Made +1
            else:
              Nitin_Miss = Nitin_Miss +1
          if name == "Patrick Coughlan":
            Patrick = Patrick +1
            target = SLA[3:7]
            if target == "MADE":
              Patrick_Made = Patrick_Made +1
            else:
              Patrick_Miss = Patrick_Miss +1
          if name == "Rashmi Deoli":
            Rashmi = Rashmi +1
            target = SLA[3:7]
            if target == "MADE":
              Rashmi_Made = Rashmi_Made +1
            else:
              Rashmi_Miss = Rashmi_Miss +1
          if name == "Seth Ford":
            Seth = Seth +1
            target = SLA[3:7]
            if target == "MADE":
              Seth_Made = Seth_Made +1
            else:
              Seth_Miss = Seth_Miss +1
          if name == "Shannon Kingen":
            Shannon = Shannon +1
            target = SLA[3:7]
            if target == "MADE":
              Shannon_Made = Shannon_Made +1
            else:
              Shannon_Miss = Shannon_Miss +1
          if name == "Shanthini Balaji":
            Shanthini = Shanthini +1
            target = SLA[3:7]
            if target == "MADE":
              Shanthini_Made = Shanthini_Made +1
            else:
              Shanthini_Miss = Shanthini_Miss +1
          if name == "Sourabh Sahu":
            Sourabh = Sourabh +1
            target = SLA[3:7]
            if target == "MADE":
              Sourabh_Made = Sourabh_Made +1
            else:
              Sourabh_Miss = Sourabh_Miss +1
          if name == "Sylvia Aldridge-Gibson":
            Sylvia = Sylvia +1
            target = SLA[3:7]
            if target == "MADE":
              Sylvia_Made = Sylvia_Made +1
            else:
              Sylvia_Miss = Sylvia_Miss +1
          if name == "Tessa Springer":
            Tessa = Tessa +1
            target = SLA[3:7]
            if target == "MADE":
              Tessa_Made = Tessa_Made +1
            else:
              Tessa_Miss = Tessa_Miss +1
          if name == "Tony Suarez":
            Tony = Tony +1
            target = SLA[3:7]
            if target == "MADE":
              Tony_Made = Tony_Made +1
            else:
              Tony_Miss = Tony_Miss +1
          if name == "Vennica Li":
            Vennica = Vennica +1
            target = SLA[3:7]
            if target == "MADE":
              Vennica_Made = Vennica_Made +1
            else:
              Vennica_Miss = Vennica_Miss +1
          if name == "Vishal Shinde":
            Vishal = Vishal +1
            target = SLA[3:7]
            if target == "MADE":
              Vishal_Made = Vishal_Made +1
            else:
              Vishal_Miss = Vishal_Miss +1
          if name == "Vivian Obregon":
            Vivian = Vivian +1
            target = SLA[3:7]
            if target == "MADE":
              Vivian_Made = Vivian_Made +1
            else:
              Vivian_Miss = Vivian_Miss +1
##

 
    
#print(name, SLA)
Anne_SLA = '{0:.2f}'.format((Anne_Made/Anne * 100))
print("Anne has closed",Anne, "of those", Anne_Made, "Were in the SLA for a SLA met percent of",Anne_SLA)
 

#print(Adrian,"Adrian")
Adrian_SLA = '{0:.2f}'.format((Adrian_Made/Adrian * 100))
print("Adrian has closed",Adrian, "of those", Adrian_Made, "Were in the SLA for a SLA met percent of",Adrian_SLA)

#print(Al,"Al")
Al_SLA = '{0:.2f}'.format((Al_Made/Al * 100))
print("Al has closed",Al, "of those", Al_Made, "Were in the SLA for a SLA met percent of",Al_SLA)

#print(AnthonyA,"AnthonyA")
AnthonyA_SLA = '{0:.2f}'.format((AnthonyA_Made/AnthonyA * 100))
print("AnthonyA has closed",AnthonyA, "of those", AnthonyA_Made, "Were in the SLA for a SLA met percent of",AnthonyA_SLA)
      
#print(AnthonyC,"AnthonyC")
AnthonyC_SLA = '{0:.2f}'.format((AnthonyC_Made/AnthonyC * 100))
print("AnthonyC has closed",AnthonyC, "of those", AnthonyC_Made, "Were in the SLA for a SLA met percent of",AnthonyC_SLA)

#print(Brian,"Brian")
Brian_SLA = '{0:.2f}'.format((Brian_Made/Brian * 100))
print("Brian has closed",Brian, "of those", Brian_Made, "Were in the SLA for a SLA met percent of",Brian_SLA)

#print(Chris,"Chris")
Chris_SLA = '{0:.2f}'.format((Chris_Made/Chris * 100))
print("Chris has closed",Chris, "of those", Chris_Made, "Were in the SLA for a SLA met percent of",Chris_SLA)

#print(DSen,"DSen")
DSen_SLA = '{0:.2f}'.format((DSen_Made/DSen * 100))
print("DSen has closed",DSen, "of those", DSen_Made, "Were in the SLA for a SLA met percent of",DSen_SLA)

#print(Daniel,"Daniel")
Daniel_SLA = '{0:.2f}'.format((Daniel_Made/Daniel * 100))
print("Daniel has closed",Daniel, "of those", Daniel_Made, "Were in the SLA for a SLA met percent of",Daniel_SLA)

#print(Debbie,"Debbie")
Debbie_SLA = '{0:.2f}'.format((Debbie_Made/Debbie * 100))
print("Debbie has closed",Debbie, "of those", Debbie_Made, "Were in the SLA for a SLA met percent of",Debbie_SLA)

#print(Glendora,"Glendora")
Glendora_SLA = '{0:.2f}'.format((Glendora_Made/Glendora * 100))
print("Glendora has closed",Glendora, "of those", Glendora_Made, "Were in the SLA for a SLA met percent of",Glendora_SLA)

#print(Ishita,"Ishita")
Ishita_SLA = '{0:.2f}'.format((Ishita_Made/Ishita * 100))
print("Ishita has closed",Ishita, "of those", Ishita_Made, "Were in the SLA for a SLA met percent of",Ishita_SLA)

#print(Jino,"Jino")
Jino_SLA = '{0:.2f}'.format((Jino_Made/Jino * 100))
print("Jino has closed",Jino, "of those", Jino_Made, "Were in the SLA for a SLA met percent of",Jino_SLA)

#print(Kevin,"Kevin")
Kevin_SLA = '{0:.2f}'.format((Kevin_Made/Kevin * 100))
print("Kevin has closed",Kevin, "of those", Kevin_Made, "Were in the SLA for a SLA met percent of",Kevin_SLA)

#print(Kherlyn,"Kherlyn")
Kherlyn_SLA = '{0:.2f}'.format((Kherlyn_Made/Kherlyn * 100))
print("Kherlyn has closed",Kherlyn, "of those", Kherlyn_Made, "Were in the SLA for a SLA met percent of",Kherlyn_SLA)

#print(Leonard,"Leonard")
Leonard_SLA = '{0:.2f}'.format((Leonard_Made/Leonard * 100))
print("Leonard has closed",Leonard, "of those", Leonard_Made, "Were in the SLA for a SLA met percent of",Leonard_SLA)

#print(Mohan,"Mohan")
Mohan_SLA = '{0:.2f}'.format((Mohan_Made/Mohan * 100))
print("Mohan has closed",Mohan, "of those", Mohan_Made, "Were in the SLA for a SLA met percent of",Mohan_SLA)

#print(Muhammad,"Muhammad")
Muhammad_SLA = '{0:.2f}'.format((Muhammad_Made/Muhammad * 100))
print("Muhammad has closed",Muhammad, "of those", Muhammad_Made, "Were in the SLA for a SLA met percent of",Muhammad_SLA)

#print(Nayana,"Nayana")
Nayana_SLA = '{0:.2f}'.format((Nayana_Made/Nayana * 100))
print("Nayana has closed",Nayana, "of those", Nayana_Made, "Were in the SLA for a SLA met percent of",Nayana_SLA)

#print(Neha,"Neha")
Neha_SLA = '{0:.2f}'.format((Neha_Made/Neha * 100))
print("Neha has closed",Neha, "of those", Neha_Made, "Were in the SLA for a SLA met percent of",Neha_SLA)

#print(Nitin,"Nitin")
Nitin_SLA = '{0:.2f}'.format((Nitin_Made/Nitin * 100))
print("Nitin has closed",Nitin, "of those", Nitin_Made, "Were in the SLA for a SLA met percent of",Nitin_SLA)

#print(Patrick,"Patrick")
Patrick_SLA = '{0:.2f}'.format((Patrick_Made/Patrick * 100))
print("Patrick has closed",Patrick, "of those", Patrick_Made, "Were in the SLA for a SLA met percent of",Patrick_SLA)

#print(Rashmi,"Rashmi")
Rashmi_SLA = '{0:.2f}'.format((Rashmi_Made/Rashmi * 100))
print("Rashmi has closed",Rashmi, "of those", Rashmi_Made, "Were in the SLA for a SLA met percent of",Rashmi_SLA)

#print(Seth,"Seth")
Seth_SLA = '{0:.2f}'.format((Seth_Made/Seth * 100))
print("Seth has closed",Seth, "of those", Seth_Made, "Were in the SLA for a SLA met percent of",Seth_SLA)

#print(Shannon,"Shannon")
Shannon_SLA = '{0:.2f}'.format((Shannon_Made/Shannon * 100))
print("Shannon has closed",Shannon, "of those", Shannon_Made, "Were in the SLA for a SLA met percent of",Shannon_SLA)

#print(Shanthini,"Shanthini")
Shanthini_SLA = '{0:.2f}'.format((Shanthini_Made/Shanthini * 100))
print("Shanthini has closed",Shanthini, "of those", Shanthini_Made, "Were in the SLA for a SLA met percent of",Shanthini_SLA)

#print(Sourabh,"Sourabh")
Sourabh_SLA = '{0:.2f}'.format((Sourabh_Made/Sourabh * 100))
print("Sourabh has closed",Sourabh, "of those", Sourabh_Made, "Were in the SLA for a SLA met percent of",Sourabh_SLA)

#print(Sylvia,"Sylvia")
Sylvia_SLA = '{0:.2f}'.format((Sylvia_Made/Sylvia * 100))
print("Sylvia has closed",Sylvia, "of those", Sylvia_Made, "Were in the SLA for a SLA met percent of",Sylvia_SLA)

#print(Tessa,"Tessa")
Tessa_SLA = '{0:.2f}'.format((Tessa_Made/Tessa * 100))
print("Tessa has closed",Tessa, "of those", Tessa_Made, "Were in the SLA for a SLA met percent of",Tessa_SLA)

#print(Tony,"Tony")
Tony_SLA = '{0:.2f}'.format((Tony_Made/Tony * 100))
print("Tony has closed",Tony, "of those", Tony_Made, "Were in the SLA for a SLA met percent of",Tony_SLA)

#print(Vennica,"Vennica")
Vennica_SLA = '{0:.2f}'.format((Vennica_Made/Vennica * 100))
print("Vennica has closed",Vennica, "of those", Vennica_Made, "Were in the SLA for a SLA met percent of",Vennica_SLA)

#print(Vishal,"Vishal")
Vishal_SLA = '{0:.2f}'.format((Vishal_Made/Vishal * 100))
print("Vishal has closed",Vishal, "of those", Vishal_Made, "Were in the SLA for a SLA met percent of",Vishal_SLA)

#print(Vivian,"Vivian")
Vivian_SLA = '{0:.2f}'.format((Vivian_Made/Vivian * 100))
print("Vivian has closed",Vivian, "of those", Vivian_Made, "Were in the SLA for a SLA met percent of",Vivian_SLA)

with open (assoc_file_path,'a', newline='') as assoc:
    assoc.write("Name, Total Tickets, Met SLA, Missed SLA, Percent in SLA "+"\n")

with open (assoc_file_path,'a', newline='') as assoc:
  writablefile = csv.writer(assoc)
  #print(type(Anne))
  #print(type(Anne_Made))
  #print(type(Anne_SLA))
  Anne = str(Anne)
  Anne_Made = str(Anne_Made)
  Anne_Miss = str(Anne_Miss)
  Adrian = str(Adrian)
  Adrian_Made = str(Adrian_Made)
  Adrian_Miss = str(Adrian_Miss)
  Al = str(Al) 
  Al_Made = str(Al_Made)
  Al_Miss = str(Al_Miss)
  AnthonyA = str(AnthonyA)
  AnthonyA_Made = str(AnthonyA_Made)
  AnthonyA_Miss = str(AnthonyA_Miss)
  AnthonyC = str(AnthonyC)
  AnthonyC_Made = str(AnthonyC_Made)
  AnthonyC_Miss = str(AnthonyC_Miss)
  Brian = str(Brian)
  Brian_Made = str(Brian_Made)
  Brian_Miss = str(Brian_Miss)
  Chris = str(Chris)
  Chris_Made = str(Chris_Made)
  Chris_Miss = str(Chris_Miss)
  DSen = str(DSen)
  DSen_Made = str(DSen_Made)
  DSen_Miss = str(DSen_Miss)
  Daniel = str(Daniel)
  Daniel_Made = str(Daniel_Made)
  Daniel_Miss = str(Daniel_Miss)
  Debbie = str(Debbie)
  Debbie_Made = str(Debbie_Made)
  Debbie_Miss = str(Debbie_Miss)
  Glendora = str(Glendora)
  Glendora_Made = str(Glendora_Made)
  Glendora_Miss = str(Glendora_Miss)
  Ishita = str(Ishita)
  Ishita_Made = str(Ishita_Made)
  Ishita_Miss = str(Ishita_Miss)
  Jino = str(Jino)
  Jino_Made = str(Jino_Made)
  Jino_Miss = str(Jino_Miss)
  Kevin = str(Kevin)
  Kevin_Made = str(Kevin_Made)
  Kevin_Miss = str(Kevin_Miss)
  Kherlyn = str(Kherlyn)
  Kherlyn_Made = str(Kherlyn_Made)
  Kherlyn_Miss = str(Kherlyn_Miss)
  Leonard = str(Leonard)
  Leonard_Made = str(Leonard_Made)
  Leonard_Miss = str(Leonard_Miss)
  Mohan = str(Mohan)
  Mohan_Made = str(Mohan_Made)
  Mohan_Miss = str(Mohan_Miss)
  Muhammad = str(Muhammad)
  Muhammad_Made = str(Muhammad_Made)
  Muhammad_Miss = str(Muhammad_Miss)
  Nayana = str(Nayana)
  Nayana_Made = str(Nayana_Made)
  Nayana_Miss = str(Nayana_Miss)
  Neha = str(Neha)
  Neha_Made = str(Neha_Made)
  Neha_Miss = str(Neha_Miss)
  Nitin = str(Nitin)
  Nitin_Made = str(Nitin_Made)
  Nitin_Miss = str(Nitin_Miss)
  Patrick = str(Patrick)
  Patrick_Made = str(Patrick_Made)
  Patrick_Miss = str(Patrick_Miss)
  Rashmi = str(Rashmi)
  Rashmi_Made = str(Rashmi_Made)
  Rashmi_Miss = str(Rashmi_Miss)
  Seth = str(Seth)
  Seth_Made = str(Seth_Made)
  Seth_Miss = str(Seth_Miss)
  Shannon = str(Shannon)
  Shannon_Made = str(Shannon_Made)
  Shannon_Miss = str(Shannon_Miss)
  Shanthini = str(Shanthini)
  Shanthini_Made = str(Shanthini_Made)
  Shanthini_Miss = str(Shanthini_Miss)
  Sourabh = str(Sourabh) 
  Sourabh_Made = str(Sourabh_Made)
  Sourabh_Miss = str(Sourabh_Miss)
  Sylvia = str(Sylvia)
  Sylvia_Made = str(Sylvia_Made)
  Sylvia_Miss = str(Sylvia_Miss)
  Tessa = str(Tessa)
  Tessa_Made = str(Tessa_Made)
  Tessa_Miss = str(Tessa_Miss)
  Tony = str(Tony)
  Tony_Made = str(Tony_Made)
  Tony_Miss = str(Tony_Miss)
  Vennica = str(Vennica)
  Vennica_Made = str(Vennica_Made)
  Vennica_Miss = str(Vennica_Miss)
  Vishal = str(Vishal)
  Vishal_Made = str(Vishal_Made)
  Vishal_Miss = str(Vishal_Miss)
  Vivian = str(Vivian)
  Vivian_Made = str(Vivian_Made)
  Vivian_Miss = str(Vivian_Miss)

  lst=("Anne",Anne,Anne_Made,Anne_Miss,Anne_SLA)
  writablefile.writerow(lst)
  lst=("Adrian",Adrian,Adrian_Made,Adrian_Miss,Adrian_SLA)
  writablefile.writerow(lst)
  lst=("Al",Al,Al_Made,Al_Miss,Al_SLA)
  writablefile.writerow(lst)

  lst=("AnthonyA",AnthonyA,AnthonyA_Made,AnthonyA_Miss,AnthonyA_SLA)
  writablefile.writerow(lst) 
  lst=("AnthonyC",AnthonyC,AnthonyC_Made,AnthonyC_Miss,AnthonyC_SLA)
  writablefile.writerow(lst) 
  lst=("Brian",Brian,Brian_Made,Brian_Miss,Brian_SLA)
  writablefile.writerow(lst) 
  lst=("Chris",Chris,Chris_Made,Chris_Miss,Chris_SLA)
  writablefile.writerow(lst) 
  lst=("DSen",DSen,DSen_Made,DSen_Miss,DSen_SLA)
  writablefile.writerow(lst) 
  lst=("Daniel",Daniel,Daniel_Made,Daniel_Miss,Daniel_SLA)
  writablefile.writerow(lst) 
  lst=("Debbie",Debbie,Debbie_Made,Debbie_Miss,Debbie_SLA)
  writablefile.writerow(lst) 
  lst=("Glendora",Glendora,Glendora_Made,Glendora_Miss,Glendora_SLA)
  writablefile.writerow(lst) 
  lst=("Ishita",Ishita,Ishita_Made,Ishita_Miss,Ishita_SLA)
  writablefile.writerow(lst) 
  lst=("Jino",Jino,Jino_Made,Jino_Miss,Jino_SLA)
  writablefile.writerow(lst) 
  lst=("Kevin",Kevin,Kevin_Made,Kevin_Miss,Kevin_SLA)
  writablefile.writerow(lst) 
  lst=("Kherlyn",Kherlyn,Kherlyn_Made,Kherlyn_Miss,Kherlyn_SLA)
  writablefile.writerow(lst) 
  lst=("Leonard",Leonard,Leonard_Made,Leonard_Miss,Leonard_SLA)
  writablefile.writerow(lst) 
  lst=("Mohan",Mohan,Mohan_Made,Mohan_Miss,Mohan_SLA)
  writablefile.writerow(lst) 
  lst=("Muhammad",Muhammad,Muhammad_Made,Muhammad_Miss,Muhammad_SLA)
  writablefile.writerow(lst) 
  lst=("Nayana",Nayana,Nayana_Made,Nayana_Miss,Nayana_SLA)
  writablefile.writerow(lst) 
  lst=("Neha",Neha,Neha_Made,Neha_Miss,Neha_SLA)
  writablefile.writerow(lst) 
  lst=("Nitin",Nitin,Nitin_Made,Nitin_Miss,Nitin_SLA)
  writablefile.writerow(lst) 
  lst=("Patrick",Patrick,Patrick_Made,Patrick_Miss,Patrick_SLA)
  writablefile.writerow(lst)
  lst=("Rashmi",Rashmi,Rashmi_Made,Rashmi_Miss,Rashmi_SLA)
  writablefile.writerow(lst) 
  lst=("Seth",Seth,Seth_Made,Seth_Miss,Seth_SLA)
  writablefile.writerow(lst) 
  lst=("Shannon",Shannon,Shannon_Made,Shannon_Miss,Shannon_SLA)
  writablefile.writerow(lst) 
  lst=("Shanthini",Shanthini,Shanthini_Made,Shanthini_Miss,Shanthini_SLA)
  writablefile.writerow(lst) 
  lst=("Sourabh",Sourabh,Sourabh_Made,Sourabh_Miss,Sourabh_SLA) 
  writablefile.writerow(lst) 
  lst=("Sylvia",Sylvia,Sylvia_Made,Sylvia_Miss,Sylvia_SLA)
  writablefile.writerow(lst) 
  lst=("Tessa",Tessa,Tessa_Made,Tessa_Miss,Tessa_SLA)
  writablefile.writerow(lst) 
  lst=("Tony",Tony,Tony_Made,Tony_Miss,Tony_SLA)
  writablefile.writerow(lst) 
  lst=("Vennica",Vennica,Vennica_Made,Vennica_Miss,Vennica_SLA)
  writablefile.writerow(lst) 
  lst=("Vishal",Vishal,Vishal_Made,Vishal_Miss,Vishal_SLA)
  writablefile.writerow(lst) 
  lst=("Vivian",Vivian,Vivian_Made,Vivian_Miss,Vivian_SLA)
  writablefile.writerow(lst) 
 #added 1/18/2021
