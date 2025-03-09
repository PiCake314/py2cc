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
	auto x = true;
	auto y = false;
	std::println("{}", x or y);
	std::println("{}", x and y);
}


