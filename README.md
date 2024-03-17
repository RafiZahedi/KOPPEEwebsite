# KOPPEE Website

KOPPEE is a web application for a coffee shop built with Django. It allows users to make reservations for the coffee shop online.

## Features

- Users can make reservations by providing their name, email, preferred date and time, and the number of people.
- Reservations are validated to ensure they meet the criteria, such as not being in the past, within the coffee shop's operating hours, and limited to a maximum number of people.
- Admin panel for managing reservations and viewing available tables.
- Responsive design for desktop and mobile devices.

## Technologies Used

- Django: Python web framework used for backend development.
- HTML, CSS, JavaScript: Frontend technologies for building user interfaces and interactions.
- SCSS: CSS preprocessor for styling.
- Bootstrap: Frontend framework for responsive design and UI components.


   ## Usage

- Visit the website to make a reservation or log in to the admin panel to manage reservations.
- Users can select their desired date and time from the available options.
- Admins can view, create, update, and delete reservations in the admin panel.

## Running the Project
To run the KOPPEE website locally on your machine, follow these steps:

Prerequisites
Python 3.x installed on your system. You can download and install Python from here.
Git installed on your system. You can download and install Git from here.
Steps

1- Clone the repository to your local machine:

git clone https://github.com/RafiZahedi/KOPPEEwebsite.git

2- Navigate to the project directory:

cd koppee-website

3- (Optional) It's recommended to create a virtual environment to isolate the project's dependencies. You can create one using the following command:

python3 -m venv myenv

Activate the virtual environment:

On Windows:

myenv\Scripts\activate

On macOS and Linux:
source myenv/bin/activate

4- Install the project dependencies:

pip install -r requirements.txt

5- Apply migrations to set up the database:

python manage.py migrate

6- Create a superuser account to access the admin panel:

python manage.py createsuperuser

(Follow the prompts to create a superuser account.)

7- Run the development server:

python manage.py runserver

Once the server is running, visit http://localhost:8000 in your web browser to access the KOPPEE website.

To access the admin panel, visit http://localhost:8000/admin and log in using the superuser account you created earlier.

## Additional Information

If you encounter any issues or have questions about running the project, feel free to open an issue on the GitHub repository or reach out to the project maintainers for assistance.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
