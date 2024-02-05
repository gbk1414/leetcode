import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #정렬 후 dictonary에 key = sorted(str) : str으로 넣어준 후,
        #모든 key값을 순회하며 값을 리스트로 호출
        #set도 가능할것 같다.
        answer = []
        my_dict = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in my_dict:
                my_dict[sorted_str].append(s)
            else:
                my_dict[sorted_str] = [s]
        all_keys = my_dict.keys()
        for key in all_keys:
            answer.append(my_dict[key])
        return answer
