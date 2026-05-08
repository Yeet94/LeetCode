// Last updated: 5/8/2026, 4:23:48 PM
char* longestCommonPrefix(char** strs, int strsSize) {
    if(strsSize == 0)
    {
        static char ans[] = "";
        return ans;
    }

    char* prefix = strs[0];
    int prefixlen = strlen(prefix);

    for(int i=0; i<strsSize; i++)
    {
        while(strncmp(prefix,strs[i],prefixlen)!= 0)
        {
            prefixlen--;
            prefix[prefixlen] = '\0';
        }
        if(prefixlen ==0)
            return prefix;
        
    }
    return prefix;
}