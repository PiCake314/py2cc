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
	std::println("{}", 1 < 2 and 2 < 3);
	std::println("{}", 1 < 2 < 3);
	std::println("{}", 1 < (2 < 3));
	std::println("{}", 1 < 5 and 5 > 2 and 2 < 1);
	std::println("{}", 1 < 5 and 5 > 2 and 2 > 1);
}


