 #include<iostream>
 using namespace std;

 int main(){
    int digit, i, p, f, sum = 0;
    cout << "Enter a number: ";
    cin >> digit;
    while(digit != 0){
        p = digit % 10;
        sum += p;
        digit /= 10;
    }
    cout << sum;
 }