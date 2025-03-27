#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <utility>
#include <ranges>

#include <optional>
#include <variant>
#include <any>


using std::operator""s;



auto f(std::string& s) {
	s = "Hi"s;
	std::println("{}", s);
}



int main()
{
	std::variant<int, std::string> x = 1;
	x = "Hello"s;
}


