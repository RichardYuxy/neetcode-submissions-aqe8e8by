class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> x;

        for(const auto& s : strs){
            vector<int> table(26, 0);
            for (char c : s){
                table[c - 'a']++;
            }
            string key = to_string(table[0]);
            for(int i=1;i<table.size();i++){
                key += ','+to_string(table[i]);
            }
            x[key].push_back(s);
        }

        vector<vector<string>> result;
        for(const auto& pair : x){
            result.push_back(pair.second);
        }

        return result;
    }
};
