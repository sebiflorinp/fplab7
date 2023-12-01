<style>
  h5 {
    margin-top: 1px;
    margin-bottom: 1px;
  }

  h4 {
    margin-top: 5px;
    margin-bottom: 5px;
  }

  table {
            border-collapse: collapse;
            border-style: hidden;
  }

  td, th {
    padding: 4px;
  }

  table, td, th{
    border-style: solid;
    border-color: black;
    border-width: thin;
  }

  .center {
    display: flex;
    flex-flow: column nowrap;
    justify-content: flex-start;
    align-items: center;
  }
</style>

<div class = "center">

# Documentation
</div>

## 1. Statement

#### Write an application which manages the marks and the laboratory problems for a certain subject.
#### The application manages:
* #### students:  \<studentId>, \<name>, \<group>
* #### laboratory problem: \<laboratoryNumber_problemNumber>, \<description>, \<deadline>
#### The application allows:
* #### Management of the list of students and laboratory problems.
* #### Add, delete and update the list of students and laboratory problems.
* #### Search a student or a laboratory problem.
* #### Assign a laboratory / Mark a laboratory.
* #### Create statistics:
    * #### list of students and their marks for a given laboratory problem ordered by name alphabetically and mark
    * #### all students with an average mark smaller than 5 (name and average mark)


## 2. Features

<div class="center">

|Index|Feature|
|:-:|:-:|
|F1.1|Add a student to the list of students.|
|F1.2|Delete a student from the list of students.|
|F1.3|Update a student from the list of students.|
|F2.1|Add a problem to the list of laboratory problems.|
|F2.2|Delete a problem from the list of laboratory problems.|
|F2.3|Update a problem from the list of laboratory problems.|
|F3.1|Search a student from the list of students by ID.|
|F3.2|Search a problem from the list of laboratory problems by laboratory number and problem number.|
|F4.1|Assign a laboratory problem.|
|F4.2|Mark a laboratory problem.|
|F5.1|Display all students and their marks at a given laboratory problem ordered alphabetically by their marks|
|F5.2|Display all students whose average mark is smaller than five and their average mark.|

</div>

## 3. Iterations

<div class="center">

|Index|          Planned features          |
|:-:|:----------------------------------:|
|1.| F1.1, F1.2, F1.3, F2.1, F2.2, F2.3 |
|2.|       F3.1, F3.2, F4.1, F4.2       |
|3.|             F5.1, F5.2             |
</div>

## 4. Running scenarios

<div class="center">

### Adding a student

### Scenario #1

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|add student|-|The user chooses to add a new student.|
|2.|-|Input the ID of the student.|The user is asked to input the ID of the student.|
|3.|1|-|The applications receives the input from the user.|
|4.|-|There is already a student with the ID of 1.|The user is notified that there is already a student with the ID of 1.|

### Scenario #2

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|add student|-|The user chooses to add a new student.|
|2.|-|Input the ID of the student.|The user is asked to input the ID of the student.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the name of the student.|The user is asked to input the name of the student.|
|5.|George|-|The application receives the input from the user.|
|6.|-|Input the student's group.|The user is asked to input the student's group.|
|7.|213|-|The application receives the input from the user.|
|8.|-|The student has been added successfully.|The application notifies the user that the operation was successful.|

</div>
<div style="page-break-after: always;"></div>
<div class="center">

### Deleting a student

### Scenario #1
|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|delete student|-|The user chooses to delete a student.|
|2.|-|Input the ID of the student which will be deleted.|The user is asked to input the ID of the student which will be deleted.|
|3.|200|-|The application receives the input from the user.|
|4.|-|There is no student with the ID of 200.|The user is notified that the input ID didn't belong to any student.|

### Scenario #2

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|delete student|-|The user chooses to delete a student.|
|2.|-|Input the ID of the student which will be deleted.|The user is asked to input the ID of the student which will be deleted.|
|3.|213|-|The application receives the input from the user.|
|4.|-|The following student has been deleted successfully.|The user is notified that the student with the input ID was deleted successfully.|
|5.|-|A table.|The application prints a table with the information of the deleted student.|

### Updating a student

### Scenario #1

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|update student|-|The user chooses to update a student.|
|2.|-|Input the ID of the student which will be updated.|The user is asked to input the ID of the student which will be updated.|
|3.|200|-|The application receives the input from the user.|
|4.|-|There is no student with the ID of 200, please input another ID.|The user is notified that the input ID didn't belong to any student.|

</div>
<div style="page-break-after: always;"></div>
<div class="center">

