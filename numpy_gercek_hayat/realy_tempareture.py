import numpy as np
import matplotlib.pyplot as plt

#Günlük sıcaklık değerlerini simüle etmE
days = 365
#-10°C ile 40°C arasında rastgele sıcaklıklar üretir.
temperature_data = np.random.randint(-10, 41, size=days)

#Ortalama sıcaklığı bulur.
average_temperature = np.mean(temperature_data)

#En sıcak ve en soğuk günleri değişkene ekler.
max_temperature_day = np.argmax(temperature_data)
min_temperature_day = np.argmin(temperature_data)

#Günlük sıcaklık değişimlerinin çizgi grafiğini oluşturmak için
plt.figure(figsize=(10, 5))
plt.plot(temperature_data, label="Daily Temperature")
plt.title("Daily Temperature Over the Year")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()

