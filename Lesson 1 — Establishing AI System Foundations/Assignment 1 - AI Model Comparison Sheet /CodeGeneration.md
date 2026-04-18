## Prompt

Generate a Java program for a Student Management System that can add, display, search, and delete student records.
Requirements:
- Use classes and objects
- Store student data using ArrayList
- Include menu-driven interaction
- Apply exception handling
- Add comments explaining logic
- Include sample output

## Chatgpt

```java
/*
 Student Management System in Java
 Features:
 - Add student
 - Display students
 - Search student
 - Delete student
 - Uses ArrayList
 - Menu-driven program
 - Includes exception handling
*/

import java.util.*;

// Student class representing student object
class Student {
    int id;
    String name;
    int age;
    String course;

    // Constructor
    Student(int id, String name, int age, String course) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.course = course;
    }

    // Method to display student details
    void displayStudent() {
        System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age + ", Course: " + course);
    }
}

// Main class for Student Management System
public class StudentManagementSystem {

    // ArrayList to store student objects
    static ArrayList<Student> studentList = new ArrayList<>();

    // Scanner object for user input
    static Scanner sc = new Scanner(System.in);

    // Method to add student
    public static void addStudent() {
        try {
            System.out.print("Enter Student ID: ");
            int id = sc.nextInt();
            sc.nextLine(); // consume newline

            System.out.print("Enter Name: ");
            String name = sc.nextLine();

            System.out.print("Enter Age: ");
            int age = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter Course: ");
            String course = sc.nextLine();

            // Create student object
            Student s = new Student(id, name, age, course);

            // Add student to list
            studentList.add(s);

            System.out.println("Student added successfully!\n");

        } catch (InputMismatchException e) {
            System.out.println("Invalid input! Please enter correct data type.\n");
            sc.nextLine(); // clear buffer
        }
    }

    // Method to display all students
    public static void displayStudents() {
        if (studentList.isEmpty()) {
            System.out.println("No student records found.\n");
            return;
        }

        System.out.println("Student Records:");
        for (Student s : studentList) {
            s.displayStudent();
        }
        System.out.println();
    }

    // Method to search student by ID
    public static void searchStudent() {
        try {
            System.out.print("Enter Student ID to search: ");
            int id = sc.nextInt();

            for (Student s : studentList) {
                if (s.id == id) {
                    System.out.println("Student Found:");
                    s.displayStudent();
                    System.out.println();
                    return;
                }
            }

            System.out.println("Student not found.\n");

        } catch (InputMismatchException e) {
            System.out.println("Invalid ID format!\n");
            sc.nextLine();
        }
    }

    // Method to delete student by ID
    public static void deleteStudent() {
        try {
            System.out.print("Enter Student ID to delete: ");
            int id = sc.nextInt();

            Iterator<Student> iterator = studentList.iterator();

            while (iterator.hasNext()) {
                Student s = iterator.next();

                if (s.id == id) {
                    iterator.remove();
                    System.out.println("Student deleted successfully!\n");
                    return;
                }
            }

            System.out.println("Student not found.\n");

        } catch (InputMismatchException e) {
            System.out.println("Invalid ID format!\n");
            sc.nextLine();
        }
    }

    // Main method (program execution starts here)
    public static void main(String[] args) {

        int choice;

        // Infinite loop for menu-driven interaction
        while (true) {

            System.out.println("===== Student Management System =====");
            System.out.println("1. Add Student");
            System.out.println("2. Display Students");
            System.out.println("3. Search Student");
            System.out.println("4. Delete Student");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");

            try {
                choice = sc.nextInt();

                switch (choice) {
                    case 1:
                        addStudent();
                        break;

                    case 2:
                        displayStudents();
                        break;

                    case 3:
                        searchStudent();
                        break;

                    case 4:
                        deleteStudent();
                        break;

                    case 5:
                        System.out.println("Exiting program...");
                        System.exit(0);

                    default:
                        System.out.println("Invalid choice! Try again.\n");
                }

            } catch (InputMismatchException e) {
                System.out.println("Please enter a numeric choice only!\n");
                sc.nextLine();
            }
        }
    }
}


/*
================ SAMPLE OUTPUT =================

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Delete Student
5. Exit
Enter your choice: 1

Enter Student ID: 101
Enter Name: Ravi
Enter Age: 20
Enter Course: BCA
Student added successfully!

Enter your choice: 2
Student Records:
ID: 101, Name: Ravi, Age: 20, Course: BCA

Enter your choice: 3
Enter Student ID to search: 101
Student Found:
ID: 101, Name: Ravi, Age: 20, Course: BCA

Enter your choice: 4
Enter Student ID to delete: 101
Student deleted successfully!

Enter your choice: 5
Exiting program...
================================================
*/
```

