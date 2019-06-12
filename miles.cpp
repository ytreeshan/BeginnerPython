//Treeshan Yeadram

  #include <iostream>
using namespace std;
int main()
{
	
	double kms, miles, km_per_mile;
	km_per_mile = 0.621371;
	

	cout << "What is the distance in Kilometer?" << endl;
	cin >> kms;


    miles = kms * km_per_mile;
	cout << "The distance in Miles is: " << miles << endl;
	

	return 0;
}
