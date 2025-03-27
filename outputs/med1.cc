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






int main()
{
	std::variant<double, int, std::string> x = 1;
	x = "Hi"s;
	x = 3.14;
	std::variant<bool, double, int, std::string> y;
	std::visit([&y] (const auto& value) { y = value; }, x);			// assigning to a variant requires std::visit
	y = true;
	std::variant<double, int, std::string> a = 3.14;
	std::visit([&y] (const auto& value) { y = value; }, a);			// assigning to a variant requires std::visit
	std::visit([&a] (const auto& value) { a = value; }, x);			// assigning to a variant requires std::visit
}


