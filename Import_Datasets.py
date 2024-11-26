from ucimlrepo import fetch_ucirepo
import pandas as pd

# Ambil dataset dengan ID 45 (Heart Disease dataset)
heart_disease = fetch_ucirepo(id=45)

# Dapatkan data fitur (X) dan target (y)
X = heart_disease.data.features
y = heart_disease.data.targets

# menggabungkan colom fitures dan colom target menjadi satu dataframe menggunakan methode concat
heart_disease_df = pd.concat([X, y], axis=1)

# menyimpan dataframe ke dalam file CSV
heart_disease_df.to_csv('heart_disease_datasets.csv', index=False)

# Tampilkan metadata tentang dataset
print("Metadata:")
print(heart_disease.metadata)

# Tampilkan informasi variabel
print("\nInformasi Variabel:")
print(heart_disease.variables)
