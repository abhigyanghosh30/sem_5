#include <bits/stdc++.h>
using namespace std;

vector<string> word_tokenizer(string s)
{
    vector <string> words;

    char str[s.size()+1];
    strcpy(str,s.c_str());

    char* tok;

    tok = strtok(str," ");
    while(tok)
    {
        char word[100];
        sscanf(tok,"%s",word);
        words.push_back(word);
        tok = strtok(NULL," ");
    }
    return words;
}

int main()
{
    FILE *fptr;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    if ((fptr = fopen("corpus4.txt", "r")) == NULL)
    {
        printf("Error! opening file");
        // Program exits if file pointer returns NULL.
        exit(1);         
    }
    while ((read = getline(&line, &len, fptr)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
        vector <string> tokens = word_tokenizer(line);
        for(auto it = tokens.begin();it!=tokens.end();it++)
        {
            cout<<*it<<endl;
        }

    }

    
    return 0;
}