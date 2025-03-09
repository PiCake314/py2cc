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
	auto cond1 = true and true or false;
	auto cond2 = not cond1;
	auto x = cond1 ? "Hi"s : "Hello"s;
	auto y = cond2 ? 1 : 2;
	std::println("{} {}", x, y);
}


