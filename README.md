# Dictionary with Concept Graphs

To run the system locally you need to have a local server and database management software - MySQL. Suggestion to use XAMPP - it enables you to install everything easy and quickly.

## Installation with XAMPP

1. Install XAMPP.
2. Download the code.
3. Add the dictionary-system folder to XAMPP htdocs folder.
4. Run XAMPP.
5. Run Apache Web Server and MySQL Database Server.
6. Go to ```localhost/phpmyadmin```
7. Click on Databases
8. Create new database called 'dictionary-system' (you can use a different name but don't forget to change it in the dictionary-system/wp-config.php file, this line: define( 'DB_NAME', '' );
9. Go to ```localhost/dictionary-system/wp-admin/install.php``` and enter the information needed.
10. To open the website go to: ```localhost/dictionary-system```
11. If you want to edit it go to: 
```localhost/dictionary-system/wp-admin```
