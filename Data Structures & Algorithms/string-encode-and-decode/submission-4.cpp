class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty()) return "";
        string enc;
        for(const string& s : strs){
            enc += to_string(s.size()) + '#' + s;
        }
        return enc;
    }

    vector<string> decode(string s) {
        if(s.empty()) return{};
        vector<string> dec;
        int i=0;
        while(i < s.size()){
            int j = i;
            while(s[j] != '#'){
                j++;
            }
            int len = stoi(s.substr(i, j-i));
            i = j+1;
            j = i+len;
            dec.push_back(s.substr(i, len));
            i=j;
        }
        return dec;
    }
};