## Claude Sonnet 4.6
```java
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

// ─────────────────────────────────────────────
//  Student.java  (inner class for portability)
//  Represents a single student record.
// ─────────────────────────────────────────────
class Student {

    // Instance variables
    private int    id;
    private String name;
    private String course;
    private double gpa;

    // Parameterised constructor
    public Student(int id, String name, String course, double gpa) {
        this.id     = id;
        this.name   = name;
        this.course = course;
        this.gpa    = gpa;
    }

    // ── Getters ──────────────────────────────
    public int    getId()     { return id;     }
    public String getName()   { return name;   }
    public String getCourse() { return course; }
    public double getGpa()    { return gpa;    }

    // ── Setters (used when updating a record) ─
    public void setName(String name)     { this.name   = name;   }
    public void setCourse(String course) { this.course = course; }
    public void setGpa(double gpa)       { this.gpa    = gpa;    }

    // Returns a neatly formatted single-line summary
    @Override
    public String toString() {
        return String.format(
            "│ %-6d │ %-22s │ %-20s │ %-5.2f │",
            id, name, course, gpa
        );
    }
}


// ─────────────────────────────────────────────
//  StudentManager.java
//  Manages the ArrayList and all CRUD operations.
// ─────────────────────────────────────────────
class StudentManager {

    // In-memory store for all student records
    private ArrayList<Student> students = new ArrayList<>();

    // Auto-increment counter for student IDs
    private int nextId = 1;

    // ── Helper: table header ─────────────────
    private void printHeader() {
        System.out.println("┌────────┬────────────────────────┬──────────────────────┬───────┐");
        System.out.println("│ ID     │ Name                   │ Course               │  GPA  │");
        System.out.println("├────────┼────────────────────────┼──────────────────────┼───────┤");
    }

    private void printFooter() {
        System.out.println("└────────┴────────────────────────┴──────────────────────┴───────┘");
    }

    // ── 1. ADD ───────────────────────────────
    /**
     * Prompts for student details, validates input,
     * then appends a new Student object to the ArrayList.
     */
    public void addStudent(Scanner sc) {
        System.out.println("\n──── Add New Student ────");

        System.out.print("Enter Name   : ");
        String name = sc.nextLine().trim();
        if (name.isEmpty()) {
            System.out.println("[ERROR] Name cannot be blank.");
            return;
        }

        System.out.print("Enter Course : ");
        String course = sc.nextLine().trim();
        if (course.isEmpty()) {
            System.out.println("[ERROR] Course cannot be blank.");
            return;
        }

        double gpa = -1;
        while (gpa < 0 || gpa > 10) {
            try {
                System.out.print("Enter GPA (0 – 10) : ");
                gpa = Double.parseDouble(sc.nextLine().trim());
                if (gpa < 0 || gpa > 10)
                    System.out.println("[ERROR] GPA must be between 0 and 10.");
            } catch (NumberFormatException e) {
                System.out.println("[ERROR] Please enter a valid decimal number.");
            }
        }

        // Create and store the new student
        Student s = new Student(nextId++, name, course, gpa);
        students.add(s);
        System.out.println("[SUCCESS] Student added with ID = " + s.getId());
    }

    // ── 2. DISPLAY ALL ───────────────────────
    /**
     * Iterates through the ArrayList and prints
     * every student in a formatted table.
     */
    public void displayAll() {
        System.out.println("\n──── All Students ────");

        if (students.isEmpty()) {
            System.out.println("[INFO] No student records found.");
            return;
        }

        printHeader();
        for (Student s : students) {
            System.out.println(s);        // calls Student.toString()
        }
        printFooter();
        System.out.println("Total records: " + students.size());
    }

    // ── 3. SEARCH ────────────────────────────
    /**
     * Searches by ID (exact) or by name (case-insensitive substring).
     * Demonstrates linear search on an ArrayList.
     */
    public void searchStudent(Scanner sc) {
        System.out.println("\n──── Search Student ────");
        System.out.println("  1. Search by ID");
        System.out.println("  2. Search by Name");
        System.out.print("Choice: ");
        String choice = sc.nextLine().trim();

        ArrayList<Student> results = new ArrayList<>();

        switch (choice) {
            case "1":
                try {
                    System.out.print("Enter Student ID: ");
                    int id = Integer.parseInt(sc.nextLine().trim());

                    // Linear search for matching ID
                    for (Student s : students) {
                        if (s.getId() == id) {
                            results.add(s);
                            break;   // IDs are unique
                        }
                    }
                } catch (NumberFormatException e) {
                    System.out.println("[ERROR] ID must be a whole number.");
                    return;
                }
                break;

            case "2":
                System.out.print("Enter Name (partial OK): ");
                String keyword = sc.nextLine().trim().toLowerCase();

                // Collect all names containing the keyword
                for (Student s : students) {
                    if (s.getName().toLowerCase().contains(keyword)) {
                        results.add(s);
                    }
                }
                break;

            default:
                System.out.println("[ERROR] Invalid choice.");
                return;
        }

        // Display results
        if (results.isEmpty()) {
            System.out.println("[INFO] No matching student found.");
        } else {
            printHeader();
            for (Student s : results) System.out.println(s);
            printFooter();
        }
    }

    // ── 4. DELETE ────────────────────────────
    /**
     * Removes a student by ID.
     * Uses Iterator-style removal via ArrayList.remove() to avoid
     * ConcurrentModificationException.
     */
    public void deleteStudent(Scanner sc) {
        System.out.println("\n──── Delete Student ────");

        try {
            System.out.print("Enter Student ID to delete: ");
            int id = Integer.parseInt(sc.nextLine().trim());

            // Find the student first so we can show a confirmation
            Student target = null;
            for (Student s : students) {
                if (s.getId() == id) {
                    target = s;
                    break;
                }
            }

            if (target == null) {
                System.out.println("[ERROR] No student found with ID = " + id);
                return;
            }

            // Confirm before deleting
            System.out.println("About to delete: " + target.getName() + " (ID " + id + ")");
            System.out.print("Confirm? (y/n): ");
            String confirm = sc.nextLine().trim();

            if (confirm.equalsIgnoreCase("y")) {
                students.remove(target);   // ArrayList.remove(Object)
                System.out.println("[SUCCESS] Student with ID " + id + " deleted.");
            } else {
                System.out.println("[INFO] Deletion cancelled.");
            }

        } catch (NumberFormatException e) {
            System.out.println("[ERROR] ID must be a whole number.");
        }
    }

    // ── 5. COUNT ─────────────────────────────
    public int count() { return students.size(); }
}


// ─────────────────────────────────────────────
//  StudentManagementSystem.java  (entry point)
//  Drives the menu loop and delegates actions.
// ─────────────────────────────────────────────
public class StudentManagementSystem {

    // ── Print the main menu ──────────────────
    private static void printMenu() {
        System.out.println("\n╔══════════════════════════════════╗");
        System.out.println("║   STUDENT MANAGEMENT SYSTEM  v1  ║");
        System.out.println("╠══════════════════════════════════╣");
        System.out.println("║  1. Add Student                  ║");
        System.out.println("║  2. Display All Students         ║");
        System.out.println("║  3. Search Student               ║");
        System.out.println("║  4. Delete Student               ║");
        System.out.println("║  5. Exit                         ║");
        System.out.println("╚══════════════════════════════════╝");
        System.out.print("  Enter choice (1–5): ");
    }

    // ── Seed demo records so the system is not empty at launch ──
    private static void seedData(StudentManager mgr, Scanner sc) {
        // We use the Scanner that belongs to main, but suppress prompts
        // by passing data through a temporary scanner trick.
        // Easier: call package-private helpers directly.
        // For clarity we just add objects manually here.
        String[][] data = {
            {"Alice Johnson",  "Computer Science",   "9.10"},
            {"Bob Martinez",   "Electrical Engg",    "8.45"},
            {"Chitra Suresh",  "Data Science",       "9.50"},
            {"David Lee",      "Mechanical Engg",    "7.80"},
            {"Esha Patel",     "Information Tech",   "8.95"},
        };
        // Access package-level fields is not possible from here without
        // exposing an addDirect method; so we add a convenience method.
    }

    public static void main(String[] args) {

        Scanner sc      = new Scanner(System.in);
        StudentManager mgr = new StudentManager();

        // ── Pre-load five sample records ──────
        System.out.println("[INFO] Loading sample records...");
        String[][] samples = {
            {"Alice Johnson",  "Computer Science",  "9.10"},
            {"Bob Martinez",   "Electrical Engg",   "8.45"},
            {"Chitra Suresh",  "Data Science",      "9.50"},
            {"David Lee",      "Mechanical Engg",   "7.80"},
            {"Esha Patel",     "Information Tech",  "8.95"},
        };

        // Re-use a fake Scanner per row to feed addStudent()
        for (String[] row : samples) {
            String fakeInput = row[0] + "\n" + row[1] + "\n" + row[2] + "\n";
            Scanner fsc = new Scanner(fakeInput);
            mgr.addStudent(fsc);
        }
        System.out.println("[INFO] " + mgr.count() + " sample records loaded.\n");

        // ── Main menu loop ────────────────────
        boolean running = true;

        while (running) {
            printMenu();

            try {
                // Read the menu option; trim whitespace for safety
                String input = sc.nextLine().trim();

                switch (input) {
                    case "1":
                        mgr.addStudent(sc);
                        break;

                    case "2":
                        mgr.displayAll();
                        break;

                    case "3":
                        mgr.searchStudent(sc);
                        break;

                    case "4":
                        mgr.deleteStudent(sc);
                        break;

                    case "5":
                        System.out.println("\nGoodbye! Total students on exit: " + mgr.count());
                        running = false;
                        break;

                    default:
                        // Handle any non-numeric or out-of-range input
                        System.out.println("[ERROR] Invalid choice. Please enter 1–5.");
                }

            } catch (Exception e) {
                // Catch-all safety net for any unexpected runtime errors
                System.out.println("[ERROR] Unexpected error: " + e.getMessage());
            }
        }

        sc.close();  // Release the Scanner resource
    }
}

/* ═══════════════════════════════════════════════════════════════════
   SAMPLE OUTPUT
   ═══════════════════════════════════════════════════════════════════

[INFO] Loading sample records...
[SUCCESS] Student added with ID = 1
[SUCCESS] Student added with ID = 2
[SUCCESS] Student added with ID = 3
[SUCCESS] Student added with ID = 4
[SUCCESS] Student added with ID = 5
[INFO] 5 sample records loaded.

╔══════════════════════════════════╗
║   STUDENT MANAGEMENT SYSTEM  v1  ║
╠══════════════════════════════════╣
║  1. Add Student                  ║
║  2. Display All Students         ║
║  3. Search Student               ║
║  4. Delete Student               ║
║  5. Exit                         ║
╚══════════════════════════════════╝
  Enter choice (1–5): 2

──── All Students ────
┌────────┬────────────────────────┬──────────────────────┬───────┐
│ ID     │ Name                   │ Course               │  GPA  │
├────────┼────────────────────────┼──────────────────────┼───────┤
│ 1      │ Alice Johnson          │ Computer Science     │  9.10 │
│ 2      │ Bob Martinez           │ Electrical Engg      │  8.45 │
│ 3      │ Chitra Suresh          │ Data Science         │  9.50 │
│ 4      │ David Lee              │ Mechanical Engg      │  7.80 │
│ 5      │ Esha Patel             │ Information Tech     │  8.95 │
└────────┴────────────────────────┴──────────────────────┴───────┘
Total records: 5

  Enter choice (1–5): 1

──── Add New Student ────
Enter Name   : Farhan Khan
Enter Course : Civil Engg
Enter GPA (0 – 10) : 8.2
[SUCCESS] Student added with ID = 6

  Enter choice (1–5): 3

──── Search Student ────
  1. Search by ID
  2. Search by Name
Choice: 2
Enter Name (partial OK): chi
┌────────┬────────────────────────┬──────────────────────┬───────┐
│ ID     │ Name                   │ Course               │  GPA  │
├────────┼────────────────────────┼──────────────────────┼───────┤
│ 3      │ Chitra Suresh          │ Data Science         │  9.50 │
└────────┴────────────────────────┴──────────────────────┴───────┘

  Enter choice (1–5): 4

──── Delete Student ────
Enter Student ID to delete: 4
About to delete: David Lee (ID 4)
Confirm? (y/n): y
[SUCCESS] Student with ID 4 deleted.

  Enter choice (1–5): 5

Goodbye! Total students on exit: 5

═══════════════════════════════════════════════════════════════════ */
```

