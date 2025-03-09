#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;

auto format(const auto& name) {
	return "Hey, "s + name + "!"s;
}

int main()
{
	auto name = "Ali"s;
	auto formatted = format(name);
	std::println("{}", formatted);
}


