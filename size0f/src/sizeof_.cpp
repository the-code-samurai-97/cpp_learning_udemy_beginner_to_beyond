#include <iostream>
#include <climits>
int main(){
    std::cout<<"Size of int "<<sizeof(int)<<" bytes"<<std::endl;
    std::cout<<"Size of char "<<sizeof(char)<<" bytes"<<std::endl;
    std::cout<<"Size of unsigned int "<<sizeof(unsigned int)<<" bytes"<<std::endl;
    std::cout<<"Size of short "<<sizeof(short)<<" bytes"<<std::endl;
    std::cout<<"Size of long "<<sizeof(long)<<" bytes"<<std::endl;
    std::cout<<"Size of long long "<<sizeof(long long)<<" bytes"<<std::endl;
    std::cout<<"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";
    std::cout<<"Size of float "<<sizeof(float)<<" bytes"<<std::endl;
    std::cout<<"Size of double "<<sizeof(double)<<" bytes"<<std::endl;
    std::cout<<"Size of long double "<<sizeof(long double)<<" bytes"<<std::endl;
    std::cout<<"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";

 // <climits>
    std::cout<<"Minimum values"<<std::endl;
    std::cout<<"char "<<CHAR_MIN <<std::endl;
    std::cout<<"int "<<INT_MIN<<std::endl;
    // std::cout<<"DOUBLE "<<DOUBLE_MIN<<" bytes"<<std::endl;
    std::cout<<"short "<<SHRT_MIN<<std::endl;
    std::cout<<"long "<<LONG_MIN<<std::endl;
    std::cout<<"long "<<LLONG_MIN<<std::endl;
    std::cout<<"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";

    std::cout<<"Maximum values"<<std::endl;
    std::cout<<"char "<<CHAR_MAX <<std::endl;
    std::cout<<"int "<<INT_MAX<<std::endl;
    // std::cout<<"DOUBLE "<<DOUBLE_MIN<<" bytes"<<std::endl;

    std::cout<<"short "<<SHRT_MAX<<std::endl;
    std::cout<<"long "<<LONG_MAX<<std::endl;
    std::cout<<"long "<<LLONG_MAX<<std::endl;
    std::cout<<"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";

}