## Gemini  Fast 1.5
```java
import java.util.ArrayList;
import java.util.Scanner;
import java.util.InputMismatchException;

public class StudentManagementSystem {
    private static ArrayList<Student> studentList = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.util.Scanner);

    public static void main(String[] args) {
        while (true) {
            try {
                showMenu();
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1: addStudent(); break;
                    case 2: displayStudents(); break;
                    case 3: searchStudent(); break;
                    case 4: deleteStudent(); break;
                    case 5: 
                        System.out.println("Exiting System. Goodbye!");
                        System.exit(0);
                    default: 
                        System.out.println("Invalid choice. Please select 1-5.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Error: Please enter a valid numerical value.");
                scanner.nextLine(); // Clear the buffer to prevent infinite loops
            }
        }
    }

    private static void showMenu() {
        System.out.println("\n--- Student Management System ---");
        System.out.println("1. Add Student");
        System.out.println("2. Display All Students");
        System.out.println("3. Search Student by ID");
        System.out.println("4. Delete Student");
        System.out.println("5. Exit");
        System.out.print("Enter choice: ");
    }

    private static void addStudent() {
        System.out.print("Enter Student ID: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter Age: ");
        int age = scanner.nextInt();

        studentList.add(new Student(id, name, age));
        System.out.println("Student added successfully!");
    }

    private static void displayStudents() {
        if (studentList.isEmpty()) {
            System.out.println("No records found.");
            return;
        }
        System.out.println("\n--- Student List ---");
        for (Student s : studentList) {
            System.out.println(s);
        }
    }

    private static void searchStudent() {
        System.out.print("Enter ID to search: ");
        int id = scanner.nextInt();
        for (Student s : studentList) {
            if (s.getId() == id) {
                System.out.println("Record Found: " + s);
                return;
            }
        }
        System.out.println("Student with ID " + id + " not found.");
    }

    private static void deleteStudent() {
        System.out.print("Enter ID to delete: ");
        int id = scanner.nextInt();
        boolean removed = studentList.removeIf(s -> s.getId() == id);
        
        if (removed) {
            System.out.println("Student record deleted.");
        } else {
            System.out.println("ID not found.");
        }
    }
}

--- Student Management System ---
1. Add Student
2. Display All Students
3. Search Student by ID
4. Delete Student
5. Exit
Enter choice: 1
Enter Student ID: 101
Enter Name: Alice Smith
Enter Age: 20
Student added successfully!

--- Student Management System ---
Enter choice: 2

--- Student List ---
ID: 101 | Name: Alice Smith | Age: 20

--- Student Management System ---
Enter choice: 4
Enter ID to delete: 101
Student record deleted.

```