### Scenario #2

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|update student|-|The user chooses to update a student.|
|2.|-|Input the ID of the student which will be updated.|The user is asked to input the ID of the student which will be updated.|
|3.|213|-|The application receives the input from the user.|
|4.|-|The following student will be updated:<br>A table|The application prints a table with the student that will be updated.|
|5.|-|Input the updated name of the student.|The user is asked to input the updated name of the student.|
|6.|Ionel|-|The application receives the input from the user.|
|7.|-|Input the updated student's group.|The user is asked to input the updated student's group.|
|8.|214|-|The application receives the input from the user.|
|9.|-|The student has been updated successfully.|The user is being notified that the update was successful.|

### Adding a problem

### Scenario #1

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|add problem|-|The user chooses to add a new problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|1|-|The application receives the input from the user.|
|6.|-|There is already a problem 2 in laboratory 2.|The user is notified that there's already a problem 2 in laboratory 2.|

</div>
<div style="page-break-after: always;"></div>
<div class="center">

### Scenario #2

Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|add problem|-|The user chooses to add a new problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|2|-|The application receives the input from the user.|
|5.|-|Input the description of the problem.|The user is asked to input the description of the problem.|
|6.|This is a difficult problem.|-|The application receives the input from the user.|
|7.|-|Input the deadline of the problem, it must have the following format: mm/dd/yyyy.|The user is asked to input the deadline of the problem.|
|8.|11/20/2023|-|The application receives the input from the user.|
|9.|-|The problem has been added successfully.|The user is notified that the problem has been added successfully.|

### Deleting a problem

### Scenario #1

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|delete problem|-|The user chooses to delete a problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|12|-|The application receives the input from the user.|
|6.|-|There is no problem 12 in laboratory 2.|The user is notified that the problem 12 from laboratory 2 does not exist.|

</div>
<div style="page-break-after: always;"></div>
<div class="center">

### Scenario #2

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|delete problem|-|The user chooses to delete a problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|2|-|The application receives the input from the user.|
|6.|-|The following problem has been deleted successfully.|The user is notified that the input problem has been deleted.|
|7.|-|A table.|The application prints a table with the information of the deleted problem.|

### Updating a problem

### Scenario #1

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|update problem|-|The user chooses to update a problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|12|-|The application receives the input from the user.|
|6.|-|There is no problem 12 in laboratory 2.|The user is notified that the problem 12 from laboratory 2 does not exist.|

</div>
<div style="page-break-after: always;"></div>
<div class="center">

### Scenario #2

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|update problem|-|The user chooses to update a problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|2|-|The application receives the input from the user.|
|6.|-|The following problem will be updated:<br>A table|The application prints a table with the problem that will be updated.|
|7.|-|Input the updated description of the problem.|The user is asked to input the updated description of the problem.|
|8.|The is an easy problem.|-|The application receives the input from the user.|
|9.|-|Input the updated deadline of the problem, it must have the following format: mm/dd/yyyy.|The user is asked to input the updated deadline of the problem.|
|10.|12/02/2023|-|The application receives the input from the user.|
|11.|-|The problem has been updated successfully.|The user is notified that the problem has been updated successfully.|

</div>
<div style="page-break-after: always;"></div>
<div class="center">

### Searching a student by ID

### Scenario #1

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|search student|-|The user chooses the search a student by their ID.|
|2.|-|Input the ID of the student.|The user is asked to input the ID of student which will be searched.|
|3.|200|-|The application receives the input from the user.|
|4.|-|There is no student with the ID of 200.|The user is notified that the input ID didn't belong to any student.|

### Scenario #2

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|search student|-|The user chooses the search a student by their ID.|
|2.|-|Input the ID of the student.|The user is asked to input the ID of student which will be searched.|
|3.|213|-|The application receives the input from the user.|
|4.|-|A table.|The application prints a table with the information of the searched student.|

### Searching a problem by laboratory number and problem number

### Scenario #1

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|search problem|-|The user chooses to search a problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|12|-|The application receives the input from the user.|
|6.|-|There is no problem 12 in laboratory 2.|The user is notified that the problem 12 from laboratory 2 does not exist.|

### Scenario #2

|Index|Input|Output|Explanation|
|:-:|:-:|:-:|:-:|
|1.|search problem|-|The user chooses to search a problem.|
|2.|-|Input the laboratory of the problem.|The user is asked to input the laboratory of the problem.|
|3.|2|-|The application receives the input from the user.|
|4.|-|Input the number of the problem.|The user is asked to input the number of the problem.|
|5.|2|-|The application receives the input from the user.|
|6.|-|A table.|The application prints a table with the information of the searched problem.|


</div>