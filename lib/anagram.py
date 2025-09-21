# your code goes here!

class Anagram:
    """
    Anagram detector.

    Initialize with a reference word, then call .match(list_of_candidates)
    to receive a list of valid anagrams (preserving the candidates' original
    spellings and order).
    """

    def __init__(self, word):
        self._original = word
        self._normalized = self._normalize(word)
        self._signature = self._signature_of(self._normalized)

    def _normalize(self, word):
        """Lowercase and strip surrounding whitespace for consistent comparisons."""
        return word.lower().strip()

    def _signature_of(self, normalized_word):
        """Produce a canonical signature (sorted letters) for an anagram check."""
        return ''.join(sorted(normalized_word))

    def match(self, candidates):
        """Return a list of candidates that are anagrams of the original word."""
        results = []
        for candidate in candidates:
            norm = self._normalize(candidate)

            if norm == self._normalized:
                continue

            if self._signature_of(norm) == self._signature:
                results.append(candidate)

        return results
