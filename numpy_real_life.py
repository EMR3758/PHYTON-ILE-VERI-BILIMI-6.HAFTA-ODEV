import numpy as np
import matplotlib.pyplot as plt

#Rastgele maaş verisi oluşturur.
np.random.seed(42)
employees_salary = np.random.randint(10000, 50000, 500)
departments = np.random.choice([1, 2, 3], 500)

#Ortalama, maksimum ve minimum maaş hesaplama
mean_salary = np.mean(employees_salary)
max_salary = np.max(employees_salary)
min_salary = np.min(employees_salary)

#Departman bazında ortalama maaş hesaplama
department_names = {1: "Engineering", 2: "Accounting", 3: "Marketing"}
department_mean_salary = {name: np.mean(employees_salary[departments == dept]) for dept, name in department_names.items()}

#Histogram çizimi
plt.figure(figsize=(12, 6))
colors = ['blue', 'green', 'red']
max_y_value = 0  # Y-eksenini ayarlamak için maksimum değer

for (department, salaries), color in zip(department_mean_salary.items(), colors):
    data = employees_salary[departments == list(department_names.keys())[list(department_names.values()).index(department)]]
    counts, bins, patches = plt.hist(data, bins=30, alpha=0.5, label=f"{department} (Ortalama: {salaries:.2f} TL, {len(data)} Çalışan)", color=color)
    max_y_value = max(max_y_value, max(counts))  # Maksimum çalışan sayısını bul

#Ortalama, maksimum ve minimum maaşları çizgi olarak gösterir
plt.axvline(mean_salary, color='black', linestyle='dashed', linewidth=2, label=f"Genel Ortalama: {mean_salary:.2f} TL")
plt.axvline(max_salary, color='purple', linestyle='dotted', linewidth=2, label=f"Maks: {max_salary} TL")
plt.axvline(min_salary, color='orange', linestyle='dotted', linewidth=2, label=f"Min: {min_salary} TL")

#Y-eksenini otomatik olarak ayarlar
plt.ylim(0, max_y_value + 5)

plt.xlabel("Maaş (TL)")
plt.ylabel("Çalışan Sayısı")
plt.title("Departmanlara Göre Maaş Dağılımı")
plt.legend()
plt.grid(True)
plt.show()
