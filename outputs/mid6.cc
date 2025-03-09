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
	for (const auto& i : std::ranges::views::iota(0, 5)) std::println("{}", i);
}


