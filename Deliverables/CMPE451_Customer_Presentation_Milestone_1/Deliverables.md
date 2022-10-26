# Deliverables

Here you can find hyperlinks to our deliverable documents:
* [Software Requirements Specification](https://github.com/bounswe/bounswe2022group8/wiki/Requirements)
* Software Design (UML)
* Scenarios and Mockups
* Project Plan
* Individual Contribution Reports
* Customer Milestone 1 Group Review


# Individual Contributions

# Milestone Group Review

### The requirements addressed in this milestone

<summary>1.1.1. Registration/Login</summary>

Please refer to our requirements for glossary and further details.

* 1.1.1.1. Users shall be able to register to the application providing their e-mail, username and password.
   * 1.1.1.1.1. Both e-mail and username shall be unique for each account. 
   * 1.1.1.1.2. Username of the user must start with a letter, cannot end with an underscore, must have at least 6 characters and can consist of letters, numbers or underscores.
   * 1.1.1.1.3. Passwords of the user must have at least 10 characters, cannot be similar to his e-mail or username and cannot be a common password. 
* 1.1.1.2. Users shall be able to log in to the application using their credentials, (username or e-mail), and password.
* 1.1.1.3. Logged-in users shall be able to safely log out.
<summary> 2.6. Security</summary>

* 2.6.1. User passwords shall be at least 10 characters long and cannot consist entirely of letters.
* 2.6.2. User passwords shall be stored in a database using PBKDF2 algorithm with a SHA256 hash.
