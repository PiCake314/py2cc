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


using namespace std::literals;



auto pretty_print(const auto& arg) {
	std::println("{} {}", "printing prettily:"s, arg);
}



int main()
{
	pretty_print(std::tuple{"Hello"s, "World"s});
	pretty_print(std::vector{"Hello"s, "World"s});
	pretty_print(std::unordered_map{std::pair{"Hello"s, "World"s}});
	pretty_print(std::unordered_set{"Hello"s, "World"s});
}


