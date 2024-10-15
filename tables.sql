CREATE TABLE employee IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    departmentId INT NOT NULL,
    contactId INT NOT NULL,
    FOREIGN KEY(departmentId) REFERENCES department(id),
    FOREIGN KEY(contactId) REFERENCES contact(id)
)

CREATE TABLE contact IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phoneNumber VARCHAR(20) NOT NULL,
    city VARCHAR(50) NOT NULL
)

CREATE TABLE department IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    managerId INT NOT NULL,
    FOREIGN KEY(managerId) REFERENCES employee(id)
)

CREATE TABLE project IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    startDate DATE NOT NULL
)

CREATE TABLE employee_project_link IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employeeId INT NOT NULL,
    projectId INT NOT NULL,
    FOREIGN KEY(employeeId) REFERENCES employee(id),
    FOREIGN KEY(projectId) REFERENCES project(id)
)




