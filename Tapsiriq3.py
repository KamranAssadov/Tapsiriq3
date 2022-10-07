print("""--------------------
      Calculator proqramina xos gelmisiz 
      
      Prossesler:
          1-Toplama
          2-Cixma
          3-Vurma
          4-Bolme
          5-EBOB
          6-EKOB
          7-2 ededin Toplaminin Faktoriali
       --------------------------------
      Proqramdan cixmaq isteyirsinizse "q" ya basin 
       
     """)
         
reqem1= int (input("Ilk reqemi daxil ediniz.."))
reqem2= int (input("Ikinci reqemi daxil ediniz.."))
          
prosses= int (input("Icra edilen funksiyani daxil ediniz"))
while True :
       prosses = input("Prossesi daxil ediniz")
      
       if(prosses=="q"):
           print("Proqramdan cixin")
           break

       elif (prosses==1):
           print("{} ile {}'nin toplami {}-a beraberdir".format(reqem1,reqem2,reqem1+reqem2))
           
       elif (prosses==2):
           print("{} ile {}'nin ferqi {}-a beraberdir".format(reqem1,reqem2,reqem1-reqem2))
          
          
       elif (prosses==3):
           print("{} ile {}'nin vurmasi {}-a beraberdir".format(reqem1,reqem2,reqem1*reqem2))
           
          
       elif (prosses==4):
           print("{} ile {}'nin bolumu {}-a beraberdir".format(reqem1,reqem2,reqem1/reqem2))
         
       elif (prosses==5):
           def ebob_tapma(reqem1,reqem2):
               
                i= 1
                ebob=1
                while (i <= reqem1 and i<= reqem2):
               
                    if (not (reqem1% i)and not (reqem2% i)):
                        ebob=i
                    i+=1
                return ebob


            print("Ebob:",ebob_tapma(reqem1, reqem2))
        elif (prosses==6):
            def ekob_tapma(reqem1,reqem2):
                
                 i= 1
                 ekob=1
                 while (i >= reqem1 and i>= reqem2):
                
                     if (not (reqem1% i)and not (reqem2% i)):
                         ekob=i
                     i-=1
                 return ekob



             print("Ekob:",ekob_tapma(reqem1, reqem2))
             
        elif (prosses==7):
            print("{} ile {}'nin toplami {}-a beraberdir".format(reqem1,reqem2,reqem1+reqem2))
            reqem1+reqem2=reqem3
            reqem3=int(reqem3)
            fakt=1
            
            for i in range(2,reqem3+1):
                fakt *= i
                
            print("Faktorial:",fakt)
            
            
           
         
       else:
           print("Bele bir prosses kodu yoxdur")
           

