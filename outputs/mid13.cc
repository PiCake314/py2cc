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
	auto l = std::vector{"x"s, "y"s, "z"s};
	std::println("{}", l);
	std::println("{}", l[1]);
	auto d = std::unordered_map{std::pair{"a"s, 1}, std::pair{"b"s, 2}, std::pair{"c"s, 3}};
	std::println("{}", d);
	std::println("{}", d["a"s]);
	d["z"s] = 26;
	std::println("{}", d["z"s]);
	auto s = std::unordered_set{"Hello"s, "Hi"s, "Hey"s, "Hi"s};
	std::println("{}", s);
}