## Deepseek r1 1.5b(Local)
```java
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

class Student {
    private int id;
    private String name;
    private String department;
    private int age;

    public Student(int id, String name, String department, int age) {
        this.id = id;
        this.name = name;
        this.department = department;
        this.age = age;
    }

    // Getters
    public int getId() { return id; }
    public String getName() { return name; }
    public String getDepartment() { return department; }
    public int getAge() { return age; }

    @Override
    public String toString() {
        return "ID: " + id + " | Name: " + name + " | Department: " + department + " | Age: " + age;
    }
}

public class StudentManagementSystem {
    private static ArrayList<Student> students = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            displayMenu();
            int choice = getIntInput("Enter choice: ");
            
            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    displayAllStudents();
                    break;
                case 3:
                    searchStudent();
                    break;
                case 4:
                    deleteStudent();
                    break;
                case 5:
                    System.out.println("Exiting program...");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private static void displayMenu() {
        System.out.println("\n--- Student Management System ---");
        System.out.println("1. Add New Student");
        System.out.println("2. Display All Students");
        System.out.println("3. Search Student by ID");
        System.out.println("4. Delete Student by ID");
        System.out.println("5. Exit");
    }

    private static void addStudent() {
        System.out.println("\n--- Add New Student ---");
        int id = getIntInput("Enter student ID: ");
        
        // Check if ID already exists
        if (findStudentById(id) != null) {
            System.out.println("Student ID already exists!");
            return;
        }
        
        String name = getStringInput("Enter student name: ");
        String dept = getStringInput("Enter department: ");
        int age = getIntInput("Enter age: ");
        
        students.add(new Student(id, name, dept, age));
        System.out.println("Student added successfully!");
    }

    private static void displayAllStudents() {
        System.out.println("\n--- All Students ---");
        if (students.isEmpty()) {
            System.out.println("No students found.");
            return;
        }
        for (Student student : students) {
            System.out.println(student);
        }
    }

    private static void searchStudent() {
        System.out.println("\n--- Search Student ---");
        int id = getIntInput("Enter student ID: ");
        Student student = findStudentById(id);
        
        if (student != null) {
            System.out.println("Student found:");
            System.out.println(student);
        } else {
            System.out.println("Student not found!");
        }
    }

    private static void deleteStudent() {
        System.out.println("\n--- Delete Student ---");
        int id = getIntInput("Enter student ID: ");
        Student student = findStudentById(id);
        
        if (student != null) {
            students.remove(student);
            System.out.println("Student deleted successfully!");
        } else {
            System.out.println("Student not found!");
        }
    }

    // Helper method to find student by ID
    private static Student findStudentById(int id) {
        for (Student student : students) {
            if (student.getId() == id) {
                return student;
            }
        }
        return null;
    }

    // Helper method to get integer input with exception handling
    private static int getIntInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter an integer.");
                scanner.nextLine(); // Clear buffer
            }
        }
    }

    // Helper method to get string input
    private static String getStringInput(String prompt) {
        System.out.print(prompt);
        scanner.nextLine(); // Consume newline left-over
        return scanner.nextLine();
    }
}

--- Student Management System ---
1. Add New Student
2. Display All Students
3. Search Student by ID
4. Delete Student by ID
5. Exit
Enter choice: 1

--- Add New Student ---
Enter student ID: 101
Enter student name: Alice Smith
Enter department: Computer Science
Enter age: 20
Student added successfully!

--- Student Management System ---
1. Add New Student
2. Display All Students
3. Search Student by ID
4. Delete Student by ID
5. Exit
Enter choice: 2

--- All Students ---
ID: 101 | Name: Alice Smith | Department: Computer Science | Age: 20

--- Student Management System ---
1. Add New Student
2. Display All Students
3. Search Student by ID
4. Delete Student by ID
5. Exit
Enter choice: 3

--- Search Student ---
Enter student ID: 101
Student found:
ID: 101 | Name: Alice Smith | Department: Computer Science | Age: 20

--- Student Management System ---
1. Add New Student
2. Display All Students
3. Search Student by ID
4. Delete Student by ID
5. Exit
Enter choice: 4

--- Delete Student ---
Enter student ID: 101
Student deleted successfully!

--- Student Management System ---
1. Add New Student
2. Display All Students
3. Search Student by ID
4. Delete Student by ID
5. Exit
Enter choice: 2

--- All Students ---
No students found.
```
