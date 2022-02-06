#include<iostream>

#include "rapidxml.hpp"
#include "rapidxml_utils.hpp"
const char* svg_path = {"/home/sibi/av-system/catkin_ws/src/common/maps/SvgPath/PPT_TB_TC_FULL.svg"};
int main()
{
    rapidxml::file<> xmlFile("/home/sibi/av-system/catkin_ws/src/common/maps/SvgPath/PPT_TB_TC_FULL.svg"); // Default template is char
    rapidxml::xml_document<> doc;
    doc.parse<0>(xmlFile.data());
    rapidxml::xml_node<> *root = doc.first_node("root-element");
    rapidxml::xml_node<> *child = root->first_node("child");
    // Get & print attribute
    rapidxml::xml_attribute<>* attr = child->first_attribute("my-attr");
    if(attr == nullptr) {
        std::cout << "No such attribute!" << std::endl;
    } 
    else 
    {
        std::cout << attr->value() << std::endl;
    }
std::cout<<"that cliche Hello World"<<std::endl;
}

