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



auto greet() {
	std::println("{}", "Hello, World!"s);
}



int main()
{
	std::setprecision(2);
	greet();
}


