class Trie {

    private TrieNode root;
    
    public Trie() {
        this.root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode current = this.root;
        
        for (char c : word.toCharArray()) {
            if (!current.hasChild(c)) {
                current.addChild(c);
            }
            current = current.getChild(c);
        }
        
        current.setEndOfWord(true);
    }
    
    public boolean search(String word) {
        TrieNode current = this.root;
        
        for (char c : word.toCharArray()) {
            if (!current.hasChild(c)) {
                return false;
            }
            current = current.getChild(c);
        }
            
        return current.isEndOfWord();
    }
    
    public boolean startsWith(String prefix) {
        TrieNode current = this.root;
        
        for (char c : prefix.toCharArray()) {
            if (!current.hasChild(c)) {
                return false;
            }
            current = current.getChild(c);
        }
            
        return true;
    }
        
    static class TrieNode {
    
        private boolean endOfWord;
        private Map<Character, TrieNode> children;
    
        TrieNode() {
            this.endOfWord = false;
            this.children = new HashMap<>();
        }
    
        boolean isEndOfWord() {
            return this.endOfWord;
        }
    
        void setEndOfWord(boolean endOfWord) {
            this.endOfWord = endOfWord;
        }
    
        void addChild(Character c) {
            this.children.put(c, new TrieNode());
        }
    
        boolean hasChild(Character c) {
            return this.children.containsKey(c);
        }
    
        TrieNode getChild(Character c) {
            return this.children.getOrDefault(c, null);
        }
    }
}

public class 0208 {
 
    public static void main(String... args) {
        Trie obj = new Trie();
        obj.insert("apple");
        
        boolean param_1 = obj.search("apple");
        System.out.println(param_1); // true
        
        boolean param_2 = obj.search("app");
        System.out.println(param_2); // false  
      
        boolean param_3 = obj.startsWith("app");
        System.out.println(param_3); // true
    }
}
