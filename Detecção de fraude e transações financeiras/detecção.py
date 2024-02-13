import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Script executado com sucesso!")

# Carregar o conjunto de dados

file_path = "caminho/para/o/seu/arquivo/creditcard.csv" #não foi possivel adicionar o arquivo pois era superior a 25mb
data = pd.read_csv(file_path)

# Separar os recursos (features) e o alvo (target)

X = data.drop('Class', axis=1)
y = data['Class']

# Dividir os dados em conjuntos de treinamento e teste

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#criar random forest

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

#Treinar o modelo

rf_model.fit(X_train, Y_train)

#fazer previssoes nos dados de teste

Y_pred_rf = rf_model.predict(X_test)

#Avaliar o desempenho de modelo de random forest

accuracy_rf = accuracy_score(Y_test, Y_pred_rf)
conf_matrix_rf = confusion_matrix(Y_test, Y_pred_rf)
class_report_rf = classification_report(Y_test, Y_pred_rf)

# Criar o modelo de regressão logistica

model = LogisticRegression()

# Ttrinar o modelo

model.fit (X_train, Y_train)

#Fazer previsoes nos dados de teste

Y_pred = model.predict(X_test)

#Avaliar o desempenho do modelo

accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix (Y_test, Y_pred)
class_report = classification_report(Y_test, Y_pred)

#Exibir metricas de avaliação

print("Acuracia no modelo:", accuracy)
print("\nMatriz de confusão:\n", conf_matrix)
print("\nRelatorio de classificação:\n", class_report)

#exibir metricas RF

print("Acuracia do modelo de random forest:", accuracy_rf)
print("\nMatriz de confusão do modelo de random forest:", conf_matrix_rf)
print("\nRelatorio de classificação do modelo de random forest:\n", class_report_rf)

print("Script executado com sucesso!")
print("feito por Daniel Luis")
