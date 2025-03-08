#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main()
{
	for (const auto& i : std::ranges::views::iota(0, 5)) std::println("{}", i);
}


