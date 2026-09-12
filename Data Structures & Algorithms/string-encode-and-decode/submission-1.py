import hashlib

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        hash_object = hashlib.sha256(strs[0].encode('utf-8'))
        hash_string = hash_object.hexdigest()
        print(hash_string.join(strs) + ":" + hash_string)
        return hash_string.join(strs) + ":" + hash_string

    def decode(self, s: str) -> List[str]:
        print(s)
        strs = s.split(':')
        hash_string = strs.pop(-1)
        s = ":".join(strs)
        strs = s.split(hash_string)
        return strs