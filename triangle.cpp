//Treeshan Yeadram
//Dec 3rd 2018
#include <iostream>
using namespace std;

int main () 
{
 int input;
 double p = 325.70; // Popluation for 2017
 double B = (12.4/1000);
 double D = (8.4/1000);
 double P;
 

 cout<<"Enter number of years? ";
 cin>> input;
 int year = 2017;
  for(int i =0; i<= input;i++)
  {
    P = p + (B*p) -(D*p);
    cout<< P<<endl;
    p=P;
  year ++;
  cout<<"Year  "    << year<< "   "    << P;
  }
 
}


