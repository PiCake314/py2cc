#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main()
{
	std::println("{}", true or true or true and true and true and true);
	std::println("{}", false or false and false);
	std::println("{}", true and false or true);
}


