#include <iostream>
#include "yaml-cpp/yaml.h"
// #include <ifstream.h>
// std::ifstream file = "config.yaml";
YAML::Node config = YAML::LoadFile(std::string("config.yaml"));
int number_of_rooms = config["number_of_rooms"].as<int>();
int tax1 = config["values"]["tax"].as<int>();



const float room_price_per_room = 30 ;//dollars
const float tax = 6; //percent
int main(int argc,char** argv[]){
    std::cout<<tax1<<"\n";
    std::cout<<"Hello! Welcome to carpet cleaning service"<<std::endl;
    std::cout<<"\nHow many rooms would you like to be cleaned? ";
    // int number_of_rooms = 0;
    // std::cin>>number_of_rooms;

    float cost = number_of_rooms * room_price_per_room;
    std::cout<<"The Estimate for cleaning service "<<std::endl;

    std::cout<<"Cost: $"<< cost<<std::endl;
    std::cout<<"Tax: $"<< cost *(tax/100)<<std::endl;
    std::cout<<"Total: $"<<cost*(1.00 + (tax/100))<<std::endl;


}