#include <print>
#include <iomanip>
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



template <typename T>
auto format(const T& name) {
	return "Hey, "s + name + "!"s;
}



int main()
{
	std::setprecision(2);
	std::string name = "Ali"s;
	auto formatted = format(name);
	std::println("{}", formatted);
}


