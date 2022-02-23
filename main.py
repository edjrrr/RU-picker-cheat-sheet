import math
import datetime
import pytz

easternTime = pytz.timezone('US/Eastern')
tdy = datetime.datetime.now(easternTime)
tdy_date = datetime.datetime.now()
ttt = int(tdy_date.strftime("%d"))
print(ttt)

st_ord = "st"
nd_ord = "nd"
rd_ord = "rd"
th_ord = "th"

if ttt == 1 or ttt == 21 or ttt == 31:
  ord = st_ord
elif ttt == 2 or ttt == 22:
  ord = nd_ord
elif ttt == 3 or ttt == 23:
  ord = rd_ord
else:
  ord = th_ord

  
print("Today is " + tdy.strftime("%A, %B %d" + ord + " %Y. Current time: %H:%M %p"))

### EDIT THIS WHEN YOU UPDATE THE CODE TO WORK FOR OTHER LINES
print("\nWorks for RHF, RHR, LHF, and LHR")
print("Use lower case letters e.g. 101x9, NOT 101X9")
print("Will show: hours needed to complete an order")
print("Will show: componets needed")
print("Will show: Amount of green/blue racks needed")
print("If something isn't working, let me know")
### EDIT THIS WHEN YOU UPDATE THE CODE TO WORK FOR OTHER LINES

print("\nWhat is your order and amount?")
descRHF = {
  "101x9": "\nDX9 panel, non-lit, DX9/LA3 armrest, NZA bezel, DX9 mid, no badge.",
  "101a3": "\nPD2 panel, non-lit, DX9/LA3 armrest, NA5 bezel, DX9 mid, no badge.",
  "941a3": "\nPD2 panel, non-lit, DX9/LA3 armrest, PS6 bezel, DX9 mid, no badge.",
  "461k5": "\nDX9 panel, lit, LK5/LK5 armrest, WF070 bezel, LK5 mid, badge.",
  "451a3": "\nPD2 panel, lit, DX9/LA3 armrest, WF070 bezel, DX9 mid, badge.",
  "351x9": "\nDXP panel, lit, DX9/LA3 armrest, WF029 bezel, DX9 mid, badge."
    
}

descRHR = {
  "702": "\nPD2/DX9 panel with sunshade.",
  "712": "\nPD2/DX9 panel with sunshade.",
  "70dx9": "\nDX9/DX9 panel with sunshade.",
  "71dx9": "\nDX9/DX9 panel with sunshade.",
  "701k5": "\nDX9/LK5 panel with sunshade.",
  "711k5": "\nDX9/LK5 panel with sunshade.",
  "682": "\nPD2/DX9 panel without sunshade.",
  "68dx9": "\nDX9/DX9 panel without sunshade."
    
}

descLHR = {
  "632": "\nPD2/DX9 panel without sunshade.",
  "652": "\nPD2/DX9 panel with sunshade.",
  "662": "\nPD2/DX9 panel with sunshade.",
  "65x9": "\nDX9/DX9 panel with sunshade.",
  "66x9": "\nDX9/DX9 panel with sunshade."

  
}

descLHF ={
  "401x9":"\nDX9 panel, non-lit, DX9/LA3 armrest, NZA-79 bezel, DX9 mid, no badge",
  "431x9":"\nDX9 panel, non-lit, DX9/LA3 armrest, NZA-81 bezel, PHEV DX9 mid, no badge.",
  "451x9": "\nDX9 panel, non-lit, DX9/LA3 armrest, NZA-81 bezel, DX9 mid, no badge. ",
  "311x9": "\nDX9 panel, lit, DX9/LA3 armrest, WF029 bezel, PHEV DX9 mid, badge.",
  "381x9": "\nDX9 panel, lit, DX9/LA3 armrest, WF029 bezel, DX9 mid, badge.",
  "501k5": "\nDX9 panel, lit, LK5/LK5 armrest, WF070 bezel, LK5 mid, badge.",
  "621k5": "\nDX9 panel, lit, LK5/LK5 armrest, WF070 bezel, PHEV LK5 mid, badge.",
  "491a3": "\nPD2 panel, lit, DX9/LA3 armrest, WF070 bezel, DX9 mid, badge.",
  "451a3": "\nPD2 panel, non-lit, DX9/LA3 armrest, NA5-81 bezel, DX9 mid, no badge.",
  "431a3": "\nPD2 panel, non-lit, DX9/LA3 armrest, NA5-81 bezel, PHEV DX9 mid, no badge.",
  "931a3": "\nPD2 panel, non-lit, Dx9/LA3 armrest, PS6-79 bezel, DX9 mid, no badge."
  
}

