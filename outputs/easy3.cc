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






int main()
{
	std::tuple x = std::tuple{1, 2};			// ctad takes care of type parameter deduction
	std::tuple y = std::tuple{"Hi"s, "Hello"s};			// ctad takes care of type parameter deduction
	std::println("{}", x);
	std::println("{}", y);
}


