# Habot

Habot is a Django-based application designed for managing employee records. This application provides RESTful APIs for user management and employee operations, utilizing JWT authentication for secure access.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Setting Up the Project](#setting-up-the-project)
- [Creating a Superuser](#creating-a-superuser)
- [Obtain JWT Tokens](#obtain-jwt-tokens)
- [Using the API](#using-the-api)
  - [Get Employees](#get-employees)
  - [Create Employee](#create-employee)
  - [Update Employee](#update-employee)
  - [Delete Employee](#delete-employee)
- [Environment Variables](#environment-variables)
- [Logging](#logging)
- [License](#license)

## Prerequisites

- Python 3.6 or higher
- Django 5.1 or higher
- Django REST Framework
- Django REST Framework Simple JWT
- PostgreSQL (optional, SQLite is default)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/habot.git
   cd habot
