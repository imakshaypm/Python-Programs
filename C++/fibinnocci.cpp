#include<iostream>
using namespace std;

int fibi(int x){
    if(x == 1){
        return x;
    }else{
        return (x * fibi(x - 1));
    }
}

int main(){
    int a;
    cout << "Enter a number: ";
    cin >> a;
    cout << fibi(a);
}