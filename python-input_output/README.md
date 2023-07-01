## Task 0: Read file

- Function: `read_file(filename="")`
- Description: Read a text file (UTF8) and print its contents to the standard output.

## Task 1: Write to a file

- Function: `write_file(filename="", text="")`
- Description: Write a string to a text file (UTF8) and return the number of characters written.

## Task 2: Append to a file

- Function: `append_write(filename="", text="")`
- Description: Append a string to the end of a text file (UTF8) and return the number of characters added.

## Task 3: Count words in a file

- Function: `count_words(filename="")`
- Description: Read a text file (UTF8) and count the total number of words.

## Task 4: Convert to JSON string

- Function: `to_json_string(my_obj)`
- Description: Convert a Python object to its JSON string representation.

## Task 5: Convert from JSON string to object

- Function: `from_json_string(my_str)`
- Description: Convert a JSON string to a Python object.

## Task 6: Save object to a JSON file

- Function: `save_to_json_file(my_obj, filename)`
- Description: Save a Python object to a JSON file.

## Task 7: Load object from a JSON file

- Function: `load_from_json_file(filename)`
- Description: Load a Python object from a JSON file.

## Task 8:Class to JSON

Function: `class_to_json(obj)`

Description:

- Converts an instance of a class into a JSON serializable dictionary.
- All attributes of the class are serializable (list, dictionary, string, integer, and boolean).
- No module import is allowed.

## Task 9: Student to JSON

- Class: `Student`
- Description: Define a student by their first name, last name, and age. Implement a method `to_json` that retrieves a dictionary representation of a `Student` instance.

## Task 10: Student to JSON with filter

- Class: `Student` (based on Task 9)
- Description: Enhance the `Student` class from Task 9. Implement a method `to_json` that retrieves a dictionary representation of a `Student` instance. If `attrs` is a list of strings, only retrieve the attribute names contained in the list. Otherwise, retrieve all attributes.

## Task 11: Student to disk and reload

- Class: `Student` (based on Task 10)
- Description: Enhance the `Student` class from Task 10. Implement a method `reload_from_json` that replaces all attributes of the `Student` instance based on a provided dictionary representation. Implement serialization and deserialization mechanisms using JSON.

## Task 12: Pascal's Triangle

- Function: `pascal_triangle(n)`
- Description: Create a function that returns a list of lists of integers representing Pascal's triangle of size `n`. Each element in the triangle should be the sum of the two elements above it.