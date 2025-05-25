### Hexlet tests and linter status:
[![Actions Status](https://github.com/iKogep23/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/iKogep23/python-project-83/actions)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d90aaf30cb46427d917aa3a9ae58314e)](https://app.codacy.com/gh/iKogep23/python-project-83/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=iKogep23_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=iKogep23_python-project-83)

# Page Analyzer

Page Analyzer is a Flask web application that allows users to analyze web pages for SEO effectiveness. The application checks the availability of websites and analyzes elements such as header, description, and h1 tags.

## Features

- URL availability check.
- Analysis of title and description tags.
- Writes the result to the PostgreSQL database
- Display of check results on the user interface.

## Demo

You can view the application in action at this link:
https://page-analyzer-pgu1.onrender.com


## Technologies

- Python
- Flask
- PostgreSQL
- HTML/CSS
- Bootstrap for frontend
- uv for dependency management

### Prerequisites

Ensure you have Python, uv, and PostgreSQL installed.

### Installation and Running

Use the `Makefile` to simplify the installation and startup process:
```bash
## Configuration
Before running the application, you need to set up your environment variables in file .env at the project root directory with the following variables:
- `SECRET_KEY`: a secret key for your application.
- `DATABASE_URL`: the connection string for your PostgreSQL database, formatted as `postgresql://username:password@localhost:5432/database_name`.
```
