#include <iostream>
using namespace std;

int main()
{
    FILE *fi, *fo;
    fi = fopen("output_pairs.txt", "r+");
    fo = fopen("outputs.txt", "w+");
    long long int i = 0;
    char temp[65];
    char s1[17];
    while (i < 200000)
    {
        fscanf(fi, "%s", s1);
        
        for (int l = 0; l < 16; l++)
        {
            int x;
            x=(int)s1[l]-102;
            for(int j = 0; j < 4; j++)
            {
                temp[4*l+3-j]=(char)(x%2+48);
                x/=2;
            }
        }
        temp[64] = '\0';
        i++;
        fprintf(fo, "%s\n", temp);
    }
}