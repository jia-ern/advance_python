# Coding Style & Qualities    16

## 1. Comments
## 2. Formatting & Naming
Formatting Conventions
- Naming rules (NRs)
• NR1. Letters, digits, & underscores are only allowed
• NR2. Digits are not allowed as first character
• NR3. Reserved keywords are not allowed

- Naming conventions (NCs)
• NC1. Self-explanatory and concise names are strongly advised
• NC2. Distinguishable letter cases and parts of speech are strongly advised
  o NC2.1. Variables use a noun phrase with snake case
    - user_email, number_of_rating_stars
  o NC2.2. Constants use a noun phrase with screaming case
    - NUMBER_OF_USERS, TOTAL_VIEWS
  o NC2.3. Functions use a verb phrase with snake case
    - send_email(), read_participant_name()
  o NC2.4. Classes use a noun phrase with Pascal, or upper camel, case
    - HumanMind, LanguageDisplayerView
  o NC2.5. Modules and packages use a noun phrase with lower case
    - planetorbit, languagedisplayermodel
• NC3. Noun phrases are used for names, except for functions that use verb phrases
• NC4. Built-in names are to be avoided

## 3. Coding Qualities [FERE]
3.1  Funtionality: The quality of a source code meeting its specification or functional requirements (FRs)

3.2  Effectiveness: The quality of a source code being fast & using little memory
 o Time: speed
  • algorithm improvement
  • use of additional memory
 o Space: memory usage
  • algorithm improvement
  • use of additional time

3.3  Readability-Maintainability-Reusability: The quality of a source code being easily understood, maintained, & reused as for the aim, data structures, control flow, & functionality.
 o Comments
 o Formatting conventions
 o Naming conventions
 o Constants for unnamed literals
 o Functions, classes, & modules for code organisation

3.4  Elegance: The quality of a source code being written in a concise way.
 o Augmented assignment
  rate += 2
 o Walrus assignment
  print(rate :=  2)
 o Inline if
  charge = 2 if rate == 1 else 3
 o F-strings
  print(f'rate = {rate}')
 o Collection comprehensions
  list_0_9 = [value for value in range(10)]

## 4. Casting
Explicit casting on FIBS

Implicit casting on FIBS
Functions with casting functionality 
