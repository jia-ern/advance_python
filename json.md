# Javascript
- JSON stands for JavaScript Object Notation.
- lightweight, text-based data interchange format.
- language-independent, can be used with most programming languages.
- derived from JavaScript but can be used with any programming language.
- "self-describing," making it human-readable.
- Example
```json
{
    "employees": [
        { "firstName": "Amit", "lastName": "Kumar" },
        { "firstName": "Jay", "lastName": "Sharma" },
        { "firstName": "Mohit", "lastName": "Patel" }
    ]
}
```

## JSON Syntax
- Data is written as name/value pairs (e.g., "name": "Mohit").
- Objects are enclosed in curly braces {}.
- Arrays are enclosed in square brackets [].
- Strings are wrapped in double quotes.
- Data values can be strings, numbers, booleans, arrays, objects, or null.

## json.loads() 
- aka. Deserializing JSON
- can be used to parse a valid JSON string and convert it into a Python Dictionary
- read json

## json.dumps()
- aka. Serializing JSON
- convert a subset of Python objects into a JSON string
- write json

## json.update(): 
- updates dictionary with elements from another dictionary object / from an iterable key/value pair.

## Javascript vs Python Data Type
| Python      | Javascript |
|:------------|:-----------|
| int, float  | number     |
| list, tuple | array      |
| str         | string     |
| None        | null       |
| True        | true       |
| False       | false      |
| dict        | object     |

