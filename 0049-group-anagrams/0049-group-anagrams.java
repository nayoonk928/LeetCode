import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramGroups = new HashMap<>();
        
        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedS = new String(charArray);
            
            if (!anagramGroups.containsKey(sortedS)) {
                anagramGroups.put(sortedS, new ArrayList<>());
            }
            
            anagramGroups.get(sortedS).add(s);
        }
        
        return new ArrayList<>(anagramGroups.values());
    }
}