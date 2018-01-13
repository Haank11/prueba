apetece_helado = input("Te apetece un helado? (Si/No): ")
tiene_dinero = input("Tienes dinero (Si/No): ")
esta_el_heladero = input("Esta el heladero? (Si/No): ")
esta_tu_tia = input("Estas con tu tia? (Si/No) :")

if apetece_helado == "Si"
    apetece_helado == True
elif apetece_helado == "No"
    apetece_helado == False
else:
    print("Te dije que me dijeras Si o No, no se que dijiste pero no te doy nada.")
if apetece_helado == "Si" and (tiene_dinero == "Si" or esta_tu_tia == "Si") and esta_el_heladero == "Si" :
    print("Tomate un helado")
else:
    print("No te lo tomes")
