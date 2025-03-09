#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;


auto sum(const auto& l) {
	auto acc = 0;
	for (const auto& e : l) acc += e;
	return acc;
}

auto average(const auto& l) {
	return sum(l) / std::ranges::size(l);
}


int main()
{
	auto l = std::vector{1, 2, 3, 4, 5};
	auto s = sum(l);
	if (s != 0) std::println("{} {}", "Sum:"s, s);
	std::println("{} {}", "Average:"s, average(l));
}


