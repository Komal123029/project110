import random


responce = "y"

no = random.randint(1,6)

while responce == "y" :
 if no == 1:
  print("[     ]")
  print("[     ]")
  print("[  0  ]")
  print("[     ]")
  print("[     ]")

  if no == 2:
   print("[     ]")
   print("[  0  ]")
   print("[     ]")
   print("[  0  ]")
   print("[     ]")

  if no == 3:
   print("[     ]")
   print("[  0  ]")
   print("[  0  ]")
   print("[  0  ]")
   print("[     ]")

  if no == 4:
   print("[        ]")
   print("[  0  0  ]")
   print("[        ]")
   print("[  0  0  ]")
   print("[        ]")

  if no == 5:
   print("[         ]")
   print("[   0  0  ]")
   print("[     0   ]")
   print("[   0  0  ]")
   print("[         ]") 

  if no == 6:
   print("[         ]")
   print("[  0 0 0  ]")
   print("[         ]")
   print("[  0 0 0  ]")
   print("[         ]")   

 responce = input( "Press Y to roll again N to exit : " )
 
 



