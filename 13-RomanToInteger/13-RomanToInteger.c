// Last updated: 5/8/2026, 4:23:50 PM
int romanToInt(char* s) 
{
    char roman[] = {'I','V','X','L','C','D','M'};
    int value[] = {1,5,10,50,100,500,1000};

    int ans = 0;
    int length = strlen(s);
    for(int i=0; i<length;i++)
    {
        int current, next = 0;

        for(int j=0; j<7; j++)
        {
            if(s[i] == roman[j])
                current = value[j];
            
            if(i+1 < length && s[i+1] == roman[j])
                next = value[j];
        }

        if(current < next)
            ans -= current;
        else
            ans += current;
    }
    return ans;
}