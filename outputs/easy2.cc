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
	int a = 1;
	bool b = true;
	std::string c = "Hello"s;
	float d = 3.14;
	std::vector e = std::vector{1, 2, 3};	// ctad takes care of type parameter deduction
	std::vector f = std::vector{true, false};	// ctad takes care of type parameter deduction
	std::vector g = std::vector{"Hello"s, "World"s};	// ctad takes care of type parameter deduction
	std::unordered_map i = std::unordered_map{std::pair{"key1"s, 1}, std::pair{"key2"s, 2}, std::pair{"key3"s, 3}};	// ctad takes care of type parameter deduction
	std::unordered_map j = std::unordered_map{std::pair{"key1"s, true}, std::pair{"key2"s, false}, std::pair{"key3"s, true}};	// ctad takes care of type parameter deduction
	std::unordered_map k = std::unordered_map{std::pair{"key1"s, "Hello"s}, std::pair{"key2"s, "World"s}, std::pair{"key3"s, "!"s}};	// ctad takes care of type parameter deduction
	std::unordered_set l = std::unordered_set{1, 2, 1, 3};	// ctad takes care of type parameter deduction
	std::unordered_set m = std::unordered_set{true, false, true};	// ctad takes care of type parameter deduction
	std::unordered_set n = std::unordered_set{"Hi"s, "Hey"s, "Hi"s, "Hello"s};	// ctad takes care of type parameter deduction
	std::println("{}", a);
	std::println("{}", b);
	std::println("{}", c);
	std::println("{}", d);
	std::println("{}", e);
	std::println("{}", f);
	std::println("{}", g);
	std::println("{}", i);
	std::println("{}", j);
	std::println("{}", k);
	std::println("{}", l);
	std::println("{}", m);
	std::println("{}", n);
}


