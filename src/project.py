import requests
from input_project import input_project
from output_project import output_project

matritsa, k = input_project()
output_project(matritsa, "Исходная матрица:")

payload = {
    "matrix": matritsa,
    "column": k
}

print("Отправка данных на сервер...")
response = requests.post("http://127.0.0.1:8000/api/delete_column", json=payload)

if response.status_code == 200:
    data = response.json()
    if data["status"] == "success":
        output_project(data["result_matrix"], "Матрица после удаления:")
    else:
        print("Ошибка обработки на сервере.")

input("")