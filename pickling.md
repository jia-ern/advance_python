# Pickling in Python
- for serializing an object
- entails transforming it into a binary representation 
- can be stored in a file or communicated over a network

# When to use Pickling
- Saving a trained machine learning model to disk in Python.
- Persisting user session data temporarily for quick access.
- Interprocess communication via pipes or sockets in Python.
- Sharing objects between distributed Python programs.
- For programs that require frequent access to costly-to-compute results, 
  - can cache the results using pickling. 
  - serialized data can be written to disk or memory for faster access later.

# When not to use Pickling
- Pickled objects are Python-specific
- Pickled is non Human-Readable Formats
- Unpickling data from untrusted sources may lead to code injection
- MessagePack, Apache Avro, Protocol Buffers may offer better performance & compatibility

# Unpickling in Python
- Deserialization process that converts a binary representation back into a Python object.

# Pickling VS Unpickling
| Feature | Pickling | Unpickling |
| :-- | :-- | :-- |
| Definition | Serialization process that converts a Python object into a binary representation. | Deserialization process that converts a binary representation back into a Python object. |
| Purpose | Allows objects to be stored in a file or transmitted over a network. | Retrieves objects from a stored file or received data. |
| Functions Used | pickle.dump() - Writes objects to a file or a stream. | pickle.load() - Reads objects from a file or a stream. |
| Human-Readability | Objects are converted into a binary format that is not human-readable. | Binary format is converted back into Python objects. |
| Complex Object Support | Supports serialization of complex objects, including custom classes, functions, and data structures. | Supports deserialization of complex objects, including custom classes, functions, and data structures. |
| Object References | Can handle circular references and maintain object references during serialization. | Can restore object references during deserialization, preserving original object relationships. |