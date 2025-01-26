class Codec:

    # Encodes a list of strings to a single string.
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return chr(258)  # Special character for empty list
        
        separator = chr(257)  # Special separator character
        return separator.join(strs)

    # Decodes a single string to a list of strings.
    def decode(self, s: str) -> list[str]:
        if s == chr(258):  # Check for empty list encoding
            return []
        
        separator = chr(257)  # Special separator character
        return s.split(separator)
