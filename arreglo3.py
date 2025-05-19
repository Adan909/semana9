edades = [18, 17, 17, 16, 20, 27, 19, 21]
print(edades)
#ordenar

edades.sort()
print(edades)

edades.sort(reverse = True)
print(edades)

#Liberia estadistica
import statistics as st

#mostrar media
media = st.mean(edades)
print(f"media: {media}")

#mostrar moda
moda = st.mode(edades)
print(f"Moda: {moda}")