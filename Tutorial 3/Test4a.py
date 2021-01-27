user_choice=int(input("1.Celsius to Fahrenheit: \n2.Fahrenheit to Celsius:"))
if user_choice==1:
    tempereture=int(input("Entert the temperature in celcius:")) #the tempereture in celcius value
    print("The tempereture in Fahrenheit:", (9/5)*tempereture+32) # celcius  convert to fahrenheit
elif user_choice==2:
     tempereture=int(input("Entert the temperature in Fahrenheit:")) #the tempereture in fahrenheit value
     print("The tempereture in celcius", (tempereture-32)*5/9) #fahrenheit convert to celcius
    

    
