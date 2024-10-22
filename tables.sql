CREATE TABLE contact(
    id INT AUTO_INCREMENT PRIMARY KEY,
    phoneNumber VARCHAR(20) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    departmentId INT NOT NULL,
    contactId INT NOT NULL,
    FOREIGN KEY(contactId) REFERENCES contact(id)
);

CREATE TABLE department (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    managerId INT NOT NULL,
    FOREIGN KEY(managerId) REFERENCES employee(id)
);

ALTER TABLE employee ADD FOREIGN KEY(departmentId) REFERENCES department(id);
ALTER TABLE contact ADD address VARCHAR(200);
ALTER TABLE employee ADD password VARCHAR(20);
ALTER TABLE employee ADD email VARCHAR(100) NOT NULL UNIQUE;
alter table department add description VARCHAR(200);
alter table department modify column managerId INT;
alter table employee modify column contactId INT;

CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    priority ENUM('low', 'medium', 'high') NOT NULL,
    deadline DATE NOT NULL,
    departmentId INT NOT NULL,
    FOREIGN KEY(departmentId) REFERENCES department(id)
);

CREATE TABLE employee_project_link IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employeeId INT NOT NULL,
    projectId INT NOT NULL,
    FOREIGN KEY(employeeId) REFERENCES employee(id),
    FOREIGN KEY(projectId) REFERENCES project(id)
)




