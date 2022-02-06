#include<iostream>
#include <fstream>
#include <set>
#include <string>
std::string filetostring()
{
	std::ifstream input("/home/sibi/americanenglish.txt");
    std::ifstream myReadFile;
    myReadFile.open("/home/sibi/americanenglish.txt");
    char output[100];
    if (myReadFile.is_open()) 
    {
        while (!myReadFile.eof()) 
        {
            myReadFile >> output;
            std::cout<<output;
        }
    }
    myReadFile.close();
    std::string fileStr;

    fileStr = "hrllo";

    return fileStr;
}
int main()
{
    std::string example = filetostring();
    
}