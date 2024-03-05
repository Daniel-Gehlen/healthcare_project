# legacy_system_integration/integration.py
import requests


def get_available_appointments():
    # Implementa a função para obter consultas disponíveis do sistema legado
    try:
        response = requests.get('https://sistema-legado.com/api/appointments')
        if response.status_code == 200:
            return response.json()
        else:
            # Tratar o caso de falha na solicitação
            return []
    except requests.RequestException as e:
        # Tratar o caso de falha na conexão
        print(f"Erro ao obter consultas disponíveis: {e}")
        return []


def get_available_times(appointment_id):
    # Implementa a função para obter horários disponíveis para uma consulta específica do sistema legado
    try:
        response = requests.get(f'https://sistema-legado.com/api/appointments/{appointment_id}/times')
        if response.status_code == 200:
            return response.json()
        else:
            # Tratar o caso de falha na solicitação
            return []
    except requests.RequestException as e:
        # Tratar o caso de falha na conexão
        print(f"Erro ao obter horários disponíveis para a consulta {appointment_id}: {e}")
        return []
