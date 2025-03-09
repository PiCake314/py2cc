#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;





int main()
{
	auto name = "Ali"s;
	auto age = 23;
	std::println("{} {} {}", "Hello, my name is "s + name + " and I am"s, age, "years old"s);
}


