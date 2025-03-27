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
auto sum(const T& l) {
	int acc = 0;
	for (const auto& e : l) acc += e;
	return acc;
}

template <typename T>
auto average(const T& l) {
	return sum(l) / (double) std::ranges::size(l);			// single div in python results in a double
}


int main()
{
	std::setprecision(2);
	std::vector l = std::vector{1, 2, 3, 4, 8};			// ctad takes care of type parameter deduction
	auto s = sum(l);
	if (s != 0) std::println("{} {}", "Sum:"s, s);
	std::println("{} {}", "Average:"s, average(l));
}


