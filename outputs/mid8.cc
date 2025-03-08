#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main()
{
	auto v = std::vector{"Hey!"s, "Name is"s, "aliiii"s};
	for (const auto& e : v) std::println("{}", e);
}


