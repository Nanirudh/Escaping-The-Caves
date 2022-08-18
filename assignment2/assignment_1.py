#include <bits/stdc++.h>
using namespace std;
void analysis(string ct);
int main(){
    string s = "omkf pi hdn cmgef icphsck .H krg vphqkc c,fic mco kqgf ioqag eo qfcmckf oq ficpihdn cm .Kg dcgeficu hfcm pi hdn cmklo uuncdgmc oqfc mc kfoq afihqfiokgq c!Fi cpgy cvkc yeg mfio kdck kha cokh kodjuck vn k fofvfo gqpojicmoqli opiyoa of kihsc nccqki oefc ynr2 juhpck. Fi c jhkklgm yok oMxr9V1x ya flofigvffic xvgfck. Fio kokfice";
    transform(s.begin(), s.end(),s.begin(), ::tolower); // upper case to lower case conversion
    analysis(s);
}
void analysis(string ct){
    map<char,int> cta;
    map<char,char> replace_map; // replacing map
    for(auto i:ct)
        cta[i]++;
    /* for(auto i:cta)    // Frequency Analysis
        cout<<i.first<<" : "<<i.second<<"\n"; */
    replace_map['c']='e'; // most frequent letter
    replace_map['f']='t'; // using bigram
    replace_map['i']='h';
    replace_map['m']='r'; // using bigram
    replace_map['o']='i';
    replace_map['k']='s'; 
    replace_map['q']='n'; 
    //
    replace_map['h']='a';
    replace_map['e']='f';
    replace_map['a']='g';
    replace_map['g']='o';
    replace_map['d']='m';
    replace_map['u']='l';
    replace_map['p']='c';
    replace_map['l']='w';
    replace_map['n']='b';
    
    replace_map['s']='v';
    replace_map['r']='y';
    replace_map['v']='u';

    replace_map['j']='p';
    replace_map['y']='d';

    replace_map['x']='q';

    //
    /* // Break Point, Enough Bi-grams
    replace_map['a']='g'; // inte re stin 'a' : max a should be 'g'
    //'p'h 'hdn' er - 2 times
     // the rei sn'g't hing'g' 
    replace_map['h']='a'; //inte re stin gth'h'nthison e!
    replace_map['e']='f'; //'e'irst -- first
    //p'h' hdn 'er' - 2 times  -- > chamber
    replace_map['p']='c';
    
    replace_map['n']='b';
    //ca's'es --> caves
    replace_map['s']='v';
    //so meofthe'u' ater ch amb ers
    
    //so meofthel ater ch amb ers'l'i llbemore inte re stin gthanthison e!
    
    //a s'r'o 'v'canse e
    
    //th e 'j'asswor 'y'is
    
    //th e passwor dis ir'x'y'9'u'1x' dg twithoutthe 'x'uotes --> quotes
    replace_map['x']='q';  */
    set<char> anss;
    for(auto i:ct){
        if(replace_map[i]!='\0'){
            //cout<<replace_map[i];
            cout << "\033[1;31m"<<replace_map[i]<<"\033[0m";
            anss.insert(replace_map[i]); 
        }
        else{
            cout<<i;
        }
    }
    /* for(auto i:anss)
        cout<<i<<"\n"; */
    
}