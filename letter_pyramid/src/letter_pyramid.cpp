#include <iostream>
#include <string>
#include <algorithm>
// void
int main(int argc,char** argv)
{
    while(std::cin)
    {
        std::cout<<"\n";
        std::cout<<"Enter the string_ ";
        std::string input_string; 
        std::cin>>input_string;
        std::cout<<"\n";
        for(size_t i = 0;i<input_string.size();i++)
        {
            std::string forward_letters ;
            for (size_t j = 0; j <= i; j++)
            {
                forward_letters+=input_string[j];
            }

            std::string backward_letters = forward_letters ;
            std::reverse(backward_letters.begin(),backward_letters.end());
            
            backward_letters.erase(backward_letters.begin());
            std::string answer;
            if(backward_letters.size() == 0)
            {
                answer = forward_letters;
            }
            else
            {
                answer = forward_letters + backward_letters;
            }
            for (int space = 1; space < (input_string.size() - i); space++)
            {
            std::cout << " ";
            }
            std::cout<<answer<<std::endl;

        }
    }
}