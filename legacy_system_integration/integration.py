import requests


def get_available_appointments():
    try:
        response = requests.get('https://sistema-legado.com/api/appointments')
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.RequestException as e:
        print(f"Erro ao obter consultas disponíveis: {e}")
        return []


def get_available_times(selected_date):
    try:
        response = requests.get(f'https://sistema-legado.com/api/appointments/{selected_date}/times')
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.RequestException as e:
        print(f"Erro ao obter horários disponíveis para a data {selected_date}: {e}")
        return []
