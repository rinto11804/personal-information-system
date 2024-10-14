CREATE TABLE employee IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department_id INT NOT NULL,
    contact_id INT NOT NULL,
    FOREIGN KEY(department_id) REFERENCES department(id)
    FOREIGN KEY(contact_id) REFERENCES contact(id)
)

CREATE TABLE contact IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone_number VARCHAR(20) NOT NULL,
    city VARCHAR(50) NOT NULL,
)

CREATE TABLE department IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    manager_id INT NOT NULL,
    FOREIGN KEY(manager_id) REFERENCES employee(id)
)

CREATE TABLE project IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    budget FLOAT NOT NULL
)

CREATE TABLE employee_project_link IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    FOREIGN KEY(employee_id) REFERENCES employee(id)
    FOREIGN KEY(project_id) REFERENCES project(id)
)




