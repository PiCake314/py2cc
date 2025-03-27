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






int main()
{
	std::setprecision(2);
	std::vector l = std::vector{"x"s, "y"s, "z"s};			// ctad takes care of type parameter deduction
	std::println("{}", l);
	std::println("{}", l[1]);
	std::unordered_map d = std::unordered_map{std::pair{"a"s, 1}, std::pair{"b"s, 2}, std::pair{"c"s, 3}};			// ctad takes care of type parameter deduction
	std::println("{}", d);
	std::println("{}", d["a"s]);
	d["z"s] = 26;
	std::println("{}", d["z"s]);
	std::unordered_set s = std::unordered_set{"Hello"s, "Hi"s, "Hey"s, "Hi"s};			// ctad takes care of type parameter deduction
	std::println("{}", s);
}