redo = True

while redo == True:
  x = input("\nOrder: ")
  y = float(input("Amount: "))
  bL = str(round(y / 20, 2))
  gL = str(round(y / 16, 2))
  shp = str(round(y / 28, 1))
  bL_rnd = str(math.ceil(y / 20))
  gL_rnd = str(math.ceil(y /16))
  xtrabL = math.floor(((math.ceil(y /20)) * 20) -20 * (y / 20))
  xtragL = math.floor(((math.ceil(y /16)) * 16) -16 * (y / 16))

  if xtrabL == 1 or xtragL == 1:
    prt = "part"
  else:
    prt = "parts"

  
  if (y % 28) != 0:
    qty = (y / 28) * .56 
    Ireg = "\nIrregular amount (not a full shipping rack)."
  elif (y % 28 == 0):
    qty = (y / 28) * .56
    Ireg = ""
    
###RIGHT HAND FRONT DOORS
  if x == ("101x9"):
    print("\n---This door is for RIGHT HAND FRONT---")
    print(Ireg)
    print(descRHF["101x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    redo = True
    
  elif x == ("101a3"):
    print("\n---This door is for RIGHT HAND FRONT---")
    print(Ireg)
    print(descRHF["101a3"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    redo = True
    
  elif x == ("941a3"):
    print("\n---This door is for RIGHT HAND FRONT---")
    print(Ireg)
    print(descRHF["941a3"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True
    
  elif x == ("461k5"):
    print("\n---This door is for RIGHT HAND FRONT---")
    print(Ireg)
    print(descRHF["461k5"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    redo = True
    
  elif x == ("451a3"):
    print("\n---This door is for RIGHT HAND FRONT---")
    print(Ireg)
    print(descRHF["451a3"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    redo = True
    
  elif x == ("351x9"):
    print("\n---This door is for RIGHT HAND FRONT---")
    print(Ireg)
    print(descRHF["351x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    redo = True

 ### RIGHT HAND REAR DOORS  
  elif x == ("702"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["702"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("712"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["712"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("70dx9"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["70dx9"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("71dx9"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["71dx9"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("701k5"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["701k5"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("711k5"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["711k5"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("682"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["682"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("68dx9"):
    print("\n---This door is for RIGHT HAND REAR---")
    print(Ireg)
    print(descRHR["68dx9"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

### LEFT HAND REAR DOORS
  elif x == ("632"):
    print("\n---This door is for LEFT HAND REAR---")
    print(Ireg)
    print(descLHR["632"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("652"):
    print("\n---This door is for LEFT HAND REAR---")
    print(Ireg)
    print(descLHR["652"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("662"):
    print("\n---This door is for LEFT HAND REAR---")
    print(Ireg)
    print(descLHR["662"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("65x9"):
    print("\n---This door is for LEFT HAND REAR---")
    print(Ireg)
    print(descLHR["65x9"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True

  elif x == ("66x9"):
    print("\n---This door is for LEFT HAND REAR---")
    print(Ireg)
    print(descLHR["66x9"])
    print(round(qty, 2), "hours to complete.")
    print(gL + " Green racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + gL_rnd + " full green racks with " + str(xtragL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo = True
    
### LEFT HAND FRONT DOORS
  elif x ==("401x9"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["401x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("431x9"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["431x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("451x9"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["451x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("311x9"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["311x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True
    
  elif x ==("381x9"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["431x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("501x9"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["501x9"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("621k5"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["621k5"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("491a3"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["491a3"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("451a3"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["451a3"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("431a3"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["431a3"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  elif x ==("931a3"):
    print("\n---This door is for LEFT HAND FRONT---")
    print(Ireg)
    print(descLHF["931a3"])
    print(round(qty, 2), "hours to complete.")
    print(bL + " Blue racks exactly to finish the " + str(shp) + " shipping rack(s)."" \nOr " + bL_rnd + " full blue racks with " + str(xtrabL) + " extra " + prt +" to spare.")
    print("\nInput another order and amount:")
    redo == True

  else:
    print("\nInvalid order. Input again.")