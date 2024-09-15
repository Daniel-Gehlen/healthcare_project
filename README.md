# Healthcare Project

## Overview

The `healthcare_project` is a Django-based web application designed for scheduling medical consultations. It integrates with a legacy system to fetch real-time availability information and allows users to book appointments with healthcare professionals. The project includes user authentication and provides various functionalities for managing and scheduling appointments.

## Features

- **Real-Time Availability:** Fetches real-time availability data from a legacy system's calendar.
- **Appointment Scheduling:** Allows users to book medical consultations based on the availability of healthcare professionals.
- **User Authentication:** Utilizes Django's built-in authentication system for user login and management.
- **Availability Management:** Disables appointment slots upon booking to prevent double-booking.
- **User Interface:** Includes pages for login, scheduling appointments, and viewing appointment history.

## Project Structure

```
healthcare_project
|--static/
|   |--css/
|   |--img/
|   |--js/
|-- healthcare_project
|   |-- __init__.py
|   |-- settings.py       
|   |-- urls.py            
|   |-- wsgi.py           
|-- healthcare
|   |-- migrations/         
|   |--|--avaliacoes/
|   |--|--|--detalhes_avaliacoes.html
|   |--|--|--listar_avaliacoes.html
|   |--|--cadastro/
|   |--|--|--staff/
|   |--|--|--|--cadastro_staff.html
|   |--|--|--user/
|   |--|--|--|--cadastro_user.html
|   |--|--configuracoes/
|   |--|--|--detalhes_configuracoes.html
|   |--|--|--listar_configuracoes.html
|   |--|--consultas/
|   |--|--|--detalhes_consultas.html
|   |--|--|--listar_consultas.html
|   |--|--dashboard/
|   |--|--|--staff/
|   |--|--|--|--taff_dashboard.html
|   |--|--|--user/
|   |--|--|--|--user_dashboard.html
|   |--|--informacoes/
|   |--|--|--detalhes_informacoes_medicas.html
|   |--|--|--listar_informacoes_medicas.html
|   |--|--login/
|   |--|--|--staff/
|   |--|--|--|--login_taff.html
|   |--|--|--user/
|   |--|--|--|--login_user.html
|   |--|--mensagens/
|   |--|--|--detalhes_mensagens.html
|   |--|--|--listar_mensagens.html
|   |--|--relatorios/
|   |--|--|--detalhes_relatorios.html
|   |--|--|--listar_relatorios.html
|   |--|--usuarios/
|   |--|--|--detalhes_usuarios.html
|   |--|--|--listar_usuarios.html
|   |--|--base.html          
|   |-- __init__.py   
|   |-- admin.py       
|   |-- apps.py            
|   |-- models.py          
|   |-- forms.py           
|   |-- urls.py            
|   |-- views.py          
|   |-- tests.py                       
|manage.py               
|sqlite3
```

## Technologies Used

- **Django:** Web framework for building the application.
- **Python:** Programming language used for development.
- **SQLite:** Database used for storing application data.
- **HTML/CSS:** Markup and styling for the web interface.
- **JavaScript:** Client-side scripting for interactive features.
- **Legacy System Integration:** Custom Python scripts to interface with an existing legacy system.

## Setup and Running the Project

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd healthcare_project
   ```

 2. Install Dependencies:

Make sure you have Python installed. Create a virtual environment and install the required packages:  

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Run Migrations:

Apply the database migrations to set up the database schema:

```
python manage.py migrate
```

4. Start the Development Server:

Run the Django development server:

```
python manage.py runserver
```

5. Access the Application:

Open your web browser and navigate to:

```
http://localhost:8000
```
For admin access:

```
http://localhost:8000/admin
```


